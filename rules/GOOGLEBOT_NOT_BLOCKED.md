---
title: Googlebot is not blocked by robots.txt
impact: HIGH
impactDescription: Google must be able to crawl the page; robots.txt disallow rules that match the URL prevent indexing.
tags: accessibility
inputFields:
  - name: robots_txt
    required: true
    description: robots.txt file content to evaluate.
  - name: url
    required: true
    description: URL of the page to check against robots.txt rules.
---

## GOOGLEBOT_NOT_BLOCKED
Ensures Googlebot is not blocked from crawling the page by robots.txt rules.

## Evidence to collect
- Disallow rules for Googlebot or * in robots.txt
- URL path to check against Disallow rules

## Logic (pseudocode)
Input: robots_txt, url
1. Parse robots_txt line by line.
2. Identify sections where User-agent is "Googlebot" or "*".
3. For each Disallow rule in those sections, resolve the path.
4. If the URL path starts with any Disallow path, set blocked = true.
5. If blocked is true, result = fail else result = pass.

## Pass condition
No Disallow rule for Googlebot (or *) matches the page URL.

## Failure messages
Robots.txt disallows Googlebot from accessing ${url}

## Examples
### Passing
User-agent: Googlebot
Disallow:

### Failing
User-agent: Googlebot
Disallow: /private

### References
Google Search documentation — https://developers.google.com/search/docs/advanced/crawling/overview