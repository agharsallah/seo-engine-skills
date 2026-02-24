#!/usr/bin/env python3
"""
Sneaky Redirect Detection Script
Detects redirects that serve different content to users versus crawlers (Googlebot).
"""

import sys
import json
import argparse
import requests
from urllib.parse import urlparse, urljoin
import time
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User agent strings
USER_AGENT_REGULAR = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
USER_AGENT_GOOGLEBOT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

# Common redirect status codes
REDIRECT_CODES = {301, 302, 303, 307, 308}
SUCCESS_CODES = {200, 201, 202, 204}
CLIENT_ERROR_CODES = {400, 401, 403, 404, 405, 410, 429}
SERVER_ERROR_CODES = {500, 501, 502, 503, 504, 505}


def setup_session():
    """Setup requests session with retry strategy."""
    session = requests.Session()

    # Setup retry strategy
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def follow_redirects_with_details(session, url, user_agent, max_redirects=10, timeout=30):
    """
    Follow redirects and return detailed information about the redirect chain.

    Returns:
        dict: Contains final URL, status code, redirect chain, and analysis
    """
    redirect_chain = []
    current_url = url

    session.headers.update({"User-Agent": user_agent})

    try:
        for step in range(max_redirects + 1):
            logger.info(f"Step {step}: Requesting {current_url}")

            # Make request without following redirects
            response = session.get(current_url, allow_redirects=False, timeout=timeout, verify=True)

            step_info = {
                "step": step,
                "url": current_url,
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content_length": len(response.content),
                "content_type": response.headers.get("Content-Type", ""),
                "server": response.headers.get("Server", ""),
                "location": response.headers.get("Location", ""),
                "redirect_type": None,
            }

            # Determine redirect type
            if response.status_code in REDIRECT_CODES:
                if response.status_code == 301:
                    step_info["redirect_type"] = "Permanent Redirect"
                elif response.status_code == 302:
                    step_info["redirect_type"] = "Temporary Redirect"
                elif response.status_code == 303:
                    step_info["redirect_type"] = "See Other"
                elif response.status_code == 307:
                    step_info["redirect_type"] = "Temporary Redirect (Method Preserved)"
                elif response.status_code == 308:
                    step_info["redirect_type"] = "Permanent Redirect (Method Preserved)"

            redirect_chain.append(step_info)

            # Check if this is a redirect
            if response.status_code not in REDIRECT_CODES:
                # Final destination reached
                final_result = {
                    "final_url": current_url,
                    "final_status_code": response.status_code,
                    "redirect_count": step,
                    "redirect_chain": redirect_chain,
                    "total_time": sum(r.get("response_time", 0) for r in redirect_chain),
                    "user_agent": user_agent,
                    "success": response.status_code in SUCCESS_CODES,
                }
                return final_result

            # Get next URL from Location header
            location = response.headers.get("Location")
            if not location:
                # Redirect without location header - malformed
                final_result = {
                    "final_url": current_url,
                    "final_status_code": response.status_code,
                    "redirect_count": step,
                    "redirect_chain": redirect_chain,
                    "error": "Redirect response missing Location header",
                    "user_agent": user_agent,
                    "success": False,
                }
                return final_result

            # Handle relative URLs
            if location.startswith("/"):
                parsed_current = urlparse(current_url)
                current_url = f"{parsed_current.scheme}://{parsed_current.netloc}{location}"
            elif not location.startswith(("http://", "https://")):
                current_url = urljoin(current_url, location)
            else:
                current_url = location

        # Exceeded max redirects
        final_result = {
            "final_url": current_url,
            "final_status_code": None,
            "redirect_count": max_redirects,
            "redirect_chain": redirect_chain,
            "error": f"Exceeded maximum redirects ({max_redirects})",
            "user_agent": user_agent,
            "success": False,
        }
        return final_result

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        final_result = {
            "final_url": current_url,
            "final_status_code": None,
            "redirect_count": len(redirect_chain),
            "redirect_chain": redirect_chain,
            "error": f"Request failed: {str(e)}",
            "user_agent": user_agent,
            "success": False,
        }
        return final_result


def analyze_redirect_differences(regular_result, googlebot_result):
    """Analyze differences between regular user and Googlebot redirect behavior."""
    differences = []

    # Compare final URLs
    regular_final = regular_result.get("final_url", "")
    googlebot_final = googlebot_result.get("final_url", "")

    if regular_final != googlebot_final:
        differences.append(
            {
                "type": "final_url_mismatch",
                "description": "Final URLs differ between user agents",
                "regular_value": regular_final,
                "googlebot_value": googlebot_final,
                "severity": "HIGH",
            }
        )

    # Compare final status codes
    regular_status = regular_result.get("final_status_code")
    googlebot_status = googlebot_result.get("final_status_code")

    if regular_status != googlebot_status:
        differences.append(
            {
                "type": "final_status_mismatch",
                "description": "Final HTTP status codes differ between user agents",
                "regular_value": regular_status,
                "googlebot_value": googlebot_status,
                "severity": "HIGH",
            }
        )

    # Compare redirect counts
    regular_redirects = regular_result.get("redirect_count", 0)
    googlebot_redirects = googlebot_result.get("redirect_count", 0)

    if regular_redirects != googlebot_redirects:
        differences.append(
            {
                "type": "redirect_count_mismatch",
                "description": "Number of redirects differs between user agents",
                "regular_value": regular_redirects,
                "googlebot_value": googlebot_redirects,
                "severity": "MEDIUM",
            }
        )

    # Compare redirect chains
    regular_chain = regular_result.get("redirect_chain", [])
    googlebot_chain = googlebot_result.get("redirect_chain", [])

    # Check for different redirect patterns
    if len(regular_chain) != len(googlebot_chain):
        differences.append(
            {
                "type": "redirect_chain_length_mismatch",
                "description": "Redirect chain lengths differ",
                "regular_value": len(regular_chain),
                "googlebot_value": len(googlebot_chain),
                "severity": "MEDIUM",
            }
        )
    else:
        # Compare each step in the chain
        for i, (reg_step, gb_step) in enumerate(zip(regular_chain, googlebot_chain)):
            if reg_step.get("url") != gb_step.get("url"):
                differences.append(
                    {
                        "type": "redirect_step_mismatch",
                        "description": f"Redirect step {i} URLs differ",
                        "regular_value": reg_step.get("url"),
                        "googlebot_value": gb_step.get("url"),
                        "severity": "HIGH",
                        "step": i,
                    }
                )

            if reg_step.get("status_code") != gb_step.get("status_code"):
                differences.append(
                    {
                        "type": "redirect_step_status_mismatch",
                        "description": f"Redirect step {i} status codes differ",
                        "regular_value": reg_step.get("status_code"),
                        "googlebot_value": gb_step.get("status_code"),
                        "severity": "MEDIUM",
                        "step": i,
                    }
                )

    return differences


def analyze_url_for_sneaky_redirects(url, max_redirects=10, timeout=30):
    """Analyze a URL for sneaky redirects by testing with different user agents."""
    session = setup_session()

    try:
        logger.info(f"Analyzing URL: {url}")

        # Test with regular user agent
        logger.info("Testing with regular browser user agent...")
        regular_result = follow_redirects_with_details(session, url, USER_AGENT_REGULAR, max_redirects, timeout)

        # Wait between requests to be polite
        time.sleep(1)

        # Test with Googlebot user agent
        logger.info("Testing with Googlebot user agent...")
        googlebot_result = follow_redirects_with_details(session, url, USER_AGENT_GOOGLEBOT, max_redirects, timeout)

        # Analyze differences
        differences = analyze_redirect_differences(regular_result, googlebot_result)

        # Determine if sneaky redirect detected
        has_sneaky_redirects = len(differences) > 0
        high_severity_issues = [d for d in differences if d.get("severity") == "HIGH"]

        result = {
            "status": "success",
            "url": url,
            "passed": not has_sneaky_redirects,
            "sneaky_redirects_detected": has_sneaky_redirects,
            "differences_count": len(differences),
            "high_severity_count": len(high_severity_issues),
            "differences": differences,
            "regular_user_result": regular_result,
            "googlebot_result": googlebot_result,
            "analysis": {
                "same_final_url": regular_result.get("final_url") == googlebot_result.get("final_url"),
                "same_final_status": regular_result.get("final_status_code")
                == googlebot_result.get("final_status_code"),
                "same_redirect_count": regular_result.get("redirect_count") == googlebot_result.get("redirect_count"),
            },
        }

        if has_sneaky_redirects:
            if high_severity_issues:
                primary_issue = high_severity_issues[0]
                result["message"] = (
                    f"Sneaky redirect detected: {primary_issue['description']} - Regular: {primary_issue['regular_value']}, Googlebot: {primary_issue['googlebot_value']}"
                )
            else:
                result["message"] = (
                    f"Potential redirect inconsistencies detected ({len(differences)} differences found)"
                )
        else:
            result["message"] = "No sneaky redirects detected. Both user agents follow identical redirect patterns."

        return result

    except Exception as e:
        logger.error(f"Error analyzing URL {url}: {e}")
        return {"status": "error", "message": f"Failed to analyze URL: {str(e)}", "url": url}


def analyze_manual_redirect_data(final_url_googlebot, final_url_user, http_status_googlebot, http_status_user):
    """Analyze manually provided redirect data."""
    try:
        differences = []

        # Compare final URLs
        if final_url_googlebot != final_url_user:
            differences.append(
                {
                    "type": "final_url_mismatch",
                    "description": "Final URLs differ between user agents",
                    "regular_value": final_url_user,
                    "googlebot_value": final_url_googlebot,
                    "severity": "HIGH",
                }
            )

        # Compare status codes
        if http_status_googlebot != http_status_user:
            differences.append(
                {
                    "type": "final_status_mismatch",
                    "description": "Final HTTP status codes differ between user agents",
                    "regular_value": http_status_user,
                    "googlebot_value": http_status_googlebot,
                    "severity": "HIGH",
                }
            )

        has_sneaky_redirects = len(differences) > 0

        result = {
            "status": "success",
            "passed": not has_sneaky_redirects,
            "sneaky_redirects_detected": has_sneaky_redirects,
            "differences_count": len(differences),
            "differences": differences,
            "input_data": {
                "final_url_googlebot": final_url_googlebot,
                "final_url_user": final_url_user,
                "http_status_googlebot": http_status_googlebot,
                "http_status_user": http_status_user,
            },
            "analysis": {
                "same_final_url": final_url_googlebot == final_url_user,
                "same_final_status": http_status_googlebot == http_status_user,
            },
        }

        if has_sneaky_redirects:
            result["message"] = (
                f"Sneaky redirect detected: Googlebot ends at '{final_url_googlebot}' (status {http_status_googlebot}) while user ends at '{final_url_user}' (status {http_status_user})"
            )
        else:
            result["message"] = (
                "No sneaky redirects detected. Both user agents have identical final destinations and status codes."
            )

        return result

    except Exception as e:
        logger.error(f"Error analyzing manual data: {e}")
        return {"status": "error", "message": f"Failed to analyze manual data: {str(e)}"}


def main():
    parser = argparse.ArgumentParser(
        description="Detect sneaky redirects that serve different content to users vs crawlers"
    )
    parser.add_argument("--url", help="URL to analyze for sneaky redirects")

    # Manual input options (matching the original rule format)
    parser.add_argument("--final-url-googlebot", help="Final URL after redirect for Googlebot")
    parser.add_argument("--final-url-user", help="Final URL after redirect for regular user")
    parser.add_argument("--http-status-googlebot", type=int, help="HTTP status code for Googlebot")
    parser.add_argument("--http-status-user", type=int, help="HTTP status code for user")

    parser.add_argument("--max-redirects", type=int, default=10, help="Maximum redirects to follow (default: 10)")
    parser.add_argument("--timeout", type=int, default=30, help="Request timeout in seconds (default: 30)")
    parser.add_argument("--output", help="Output file for results", default="sneaky_redirect_results.json")

    args = parser.parse_args()

    # Check input parameters
    manual_params = [args.final_url_googlebot, args.final_url_user, args.http_status_googlebot, args.http_status_user]
    has_manual_params = any(param is not None for param in manual_params)
    has_all_manual_params = all(param is not None for param in manual_params)

    if args.url:
        if has_manual_params:
            print("Warning: Both URL and manual parameters provided. Using URL analysis.")
        result = analyze_url_for_sneaky_redirects(args.url, args.max_redirects, args.timeout)
    elif has_all_manual_params:
        result = analyze_manual_redirect_data(
            args.final_url_googlebot, args.final_url_user, args.http_status_googlebot, args.http_status_user
        )
    elif has_manual_params:
        print(
            "Error: All manual parameters are required (final-url-googlebot, final-url-user, http-status-googlebot, http-status-user)"
        )
        sys.exit(1)
    else:
        print("Error: Must provide either --url or all manual parameters")
        sys.exit(1)

    # Output results
    print(json.dumps(result, indent=2))

    # Save to file if specified
    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)

    # Exit with appropriate code
    sys.exit(0 if result.get("passed", False) else 1)


if __name__ == "__main__":
    main()
