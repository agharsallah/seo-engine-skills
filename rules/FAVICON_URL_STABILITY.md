---
title: Ensure favicon URL is stable and not frequently changed
impact: LOW
impactDescription: A stable favicon URL prevents Google from losing the association between the site and its favicon, ensuring consistent display in search results.
tags: favicon, url, stability
inputFields:
  - name: html
    required: true
    description: HTML of the home page to locate the favicon link.
---

## Ensure favicon URL is stable and not frequently changed
A stable favicon URL prevents Google from losing the association between the site and its favicon, ensuring consistent display in search results.

## Evidence to collect
- Favicon URL: `link[rel~='icon'], link[rel='apple-touch-icon'], link[rel='apple-touch-icon-precomposed']`

## Logic (pseudocode)
1. Extract favicon_href from html.
2. If favicon_href contains a query string (e.g., "?v=123") OR
   matches a pattern indicating versioned filenames (e.g., "favicon-*.ico")
   THEN flag as unstable.
3. Otherwise, consider the URL stable.

## Pass condition
The favicon href does not contain a query component and does not match a versioned filename pattern.

## Failure messages
Favicon URL '${href}' appears to be dynamic (contains query parameters or versioned filename).

## Examples
### Passing
Simple stable path.
```html
<link rel="icon" href="/favicon.ico">
```

### Failing
URL with version query.
```html
<link rel="icon" href="/favicon.ico?v=20240101">
```

### test case passing
```html
<link rel='icon' href='/favicon.ico'>
```

### test case failing
```html
<link rel='icon' href='/favicon.ico?v=20240101'>
```

### References
Reference: [Define Website Favicon for Search Results](https://developers.google.com/search/docs/appearance/favicon)