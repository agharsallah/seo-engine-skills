---
title: Confirm Googlebot can access the new site (HTTP 200)
impact: CRITICAL
impactDescription: Googlebot must be able to retrieve pages to index them after the move
tags: accessibility, googlebot
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers including the status code.
---

## Confirm Googlebot can access the new site (HTTP 200)
Googlebot must be able to retrieve pages to index them after the move.

## Evidence to collect
- HTTP Status: status_code (HTTP response status for the requested URL.)

## Logic (pseudocode)
Input: http_headers
1. Retrieve the HTTP status code from http_headers (e.g., headers[':status'] or similar).
2. If status code equals 200, set pass; otherwise, set fail.

## Pass condition
HTTP status code is 200.

## Failure messages
- Googlebot received HTTP status ${observed} instead of 200.

## Examples
### Passing
HTTP 200 response.
```
HTTP/1.1 200 OK
```

### Failing
HTTP 404 response.
```
HTTP/1.1 404 Not Found
```

### test case passing
```json
{
  "http_headers": {
    ":status": 200
  }
}
```

### test case failing
```json
{
  "http_headers": {
    ":status": 404
  }
}
```

### References
Reference: [Changing Your Web Hosting and SEO](https://developers.google.com/search/docs/hosting/migrate)