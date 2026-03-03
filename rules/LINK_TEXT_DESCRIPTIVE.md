---
title: Verify that anchor text is non‑empty and descriptive
impact: MEDIUM
impactDescription: Descriptive anchor text helps users and search engines understand linked content.
tags: links, anchor-text
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page.
---

## Verify that anchor text is non‑empty and descriptive
Descriptive anchor text helps users and search engines understand linked content.

## Evidence to collect
- Text content of each anchor element: `a`

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse html into a DOM.
2. For each <a> element:
   a. Retrieve its visible text (trim whitespace).
   b. If text is empty, record a failure.
3. If any failures recorded, result = fail; else result = pass.

## Pass condition
All anchor elements have non‑empty visible text.

## Failure messages
Anchor at index ${index} has empty link text.

## Examples
### Passing
Anchor with descriptive text.
```html
<a href="/about">About Our Company</a>
```

### Failing
Anchor with no text.
```html
<a href="/contact"></a>
```

### test case passing
```html
<html><body><a href="/home">Home</a></body></html>
```

### test case failing
```html
<html><body><a href="/login"></a></body></html>
```

### References
Reference: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)