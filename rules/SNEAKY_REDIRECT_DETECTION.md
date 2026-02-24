---
title: Detect redirects that serve different content to users versus crawlers
impact: HIGH
impactDescription: Sneaky redirects deceive users or search engines by showing different destinations.
tags: redirects
script: ../scripts/sneaky_redirect_detection/sneaky_redirect_detection.py
inputFields:
  - name: url
    required: false
    description: URL to analyze for sneaky redirects using dual user agent testing.
  - name: final_url_googlebot
    required: false
    description: Final URL after redirect for Googlebot (manual analysis).
  - name: final_url_user
    required: false
    description: Final URL after redirect for regular user (manual analysis).
  - name: http_status_googlebot
    required: false
    description: HTTP status code for Googlebot (manual analysis).
  - name: http_status_user
    required: false
    description: HTTP status code for user (manual analysis).
  - name: max_redirects
    required: false
    default: 10
    description: Maximum number of redirects to follow during analysis.
---

## SNEAKY_REDIRECT_DETECTION
Detects sneaky redirects that serve different content or destinations to users versus crawlers using both automated URL testing and manual data analysis.

## Evidence to collect
- Complete redirect chains for both user agents
- Final URLs and HTTP status codes
- Redirect step-by-step comparison
- Response headers and timing information
- Difference analysis with severity levels

## Logic (pseudocode)  
Input: url OR (final_url_googlebot, final_url_user, http_status_googlebot, http_status_user)
1. If URL provided:
   - Make HTTP requests with regular browser user agent
   - Make HTTP requests with Googlebot user agent  
   - Follow redirect chains up to max_redirects (default: 10)
   - Track each redirect step: URL, status code, headers, redirect type
   - Record final destinations and status codes
2. If manual data provided:
   - Use provided final URLs and status codes for comparison
3. Analyze differences between user agents:
   - Compare final URLs (HIGH severity if different)
   - Compare final status codes (HIGH severity if different)
   - Compare redirect chain lengths (MEDIUM severity if different)
   - Compare individual redirect steps (HIGH/MEDIUM based on impact)
4. Determine sneaky redirect presence based on difference severity
5. Provide detailed analysis and evidence

## Technical Implementation Notes
- Uses requests library with custom User-Agent headers for each test
- Implements retry strategy for handling temporary network issues
- Properly handles all HTTP redirect codes (301, 302, 303, 307, 308)
- Resolves relative redirects to absolute URLs correctly
- Includes rate limiting between requests (1 second delay)
- Tracks complete redirect chain with detailed step information
- Categorizes differences by severity (HIGH/MEDIUM/LOW)
- Provides comprehensive JSON output with evidence

## Pass condition
Both user agents (regular browser and Googlebot) follow identical redirect patterns with same final URLs and HTTP status codes.

## Failure messages
Sneaky redirect detected: ${difference_description} - Regular: ${regular_value}, Googlebot: ${googlebot_value}

## Examples
### Passing
Googlebot and user both end at https://example.com/page (status 200).

### Failing
Googlebot ends at https://example.com/spam (status 302), user ends at https://example.com/page (status 200).

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/redirects