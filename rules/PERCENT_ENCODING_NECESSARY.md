---
title: Percent‑encode non‑ASCII characters in URLs
impact: MEDIUM
impactDescription: Percent‑encoding ensures URLs are valid, crawlable, and correctly interpreted by search engines
tags: url, encoding
inputFields:
  - name: html
    required: true
    description: HTML content of the page to extract href attributes.
---

## Percent‑encode non‑ASCII characters in URLs
Percent‑encoding ensures URLs are valid, crawlable, and correctly interpreted by search engines.

## Evidence to collect
- Collect each link's href value (a[href])

## Logic (pseudocode)
Input: html
1. Parse html and collect all href attributes from <a> tags.
2. For each href:
   a. Decode percent‑encoded sequences.
   b. If any character in the decoded URL has a code point > 127 (non‑ASCII) and is not percent‑encoded, record as violation.
3. If any violations recorded, result = fail else pass.

## Pass condition
All URLs contain only ASCII characters or properly percent‑encoded sequences.

## Failure messages
- URL contains unencoded non‑ASCII characters: ${observed}

## Examples
### Passing
URL with percent‑encoded Unicode characters.
```html
<a href="https://example.com/%E6%9D%82%E8%B4%A7/%E8%96%84%E8%8D%B7">Link</a>
```

### Failing
URL contains raw Unicode characters.
```html
<a href="https://example.com/杂货/蔬菜">Link</a>
```

### test case passing
```html
<html><body><a href="https://example.com/%E6%9D%82%E8%B4%A7"></a></body></html>
```

### test case failing
```html
<html><body><a href="https://example.com/杂货"></a></body></html>
```

### References
Reference: [URL structure best practices for Google Search](https://developers.google.com/search/docs/advanced/crawling/url-structure)