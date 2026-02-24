---
title: 503 error pages must include a Retry-After header
impact: MEDIUM
impactDescription: Provides crawlers with guidance on when to retry, reducing unnecessary load
tags: http-503, retry-after, crawl-rate
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers for the requested URL.
  - name: http_status
    required: true
    description: HTTP status code of the response.
---

## 503 error pages must include a Retry-After header
Provides crawlers with guidance on when to retry, reducing unnecessary load.

## Evidence to collect
- Value of the Retry-After response header

## Logic (pseudocode)
Input: http_status, http_headers
1. If http_status != 503, result = not_applicable.
2. If http_status == 503:
   a. Check if 'Retry-After' header exists and is non-empty.
   b. If present, result = pass; else result = fail.

## Pass condition
When a response has status 503, a non-empty Retry-After header is present.

## Failure messages
- 503 response missing Retry-After header.

## Examples
### Passing
503 response includes Retry-After header.
```
HTTP/1.1 503 Service Unavailable
Retry-After: Wed, 21 Oct 2026 07:28:00 GMT
```

### Failing
503 response without Retry-After header.
```
HTTP/1.1 503 Service Unavailable
```

### test case passing
```
HTTP/1.1 503 Service Unavailable
Retry-After: Wed, 21 Oct 2026 07:28:00 GMT
```

### test case failing
```
HTTP/1.1 503 Service Unavailable
```

### References
Reference: [Temporarily pause or disable a website](https://developers.google.com/search/docs/monitor-site/temporarily-pause-or-disable-website)