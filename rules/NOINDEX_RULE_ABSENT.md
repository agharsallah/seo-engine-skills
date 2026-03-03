---
title: Ensure noindex robots rule is not present on new site pages
impact: MEDIUM
impactDescription: Prevents accidental indexing of the test site before it goes live
tags: robots, indexing
inputFields:
  - name: html
    required: true
    description: HTML content of the page to inspect meta robots tags.
  - name: http_headers
    required: true
    description: HTTP response headers to inspect X-Robots-Tag.
---

## Ensure noindex robots rule is not present on new site pages
Prevents accidental indexing of the test site before it goes live.

## Evidence to collect
- Selector: meta[name="robots"] (Check for presence of 'noindex' token (case‑insensitive).)
- Header: X-Robots-Tag (Check for presence of 'noindex' token (case‑insensitive).)

## Logic (pseudocode)
Inputs: html, http_headers
1. Extract content of meta[name="robots"] from html.
2. Extract value of X-Robots-Tag header from http_headers.
3. If either value contains the token "noindex" (case‑insensitive), set fail.
4. Otherwise, set pass.

## Pass condition
No 'noindex' directive found in meta robots tags or X‑Robots‑Tag header.

## Failure messages
- Found 'noindex' directive in ${location}: ${observed}

## Examples
### Passing
Page without noindex directives.
```html
<meta name="robots" content="index, follow">
```

### Failing
Page with a noindex meta tag.
```html
<meta name="robots" content="noindex, nofollow">
```

### test case passing
```html
<html><head><meta name="robots" content="index, follow"></head></html>
```

### test case failing
```html
<html><head><meta name="robots" content="noindex"></head></html>
```

### References
Reference: [Changing Your Web Hosting and SEO](https://developers.google.com/search/docs/hosting/migrate)