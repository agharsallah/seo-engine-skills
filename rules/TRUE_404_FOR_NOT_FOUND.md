---
title: Return proper 404 status for missing pages
impact: HIGH
impactDescription: A true 404 response signals to Google that a page is permanently unavailable; soft 404s can mislead indexing.
tags: http, 404
inputFields:
  - name: http_status
    required: true
    description: HTTP response status code for the requested URL.
---

## Return proper 404 status for missing pages
A true 404 response signals to Google that a page is permanently unavailable; soft 404s can mislead indexing.

## Evidence to collect
- Numeric HTTP status code

## Logic (pseudocode)
Input: http_status
1. If http_status equals 404, the check passes.
2. Otherwise, it fails.

## Pass condition
HTTP status code is 404.

## Failure messages
Page returned status ${observed} instead of 404.

## Examples
### Passing
Server returns a 404 for a removed page.
```
GET /old-page.html HTTP/1.1
Host: example.com

HTTP/1.1 404 Not Found
```

### Failing
Server returns 200 with a custom not‑found page (soft 404).
```
GET /old-page.html HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
```

### test case passing
```
HTTP Status: 404
```

### test case failing
```
HTTP Status: 200
<h1>Page not found</h1>
```

### References
Reference: [Technical SEO Techniques and Strategies](https://developers.google.com/search/docs/technical-seo)