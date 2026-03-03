#!/usr/bin/env python3
"""
Simple PageSpeed Insights metrics fetcher.
- Uses official Google API Python client.
- Loads API key from .env (PAGESPEED_API_KEY or GOOGLE_API_KEY).
- Generates 'metrics.json' by default (or a filename you pass).
- Keeps the same CLI input pattern as before: <url> [output_file] [--local]
"""

import sys
import json
import os
import time
from dotenv import load_dotenv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


CATEGORIES = ["PERFORMANCE", "SEO", "ACCESSIBILITY", "BEST_PRACTICES"]
DEFAULT_STRATEGY = "DESKTOP"  # You can change to 'MOBILE' if needed


def run_pagespeed(url: str):
    """Call PageSpeed Insights API via google-api-python-client."""
    load_dotenv()
    api_key = os.getenv("PAGESPEED_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("✗ Missing API key. Set PAGESPEED_API_KEY (or GOOGLE_API_KEY) in your .env")
        sys.exit(1)

    service = build("pagespeedonline", "v5", developerKey=api_key)
    request = service.pagespeedapi().runpagespeed(url=url, category=CATEGORIES, strategy=DEFAULT_STRATEGY)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            return request.execute()
        except HttpError as e:
            status = getattr(e.resp, "status", None)
            if status == 429 and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 10
                print(f"⏳ Rate limited (429). Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            print(f"✗ PageSpeed API failed: {e}")
            sys.exit(1)
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5
                print(f"⏳ Request error, retrying in {wait_time}s... ({e})")
                time.sleep(wait_time)
                continue
            print(f"✗ Request failed after retries: {e}")
            sys.exit(1)


def ensure_url_scheme(url: str) -> str:
    """Ensure the URL has http/https scheme."""
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def transform_to_lighthouse_like(response: dict, url: str) -> dict:
    """
    Convert PageSpeed response to a Lighthouse-like structure with:
    - lighthouseVersion
    - requestedUrl, finalUrl
    - fetchTime
    - categories (performance/seo/accessibility/best-practices with scores)
    - audits (if available)
    - loadingExperience / originLoadingExperience (if available)
    """
    lr = response.get("lighthouseResult", {}) or {}
    categories = lr.get("categories", {}) or {}

    out = {
        "lighthouseVersion": lr.get("lighthouseVersion", response.get("lighthouseVersion", "Unknown")),
        "requestedUrl": url,
        "finalUrl": response.get("id", url),
        "fetchTime": time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "categories": {},
    }

    # PSI returns lowercase keys for categories in lighthouseResult
    mapping = {
        "performance": "performance",
        "seo": "seo",
        "accessibility": "accessibility",
        "best-practices": "best-practices",
    }

    for k_api, k_out in mapping.items():
        if k_api in categories:
            c = categories[k_api] or {}
            out["categories"][k_out] = {"id": k_out, "title": c.get("title", k_out.title()), "score": c.get("score", 0)}

    audits = lr.get("audits", {}) or {}
    if audits:
        out["audits"] = audits

    le = response.get("loadingExperience")
    if le:
        out["loadingExperience"] = le

    ole = response.get("originLoadingExperience")
    if ole:
        out["originLoadingExperience"] = ole

    return out


def save_json(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def summarize_scores(lh: dict) -> dict:
    scores = {}
    cats = lh.get("categories", {})
    for k, cat in cats.items():
        score = cat.get("score")
        if score is not None:
            scores[f"{k}_score"] = round(score * 100, 1)
    return scores


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_lighthouse.py <url> [output_file] [--local]")
        print("Example: python fetch_lighthouse.py https://example.com")
        print("Example: python fetch_lighthouse.py example.com metrics.json")
        print("Example: python fetch_lighthouse.py https://example.com --local")
        print()
        print("Notes:")
        print("  - Uses Google PageSpeed Insights API via google-api-python-client")
        print("  - API key loaded from .env: PAGESPEED_API_KEY (or GOOGLE_API_KEY)")
        print("  - Default output file: metrics.json")
        sys.exit(1)

    url = ensure_url_scheme(sys.argv[1])

    # Defaults
    output_file = "metrics.json"
    # Keep accepting --local to preserve input compatibility (ignored)
    # Parse remaining args
    for arg in sys.argv[2:]:
        if arg == "--local":
            print("ℹ️  '--local' is accepted for compatibility but ignored. Using PageSpeed API.")
        elif not arg.startswith("--"):
            output_file = arg

    print(f"Running PageSpeed Insights for: {url}")
    print("This may take 10–30 seconds...")

    response = run_pagespeed(url)
    lighthouse_like = transform_to_lighthouse_like(response, url)
    save_json(lighthouse_like, output_file)

    scores = summarize_scores(lighthouse_like)
    print(f"✓ PageSpeed Insights data saved to: {output_file}")
    if "performance_score" in scores:
        print(f"  Performance: {scores['performance_score']}/100")
    if "seo_score" in scores:
        print(f"  SEO: {scores['seo_score']}/100")
    if "accessibility_score" in scores:
        print(f"  Accessibility: {scores['accessibility_score']}/100")
    if "best-practices_score" in scores:
        print(f"  Best Practices: {scores['best-practices_score']}/100")

    print("\n✅ Success! Lighthouse-like metrics ready for SEO analysis.")
    print("🚀 Used Google API Python client with PageSpeed Insights.")


if __name__ == "__main__":
    main()
