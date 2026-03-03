#!/usr/bin/env python3
"""
Simple HTML fetcher for SEO analysis.
Extracts HTML content from a URL and saves it to a file.
"""

import sys
import requests
from urllib.parse import urlparse


def fetch_html(url, output_file=None):
    """
    Fetch HTML content from a URL and save to file.

    Args:
        url (str): Target URL to fetch
        output_file (str, optional): Output filename. If None, auto-generates based on URL.

    Returns:
        str: Path to saved HTML file
    """
    try:
        # Add https:// if no protocol specified
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        print(f"Fetching HTML from: {url}")

        # Fetch the page
        response = requests.get(
            url,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-Engine/1.0; +https://example.com/bot)"},
        )
        response.raise_for_status()

        # Generate output filename if not provided
        if output_file is None:
            parsed = urlparse(url)
            domain = parsed.netloc.replace("www.", "")
            output_file = f"{domain}.html"

        # Save HTML content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"✓ HTML saved to: {output_file}")
        print(f"  Size: {len(response.text):,} characters")
        print(f"  Status: {response.status_code}")

        return output_file

    except requests.RequestException as e:
        print(f"✗ Error fetching HTML: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None


def main():
    """Command-line interface for HTML fetching."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_html.py <url> [output_file]")
        print("Example: python fetch_html.py https://example.com")
        print("Example: python fetch_html.py example.com custom_output.html")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = fetch_html(url, output_file)
    if result:
        print("Success! HTML content ready for SEO analysis.")
    else:
        print("Failed to fetch HTML content.")
        sys.exit(1)


if __name__ == "__main__":
    main()
