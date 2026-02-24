---
title: Use rel="canonical" on test variant URLs
impact: MEDIUM
impactDescription: rel=canonical signals the preferred URL, preventing duplicate indexing of test variants
tags: canonical, duplicate_content
inputFields:
  - name: html
    required: true
    description: Full HTML of the page being evaluated.
---

## Use rel="canonical" on test variant URLs
rel=canonical signals the preferred URL, preventing duplicate indexing of test variants.

## Evidence to collect
- Extract the href attribute of the canonical link element (link[rel="canonical"])

## Logic (pseudocode)
Input: html
1. Parse HTML and locate <link rel="canonical"> element.
2. If element exists and href attribute is non‑empty, result = PASS.
3. Otherwise, result = FAIL.

## Pass condition
A <link rel="canonical"> element with a non‑empty href is present in the HTML.

## Failure messages
- Missing or empty rel=canonical link on test variant page.

## Examples
### Passing
Page includes a proper canonical link.
```html
<link rel="canonical" href="https://example.com/original-page">
```

### Failing
No canonical link present.
```html
<!-- missing rel=canonical -->
```

### test case passing
```html
<html><head><link rel="canonical" href="https://example.com/home"></head></html>
```

### test case failing
```html
<html><head></head></html>
```

### References
Reference: [A/B Testing Best Practices for Search](https://developers.google.com/search/docs/ab-testing)