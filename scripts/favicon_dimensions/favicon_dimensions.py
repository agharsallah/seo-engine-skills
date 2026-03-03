#!/usr/bin/env python3
"""
FAVICON_DIMENSIONS checker
Verifies that favicon is square and at least 8x8 pixels
"""

import sys
import json
from PIL import Image
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os


def extract_favicon_url(html, base_url=""):
    """Extract favicon URL from HTML"""
    soup = BeautifulSoup(html, "html.parser")

    # Look for various favicon link elements
    selectors = ['link[rel~="icon"]', 'link[rel="apple-touch-icon"]', 'link[rel="apple-touch-icon-precomposed"]']

    for selector in selectors:
        link = soup.select_one(selector)
        if link and link.get("href"):
            return urljoin(base_url, link["href"])

    # Fallback to default /favicon.ico
    return urljoin(base_url, "/favicon.ico")


def check_favicon_dimensions(favicon_url):
    """Check if favicon meets dimension requirements"""
    try:
        # Download favicon
        response = requests.get(favicon_url, timeout=10)
        response.raise_for_status()

        # Save temporarily
        temp_path = "/tmp/favicon_temp"
        with open(temp_path, "wb") as f:
            f.write(response.content)

        # Open with PIL
        with Image.open(temp_path) as img:
            width, height = img.size

            # Clean up temp file
            os.unlink(temp_path)

            # Check if square and at least 8x8
            is_square = width == height
            min_size_met = width >= 8 and height >= 8

            return {
                "passed": is_square and min_size_met,
                "width": width,
                "height": height,
                "is_square": is_square,
                "min_size_met": min_size_met,
                "message": f"Favicon dimensions: {width}x{height}px",
            }

    except Exception as e:
        return {"passed": False, "error": str(e), "message": f"Error checking favicon dimensions: {str(e)}"}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 favicon_dimensions.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]

    try:
        # Read HTML content
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Extract favicon URL
        favicon_url = extract_favicon_url(html_content)

        # Check dimensions
        result = check_favicon_dimensions(favicon_url)
        result["rule_id"] = "FAVICON_DIMENSIONS"
        result["favicon_url"] = favicon_url

        print(json.dumps(result, indent=2))

        # Exit with appropriate code
        sys.exit(0 if result["passed"] else 1)

    except Exception as e:
        error_result = {
            "rule_id": "FAVICON_DIMENSIONS",
            "passed": False,
            "error": str(e),
            "message": f"Error processing favicon: {str(e)}",
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
