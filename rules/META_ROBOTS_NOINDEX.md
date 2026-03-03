---
title: Ensure meta robots tag does not block indexing
impact: HIGH
impactDescription: A meta robots tag containing "noindex" tells Google not to index the page, preventing it from appearing in search results.
tags: indexing, meta_robots
inputFields:
  - name: html
    required: true
    description: Full HTML source of the page
---

## Ensure meta robots tag does not block indexing
A meta robots tag containing "noindex" tells Google not to index the page, preventing it from appearing in search results.

## Evidence to collect
- Content attribute of the meta robots tag: `meta[name='robots'][content]`

## Logic (pseudocode)
Inputs: html (string)
1. Parse html and locate <meta name="robots"> element.
2. If element exists, read its content attribute.
3. Convert content to lower case and split by commas.
4. If any token equals "noindex", set blocked = true.
5. Else, blocked = false.

## Pass condition
Meta robots tag is absent or does not contain "noindex".

## Failure messages
Meta robots tag contains 'noindex', preventing indexing.

## Examples
### Passing
No meta robots tag or tag without noindex.
```html
<head>
  <title>Example Page</title>
</head>
```

### Failing
Meta robots tag includes noindex.
```html
<head>
  <meta name="robots" content="noindex, nofollow">
</head>
```

### test case passing
```html
<html><head><title>Test</title></head><body></body></html>
```

### test case failing
```html
<html><head><meta name="robots" content="noindex"></head><body></body></html>
```

### References
Reference: [In-depth guide to how Google Search works](https://developers.google.com/search/docs/crawling-indexing/overview)