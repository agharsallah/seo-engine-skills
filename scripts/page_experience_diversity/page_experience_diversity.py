#!/usr/bin/env python3
"""
PAGE_EXPERIENCE_DIVERSITY checker
Verifies that at least 5 out of 7 core page experience signals pass
"""

import sys
import json


def check_page_experience_diversity(lighthouse_metrics):
    """Check if at least 5 of 7 core page experience signals pass"""

    # Define the 7 core page experience signals
    signals = [
        "LCP",  # Largest Contentful Paint
        "FID",  # First Input Delay
        "CLS",  # Cumulative Layout Shift
        "mobile_friendly",
        "safe_browsing",
        "https",
        "no_intrusive_interstitials",
    ]

    pass_count = 0
    signal_results = {}

    # Count passing signals
    for signal in signals:
        passed = lighthouse_metrics.get(signal, False)
        signal_results[signal] = passed
        if passed:
            pass_count += 1

    # Need at least 5 passing signals
    required_passes = 5
    passed_overall = pass_count >= required_passes

    return {
        "passed": passed_overall,
        "pass_count": pass_count,
        "required_passes": required_passes,
        "signal_results": signal_results,
        "message": f"Passed {pass_count} of {len(signals)} signals (need {required_passes})",
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 page_experience_diversity.py <lighthouse_metrics_json_file>")
        sys.exit(1)

    metrics_file = sys.argv[1]

    try:
        # Read lighthouse metrics
        with open(metrics_file, "r", encoding="utf-8") as f:
            lighthouse_metrics = json.load(f)

        # Check page experience diversity
        result = check_page_experience_diversity(lighthouse_metrics)
        result["rule_id"] = "PAGE_EXPERIENCE_DIVERSITY"

        print(json.dumps(result, indent=2))

        # Exit with appropriate code
        sys.exit(0 if result["passed"] else 1)

    except Exception as e:
        error_result = {
            "rule_id": "PAGE_EXPERIENCE_DIVERSITY",
            "passed": False,
            "error": str(e),
            "message": f"Error checking page experience: {str(e)}",
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
