---
title: Presence of rel="canonical" link element
impact: MEDIUM
impactDescription: rel="canonical" link annotations are listed as a factor that influences how Google determines the canonical URL
tags: canonical, link
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page to be evaluated.
---

## Presence of rel="canonical" link element
rel="canonical" link annotations are listed as a factor that influences how Google determines the canonical URL.

## Evidence to collect
- href attribute of canonical link element (link[rel='canonical'])

## Logic (pseudocode)
Input: html
1. Parse the HTML document.
2. Search for a <link> element with rel attribute equal to "canonical".
3. If such an element exists, capture its href attribute as observed_canonical.
4. If no element is found, observed_canonical = null.

## Pass condition
The page contains a <link rel="canonical"> element with a non‑empty href attribute.

## Failure messages
- Missing rel="canonical" link element on the page.

## Examples
### Passing
Page includes a proper canonical link.
```html
<head><link rel="canonical" href="https://example.com/page"></head>
```

### Failing
Page lacks a canonical link.
```html
<head></head>
```

### test case passing
```html
<html><head><link rel="canonical" href="https://example.com/page"></head></html>
```

### test case failing
```html
<html><head></head></html>
```

### References
Reference: [What is URL Canonicalization](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls)