---
title: Avoid URL fragments that change content
impact: HIGH
impactDescription: Google Search may not crawl URLs where fragments are used to change content
tags: url, crawlability
inputFields:
  - name: html
    required: true
    description: HTML content of the page to extract href attributes.
---

## Avoid URL fragments that change content
Google Search may not crawl URLs where fragments are used to change content, leading to inefficient crawling.

## Evidence to collect
- Collect each link's href value (a[href])

## Logic (pseudocode)
Input: html
1. Parse html and collect all href attributes from <a> tags.
2. For each href, if it contains a '#' character:
   a. Extract the fragment part after '#'.
   b. If fragment is non‑empty, record as violation.
3. If any violations recorded, result = fail else pass.

## Pass condition
No href attribute contains a non‑empty fragment identifier.

## Failure messages
- Link with fragment found: ${observed}

## Examples
### Passing
Page with links that have no fragments.
```html
<a href="https://example.com/page">Link</a>
```

### Failing
Page with a link that uses a fragment to change content.
```html
<a href="https://example.com/page#section1">Link</a>
```

### test case passing
```html
<html><body><a href="https://example.com/page"></a></body></html>
```

### test case failing
```html
<html><body><a href="https://example.com/page#intro"></a></body></html>
```

### References
Reference: [URL structure best practices for Google Search](https://developers.google.com/search/docs/advanced/crawling/url-structure)