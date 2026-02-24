---
title: Main heading (<h1>) present and non-empty
impact: LOW
impactDescription: Main headings are highlighted as prominent locations for keywords.
tags: seo
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for the presence of <h1> elements.
---

## MAIN_HEADING_EXISTS
Ensures the page has at least one <h1> element with non-empty text, which is important for SEO and keyword prominence.

## Evidence to collect
- Presence and text content of <h1> elements

## Logic (pseudocode)
Input: html
1. Parse html into a DOM.
2. Select all <h1> elements.
3. If no <h1> elements found, result = fail.
4. For each <h1>, trim its text content.
5. If any trimmed text is non‑empty, result = pass; otherwise fail.

## Pass condition
At least one <h1> element exists with non‑empty text.

## Failure messages
No non‑empty <h1> heading found on the page.

## Examples
### Passing
<h1>Welcome to My Site</h1>

### Failing
<h1>   </h1>
<!-- No <h1> present -->

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/headings