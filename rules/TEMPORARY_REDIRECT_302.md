---
title: Use 302 redirects for temporary test redirects
impact: MEDIUM
impactDescription: A 302 redirect signals a temporary change, ensuring the original URL remains indexed
tags: redirect, temporary_redirect
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers of the URL that performs the redirect.
---

## Use 302 redirects for temporary test redirects
A 302 redirect signals a temporary change, ensuring the original URL remains indexed.

## Evidence to collect
- Capture the HTTP status code returned for the redirect request

## Logic (pseudocode)
Input: http_headers
1. Retrieve status = http_headers["status_code"]
2. If status == 302 then result = PASS
3. Else result = FAIL

## Pass condition
The HTTP status code for the redirect response is 302.

## Failure messages
- Redirect uses status code ${observed} instead of required 302.

## Examples
### Passing
Server returns a 302 temporary redirect.
```
HTTP/1.1 302 Found
Location: https://example.com/variant
```

### Failing
Server returns a 301 permanent redirect.
```
HTTP/1.1 301 Moved Permanently
Location: https://example.com/variant
```

### test case passing
```
HTTP/1.1 302 Found
```

### test case failing
```
HTTP/1.1 301 Moved Permanently
```

### References
Reference: [A/B Testing Best Practices for Search](https://developers.google.com/search/docs/ab-testing)