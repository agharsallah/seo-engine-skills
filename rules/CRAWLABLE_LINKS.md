---
title: All anchor links are crawlable (have valid href)
impact: LOW
impactDescription: Crawlable links enable Google to discover other pages on the site.
tags: seo
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for anchor link crawlability.
---

## CRAWLABLE_LINKS
Ensures all <a> elements have valid href attributes that are crawlable by search engines.

## Evidence to collect
- Presence and value of href attributes for all <a> elements

## Logic (pseudocode)
Input: html
1. Parse html into a DOM.
2. Select all <a> elements.
3. For each <a>, retrieve its 'href' attribute.
4. If href is missing, empty, or starts with "javascript:", result = fail.
5. If all anchors have valid href values, result = pass.

## Pass condition
Every <a> element has a non‑empty href that does not start with "javascript:".

## Failure messages
Anchor link with text '${text}' has an invalid or missing href.

## Examples
### Passing
<a href="/about">About Us</a>

### Failing
<a>Contact</a>
<a href="javascript:void(0)">Home</a>

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/links