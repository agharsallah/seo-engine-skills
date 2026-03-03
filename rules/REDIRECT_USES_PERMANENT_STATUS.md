---
title: Redirect uses permanent HTTP status
impact: HIGH
impactDescription: Permanent redirects (301/308) preserve link equity and signal the move to Google
tags: redirect, seo
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers for the old URL
---

## Redirect uses permanent HTTP status
Permanent redirects (301/308) preserve link equity and signal the move to Google.

## Evidence to collect
- Header: status_code (HTTP status code of the response)

## Logic (pseudocode)
Input: http_headers
1. Extract status_code from http_headers.
2. Check if status_code is 301 or 308.

## Pass condition
Status code is 301 or 308

## Failure messages
- Redirect returned ${observed} instead of 301 or 308

## Examples
### Passing
Old URL returns 301
```
GET /old -> 301 Location: /new
```

### Failing
Old URL returns 302
```
GET /old -> 302 Location: /new
```

### test case passing
```json
{
  "http_headers": {
    "status_code": 301
  }
}
```

### test case failing
```json
{
  "http_headers": {
    "status_code": 302
  }
}
```

### References
Reference: [Plan your redirect strategy](https://developers.google.com/search/301-redirects.html)