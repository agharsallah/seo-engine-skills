#!/usr/bin/env python3
"""
Sitemap fetcher for SEO analysis.
Extracts sitemap.xml from a domain and saves it.
"""

import sys
import requests
from urllib.parse import urlparse, urljoin
import xml.etree.ElementTree as ET
import re


def fetch_sitemap(url, output_file=None):
    """
    Fetch sitemap.xml file from a domain and save to file.

    Args:
        url (str): Target URL or domain
        output_file (str, optional): Output filename. If None, auto-generates based on domain.

    Returns:
        str: Path to saved sitemap file
    """
    try:
        # Handle different URL formats
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        # Parse URL to get the base domain
        parsed = urlparse(url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"

        print(f"Searching for sitemap at: {base_url}")

        # Generate output filename if not provided
        if output_file is None:
            domain = parsed.netloc.replace("www.", "")
            output_file = f"{domain}_sitemap.xml"

        # Common sitemap locations to try
        sitemap_locations = [
            "/sitemap.xml",
            "/sitemap_index.xml",
            "/sitemap.xml.gz",
            "/sitemaps/sitemap.xml",
            "/sitemaps.xml",
        ]

        sitemap_url = None
        content = None

        # First, check robots.txt for sitemap declaration
        try:
            robots_url = urljoin(base_url, "/robots.txt")
            robots_response = requests.get(robots_url, timeout=10)
            if robots_response.status_code == 200:
                # Look for Sitemap: declarations in robots.txt
                sitemap_matches = re.findall(r"Sitemap:\s*(https?://[^\s]+)", robots_response.text, re.IGNORECASE)
                if sitemap_matches:
                    # Try the first sitemap found in robots.txt
                    sitemap_locations.insert(0, sitemap_matches[0])
                    print(f"Found sitemap reference in robots.txt: {sitemap_matches[0]}")
        except:
            pass  # Continue if robots.txt check fails

        # Try each potential sitemap location
        for location in sitemap_locations:
            if location.startswith("http"):
                test_url = location  # Full URL from robots.txt
            else:
                test_url = urljoin(base_url, location)

            try:
                print(f"Trying: {test_url}")
                response = requests.get(
                    test_url,
                    timeout=15,
                    headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-Engine/1.0; +https://example.com/bot)"},
                )

                if response.status_code == 200:
                    content = response.text
                    sitemap_url = test_url
                    print(f"✓ Found sitemap at: {test_url}")
                    break

            except requests.RequestException:
                continue

        # If no sitemap found, create a placeholder
        if content is None:
            content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- No sitemap found for {base_url} -->
<!-- Checked locations: {", ".join(sitemap_locations)} -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- No URLs found - sitemap may not exist or be accessible -->
</urlset>"""
            print("✗ No sitemap found - created placeholder")

        # Save sitemap content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✓ Sitemap saved to: {output_file}")
        print(f"  Size: {len(content):,} characters")

        # Basic XML analysis if we found actual content
        if sitemap_url:
            try:
                root = ET.fromstring(content)

                # Count URLs in sitemap
                url_count = 0
                if root.tag.endswith("urlset"):
                    # Standard sitemap
                    url_elements = root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url")
                    url_count = len(url_elements)
                elif root.tag.endswith("sitemapindex"):
                    # Sitemap index
                    sitemap_elements = root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap")
                    url_count = len(sitemap_elements)
                    print("  Type: Sitemap Index")
                    print(f"  Sub-sitemaps: {url_count}")
                    return output_file

                print("  Type: Standard Sitemap")
                print(f"  URLs: {url_count:,}")

            except ET.ParseError as e:
                print(f"  Warning: XML parsing error: {e}")
            except Exception as e:
                print(f"  Warning: Analysis error: {e}")

        return output_file

    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None


def main():
    """Command-line interface for sitemap fetching."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_sitemap.py <url> [output_file]")
        print("Example: python fetch_sitemap.py https://example.com")
        print("Example: python fetch_sitemap.py example.com custom_sitemap.xml")
        print()
        print("This script will:")
        print("  1. Check robots.txt for sitemap declarations")
        print("  2. Try common sitemap locations (/sitemap.xml, etc.)")
        print("  3. Analyze the sitemap structure and URL count")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = fetch_sitemap(url, output_file)
    if result:
        print("Success! Sitemap ready for SEO analysis.")
    else:
        print("Failed to fetch sitemap.")
        sys.exit(1)


if __name__ == "__main__":
    main()
