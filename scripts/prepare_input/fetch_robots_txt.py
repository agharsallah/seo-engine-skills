#!/usr/bin/env python3
"""
Robots.txt fetcher for SEO analysis.
Extracts robots.txt file from a domain and saves it.
"""

import sys
import requests
from urllib.parse import urlparse, urljoin


def fetch_robots_txt(url, output_file=None):
    """
    Fetch robots.txt file from a domain and save to file.

    Args:
        url (str): Target URL or domain
        output_file (str, optional): Output filename. If None, auto-generates based on domain.

    Returns:
        str: Path to saved robots.txt file
    """
    try:
        # Handle different URL formats
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        # Parse URL to get the base domain
        parsed = urlparse(url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        robots_url = urljoin(base_url, "/robots.txt")

        print(f"Fetching robots.txt from: {robots_url}")

        # Fetch robots.txt
        response = requests.get(
            robots_url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-Engine/1.0; +https://example.com/bot)"},
        )

        # Generate output filename if not provided
        if output_file is None:
            domain = parsed.netloc.replace("www.", "")
            output_file = f"{domain}_robots.txt"

        # Handle different response codes
        if response.status_code == 200:
            content = response.text
            status_msg = "Found"
        elif response.status_code == 404:
            content = "# robots.txt not found (404)\n# This means all robots are allowed to crawl all content\n"
            status_msg = "Not found (404) - using default allow all"
        else:
            content = f"# robots.txt returned HTTP {response.status_code}\n# Status: {response.reason}\n"
            status_msg = f"HTTP {response.status_code}"

        # Save robots.txt content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✓ robots.txt saved to: {output_file}")
        print(f"  Status: {status_msg}")
        print(f"  Size: {len(content):,} characters")

        # Basic analysis
        lines = [line.strip() for line in content.split("\n") if line.strip() and not line.startswith("#")]
        if lines:
            user_agents = [line for line in lines if line.lower().startswith("user-agent:")]
            disallows = [line for line in lines if line.lower().startswith("disallow:")]
            allows = [line for line in lines if line.lower().startswith("allow:")]

            print(f"  User-agents: {len(user_agents)}")
            print(f"  Disallow rules: {len(disallows)}")
            print(f"  Allow rules: {len(allows)}")

        return output_file

    except requests.RequestException as e:
        print(f"✗ Error fetching robots.txt: {e}")

        # Create a fallback file documenting the error
        if output_file is None:
            try:
                parsed = urlparse(url if url.startswith(("http://", "https://")) else "https://" + url)
                domain = parsed.netloc.replace("www.", "")
                output_file = f"{domain}_robots.txt"
            except:
                output_file = "robots_error.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Error fetching robots.txt: {e}\n")
            f.write(f"# URL attempted: {robots_url}\n")
            f.write("# Assuming default behavior: allow all robots\n")

        print(f"✓ Error documented in: {output_file}")
        return output_file

    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None


def main():
    """Command-line interface for robots.txt fetching."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_robots_txt.py <url> [output_file]")
        print("Example: python fetch_robots_txt.py https://example.com")
        print("Example: python fetch_robots_txt.py example.com custom_robots.txt")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = fetch_robots_txt(url, output_file)
    if result:
        print("Success! robots.txt ready for SEO analysis.")
    else:
        print("Failed to fetch robots.txt.")
        sys.exit(1)


if __name__ == "__main__":
    main()
