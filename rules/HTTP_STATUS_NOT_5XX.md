---
title: Verify page does not return a server error status
impact: HIGH
impactDescription: HTTP 5xx responses indicate server errors that prevent Googlebot from successfully crawling the page.
tags: crawling, http_status
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers including the status code
---

## Verify page does not return a server error status
HTTP 5xx responses indicate server errors that prevent Googlebot from successfully crawling the page.

## Evidence to collect
- Numeric HTTP status code from the response

## Logic (pseudocode)
Inputs: http_headers (object with field status_code)
1. Retrieve status_code from http_headers.
2. If status_code >= 500 and status_code < 600, set error = true.
3. Else, error = false.

## Pass condition
HTTP status code is not in the 5xx range.

## Failure messages
Page returned HTTP status ${observed}, which indicates a server error.

## Examples
### Passing
Page returns 200 OK.
```
http_headers:
  status_code: 200
```

### Failing
Page returns 503 Service Unavailable.
```
http_headers:
  status_code: 503
```

### test case passing
```
HTTP Status: 200
```

### test case failing
```
HTTP Status: 502
```

### References
Reference: [In-depth guide to how Google Search works](https://developers.google.com/search/docs/crawling-indexing/overview)