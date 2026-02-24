#!/usr/bin/env python3
"""
Keyword Stuffing Detection Script
Detects excessive repetition of keywords indicative of keyword stuffing.
"""

import sys
import json
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Common stop words to exclude from keyword density analysis
STOP_WORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "but",
    "in",
    "on",
    "at",
    "to",
    "for",
    "of",
    "with",
    "by",
    "from",
    "up",
    "about",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "between",
    "among",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "will",
    "would",
    "should",
    "could",
    "can",
    "may",
    "might",
    "must",
    "this",
    "that",
    "these",
    "those",
    "i",
    "you",
    "he",
    "she",
    "it",
    "we",
    "they",
    "me",
    "him",
    "her",
    "us",
    "them",
    "my",
    "your",
    "his",
    "its",
    "our",
    "their",
    "mine",
    "yours",
    "ours",
    "theirs",
    "myself",
    "yourself",
    "himself",
    "herself",
    "itself",
    "ourselves",
    "yourselves",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "whose",
    "where",
    "when",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "just",
    "now",
}


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


def extract_visible_text(html_content):
    """Extract visible text content from HTML body."""
    try:
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove script and style elements
        for element in soup(["script", "style", "meta", "noscript"]):
            element.decompose()

        # Get body content or fall back to entire document
        body = soup.find("body")
        if body:
            text = body.get_text()
        else:
            text = soup.get_text()

        # Clean up whitespace
        text = re.sub(r"\s+", " ", text).strip()
        return text

    except Exception as e:
        logger.error(f"Error extracting text: {e}")
        return ""


def tokenize_and_normalize(text):
    """Tokenize text into normalized words."""
    # Convert to lowercase
    text = text.lower()

    # Extract words (alphanumeric sequences)
    words = re.findall(r"\b[a-zA-Z]{2,}\b", text)

    # Filter out stop words and very short words
    meaningful_words = [word for word in words if word not in STOP_WORDS and len(word) >= 3]

    return words, meaningful_words


def calculate_keyword_density(words, meaningful_words, density_threshold=0.05):
    """Calculate keyword density and identify potential stuffing."""
    total_words = len(words)
    meaningful_total = len(meaningful_words)

    if total_words == 0:
        return [], {"total_words": 0, "meaningful_words": 0, "unique_words": 0, "density_threshold": density_threshold}

    # Count word frequencies
    word_counts = Counter(meaningful_words)

    keyword_violations = []

    for word, count in word_counts.items():
        # Calculate density against total words (including stop words)
        density = count / total_words
        density_percentage = density * 100

        if density > density_threshold:
            keyword_violations.append(
                {
                    "keyword": word,
                    "count": count,
                    "density": round(density, 4),
                    "density_percentage": round(density_percentage, 2),
                    "threshold": density_threshold,
                    "threshold_percentage": density_threshold * 100,
                }
            )

    # Sort by density (highest first)
    keyword_violations.sort(key=lambda x: x["density"], reverse=True)

    stats = {
        "total_words": total_words,
        "meaningful_words": meaningful_total,
        "unique_words": len(word_counts),
        "density_threshold": density_threshold,
        "top_keywords": [
            {
                "keyword": word,
                "count": count,
                "density": round(count / total_words, 4),
                "density_percentage": round((count / total_words) * 100, 2),
            }
            for word, count in word_counts.most_common(10)
        ],
    }

    return keyword_violations, stats


def analyze_url_for_keyword_stuffing(url, density_threshold=0.05):
    """Analyze a URL for keyword stuffing."""
    driver = setup_driver()
    if not driver:
        return {"status": "error", "message": "Failed to setup browser driver"}

    try:
        # Load the page
        driver.get(url)
        time.sleep(3)  # Wait for page to fully load

        # Get page HTML
        html_content = driver.page_source

        # Extract page title for context
        try:
            title = driver.title
        except:
            title = "Unknown"

    except Exception as e:
        logger.error(f"Error loading URL {url}: {e}")
        return {"status": "error", "message": f"Failed to load URL: {str(e)}"}

    finally:
        driver.quit()

    # Analyze the HTML content
    result = analyze_html_for_keyword_stuffing(html_content, density_threshold)
    result["url"] = url
    result["title"] = title

    return result


def analyze_html_for_keyword_stuffing(html_content, density_threshold=0.05):
    """Analyze HTML content for keyword stuffing."""
    try:
        # Extract visible text
        visible_text = extract_visible_text(html_content)

        if not visible_text:
            return {
                "status": "success",
                "passed": True,
                "message": "No text content found to analyze",
                "violations": [],
                "stats": {
                    "total_words": 0,
                    "meaningful_words": 0,
                    "unique_words": 0,
                    "density_threshold": density_threshold,
                },
            }

        # Tokenize and normalize
        all_words, meaningful_words = tokenize_and_normalize(visible_text)

        # Calculate keyword density
        violations, stats = calculate_keyword_density(all_words, meaningful_words, density_threshold)

        has_keyword_stuffing = len(violations) > 0

        result = {
            "status": "success",
            "passed": not has_keyword_stuffing,
            "violations_count": len(violations),
            "violations": violations,
            "stats": stats,
            "text_preview": visible_text[:200] + "..." if len(visible_text) > 200 else visible_text,
        }

        if has_keyword_stuffing:
            primary_violation = violations[0]
            result["message"] = (
                f"Keyword stuffing detected: '{primary_violation['keyword']}' "
                f"density {primary_violation['density_percentage']}% "
                f"exceeds allowed maximum of {primary_violation['threshold_percentage']}%"
            )
        else:
            result["message"] = f"No keyword stuffing detected. Analyzed {stats['total_words']} words."

        return result

    except Exception as e:
        logger.error(f"Error analyzing HTML: {e}")
        return {"status": "error", "message": f"Failed to analyze HTML: {str(e)}"}


def main():
    parser = argparse.ArgumentParser(description="Detect keyword stuffing in web content")
    parser.add_argument("--url", help="URL to analyze for keyword stuffing")
    parser.add_argument("--html", help="HTML content string to analyze")
    parser.add_argument("--html-file", help="Path to a local .html file to analyze")
    parser.add_argument(
        "--threshold", type=float, default=0.05, help="Keyword density threshold (0-1, default: 0.05 = 5%)"
    )
    parser.add_argument("--output", help="Output file for results", default="keyword_stuffing_results.json")

    args = parser.parse_args()

    # Validate threshold
    if not 0 < args.threshold <= 1:
        print("Error: Threshold must be between 0 and 1")
        sys.exit(1)

    if args.url:
        result = analyze_url_for_keyword_stuffing(args.url, args.threshold)
    elif args.html:
        result = analyze_html_for_keyword_stuffing(args.html, args.threshold)
    elif args.html_file:
        try:
            with open(args.html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
            result = analyze_html_for_keyword_stuffing(html_content, args.threshold)
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
