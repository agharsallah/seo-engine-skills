#!/usr/bin/env python3
"""
Hidden Text Detection Script
Detects text or links that are visually hidden but present in HTML for SEO manipulation.
"""

import sys
import json
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_driver():
    """Setup headless Chrome driver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        logger.error(f"Failed to setup Chrome driver: {e}")
        return None


def is_element_hidden(driver, element):
    """
    Check if an element is visually hidden using various techniques.
    Returns (is_hidden, reason) tuple.
    """
    try:
        # Get computed styles
        is_displayed = element.is_displayed()

        # Check CSS properties that indicate hiding
        css_checks = [
            ("display", "none"),
            ("visibility", "hidden"),
            ("opacity", "0"),
        ]

        for prop, hidden_value in css_checks:
            value = element.value_of_css_property(prop)
            if value == hidden_value:
                return True, f"{prop}: {hidden_value}"

        # Check for zero dimensions
        size = element.size
        if size["width"] == 0 or size["height"] == 0:
            return True, f"zero dimensions: {size['width']}x{size['height']}"

        # Check for positioning off-screen
        location = element.location
        if location["x"] < -9999 or location["y"] < -9999:
            return True, f"positioned off-screen: x={location['x']}, y={location['y']}"

        # Check text-indent hiding
        text_indent = element.value_of_css_property("text-indent")
        if text_indent and ("-9999" in text_indent or "-999" in text_indent):
            return True, f"negative text-indent: {text_indent}"

        # Check font-size hiding
        font_size = element.value_of_css_property("font-size")
        if font_size and (font_size == "0px" or font_size == "0"):
            return True, f"zero font-size: {font_size}"

        # Check color hiding (text same color as background)
        color = element.value_of_css_property("color")
        bg_color = element.value_of_css_property("background-color")
        if color and bg_color and color == bg_color and color != "rgba(0, 0, 0, 0)":
            return True, f"text color matches background: {color}"

        # Check if element is not displayed according to Selenium
        if not is_displayed:
            return True, "element not displayed (Selenium check)"

        return False, None

    except Exception as e:
        logger.warning(f"Error checking element visibility: {e}")
        return False, None


def extract_text_content(element):
    """Extract meaningful text content from element."""
    try:
        text = element.get_attribute("textContent") or ""
        text = re.sub(r"\s+", " ", text).strip()
        return text
    except:
        return ""


def has_links(element):
    """Check if element contains anchor tags."""
    try:
        links = element.find_elements(By.TAG_NAME, "a")
        return len(links) > 0, len(links)
    except:
        return False, 0


def analyze_url_for_hidden_text(url):
    """Analyze a URL for hidden text detection."""
    driver = setup_driver()
    if not driver:
        return {"status": "error", "message": "Failed to setup browser driver"}

    hidden_elements = []

    try:
        # Load the page
        driver.get(url)
        time.sleep(3)  # Wait for page to fully load

        # Find all text-containing elements
        text_elements = driver.find_elements(By.XPATH, "//*[text()]")

        # Also check for elements that might contain links
        link_containers = driver.find_elements(By.XPATH, "//*[.//a]")

        # Combine and deduplicate
        all_elements = list(set(text_elements + link_containers))

        for element in all_elements:
            try:
                # Check if element is hidden
                is_hidden, reason = is_element_hidden(driver, element)

                if is_hidden:
                    # Extract text content
                    text_content = extract_text_content(element)
                    has_link, link_count = has_links(element)

                    # Only flag if there's meaningful content
                    if (text_content and len(text_content.split()) >= 2) or has_link:
                        tag_name = element.tag_name

                        # Get element attributes for identification
                        element_id = element.get_attribute("id") or ""
                        element_class = element.get_attribute("class") or ""

                        hidden_elements.append(
                            {
                                "tag": tag_name,
                                "id": element_id,
                                "class": element_class,
                                "text_content": text_content[:200],  # Truncate long text
                                "text_length": len(text_content),
                                "has_links": has_link,
                                "link_count": link_count,
                                "hiding_method": reason,
                                "selector": f"{tag_name}{'#' + element_id if element_id else ''}{'.' + element_class.replace(' ', '.') if element_class else ''}",
                            }
                        )

            except Exception as e:
                logger.warning(f"Error processing element: {e}")
                continue

    except Exception as e:
        logger.error(f"Error analyzing URL {url}: {e}")
        return {"status": "error", "message": f"Failed to analyze URL: {str(e)}"}

    finally:
        driver.quit()

    # Determine pass/fail
    has_hidden_text = len(hidden_elements) > 0

    result = {
        "status": "success",
        "url": url,
        "passed": not has_hidden_text,
        "hidden_elements_count": len(hidden_elements),
        "hidden_elements": hidden_elements,
        "evidence": {
            "total_hidden_elements": len(hidden_elements),
            "elements_with_text": len([e for e in hidden_elements if e["text_length"] > 0]),
            "elements_with_links": len([e for e in hidden_elements if e["has_links"]]),
        },
    }

    if has_hidden_text:
        result["message"] = f"Hidden text detected in {len(hidden_elements)} element(s). "
        if hidden_elements:
            primary_element = hidden_elements[0]
            result["message"] += (
                f"Primary violation: {primary_element['hiding_method']} on {primary_element['selector']}"
            )
    else:
        result["message"] = "No hidden text or links detected."

    return result


def analyze_html_for_hidden_text(html_content):
    """Analyze HTML content for hidden text patterns using static analysis."""
    hidden_patterns = []

    try:
        soup = BeautifulSoup(html_content, "html.parser")

        # Check for common CSS hiding patterns in style attributes
        elements_with_style = soup.find_all(attrs={"style": True})

        for element in elements_with_style:
            style = element.get("style", "").lower()
            text_content = element.get_text(strip=True)
            has_links = bool(element.find("a"))

            # Skip if no meaningful content
            if not text_content and not has_links:
                continue

            # Check for hiding patterns
            hiding_methods = []

            if "display:none" in style.replace(" ", ""):
                hiding_methods.append("display: none")
            if "visibility:hidden" in style.replace(" ", ""):
                hiding_methods.append("visibility: hidden")
            if "opacity:0" in style.replace(" ", ""):
                hiding_methods.append("opacity: 0")
            if "font-size:0" in style.replace(" ", ""):
                hiding_methods.append("font-size: 0")
            if re.search(r"text-indent:\s*-\d{3,}", style):
                hiding_methods.append("negative text-indent")
            if re.search(r"position:\s*absolute.*left:\s*-\d{3,}", style):
                hiding_methods.append("positioned off-screen")

            if hiding_methods:
                hidden_patterns.append(
                    {
                        "tag": element.name,
                        "id": element.get("id", ""),
                        "class": element.get("class", []),
                        "text_content": text_content[:200],
                        "text_length": len(text_content),
                        "has_links": has_links,
                        "hiding_methods": hiding_methods,
                        "style": style,
                    }
                )

    except Exception as e:
        logger.error(f"Error analyzing HTML: {e}")
        return {"status": "error", "message": f"Failed to analyze HTML: {str(e)}"}

    has_hidden_text = len(hidden_patterns) > 0

    return {
        "status": "success",
        "passed": not has_hidden_text,
        "hidden_elements_count": len(hidden_patterns),
        "hidden_elements": hidden_patterns,
        "evidence": {
            "total_hidden_elements": len(hidden_patterns),
            "elements_with_text": len([e for e in hidden_patterns if e["text_length"] > 0]),
            "elements_with_links": len([e for e in hidden_patterns if e["has_links"]]),
        },
        "message": f"Hidden text detected in {len(hidden_patterns)} element(s)."
        if has_hidden_text
        else "No hidden text patterns detected.",
    }


def main():
    parser = argparse.ArgumentParser(description="Detect hidden text in web content")
    parser.add_argument("--url", help="URL to analyze for hidden text")
    parser.add_argument("--html", help="HTML content to analyze")
    parser.add_argument("--html-file", help="Path to a local .html file to analyze")
    parser.add_argument("--output", help="Output file for results", default="hidden_text_results.json")

    args = parser.parse_args()

    if args.url:
        result = analyze_url_for_hidden_text(args.url)
    elif args.html:
        result = analyze_html_for_hidden_text(args.html)
    elif args.html_file:
        try:
            with open(args.html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
            result = analyze_html_for_hidden_text(html_content)
        except Exception as e:
            print(f"Error reading HTML file: {e}")
            sys.exit(1)
    else:
        print("Error: Must provide either --url, --html, or --html-file parameter")
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
