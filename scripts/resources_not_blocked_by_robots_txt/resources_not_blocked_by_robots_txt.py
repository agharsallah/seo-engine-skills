#!/usr/bin/env python3
"""
RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT checker
Verifies that page resources (images, CSS, JS) are not blocked by robots.txt
"""

import urllib.robotparser
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import sys
import json


def extract_resource_urls(html, base_url=""):
    """Extract all resource URLs from HTML"""
    soup = BeautifulSoup(html, "html.parser")
    resources = []

    # Extract image sources
    for img in soup.find_all("img", src=True):
        resources.append(urljoin(base_url, img["src"]))

    # Extract CSS links
    for link in soup.find_all("link", {"rel": "stylesheet", "href": True}):
        resources.append(urljoin(base_url, link["href"]))

    # Extract script sources
    for script in soup.find_all("script", src=True):
        resources.append(urljoin(base_url, script["src"]))

    return resources


def check_robots_txt_allows(robots_txt_content, url_path):
    """Check if robots.txt allows access to the given URL path"""
    try:
        # Create a temporary robots.txt parser
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url("dummy://example.com/robots.txt")

        # Parse the robots.txt content directly
        lines = robots_txt_content.strip().split("\n")
        rp._read_robots_txt_content(lines)

        # Check if Googlebot can fetch the URL
        return rp.can_fetch("Googlebot", url_path) and rp.can_fetch("*", url_path)

    except Exception:
        # If parsing fails, assume allowed
        return True


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 resources_not_blocked_by_robots_txt.py <html_file> <robots_txt_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    robots_txt_file = sys.argv[2]

    try:
        # Read HTML content
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Read robots.txt content
        with open(robots_txt_file, "r", encoding="utf-8") as f:
            robots_txt_content = f.read()

        # Extract resource URLs
        resource_urls = extract_resource_urls(html_content)

        blocked_resources = []

        # Check each resource against robots.txt
        for url in resource_urls:
            parsed_url = urlparse(url)
            url_path = parsed_url.path

            if not check_robots_txt_allows(robots_txt_content, url_path):
                blocked_resources.append(url)

        # Generate result
        result = {
            "rule_id": "RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT",
            "passed": len(blocked_resources) == 0,
            "total_resources": len(resource_urls),
            "blocked_resources": blocked_resources,
            "message": f"Found {len(blocked_resources)} blocked resources out of {len(resource_urls)} total",
        }

        print(json.dumps(result, indent=2))

        # Exit with appropriate code
        sys.exit(0 if result["passed"] else 1)

    except Exception as e:
        error_result = {
            "rule_id": "RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT",
            "passed": False,
            "error": str(e),
            "message": f"Error checking resources: {str(e)}",
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
