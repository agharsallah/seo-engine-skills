---
title: robots.txt must not return HTTP 503 status
impact: HIGH
impactDescription: A 503 response for robots.txt blocks all crawling, preventing indexing
tags: robots.txt, crawling, http-status
inputFields:
  - name: robots_txt
    required: true
    description: Content of the robots.txt file (if fetched successfully).
  - name: http_status
    required: true
    description: HTTP status code returned when fetching robots.txt.
---

## robots.txt must not return HTTP 503 status
A 503 response for robots.txt blocks all crawling, preventing indexing.

## Evidence to collect
- HTTP status code of the robots.txt request

## Logic (pseudocode)
Input: http_status (status code for robots.txt)
1. If http_status == 503 then result = fail.
2. Otherwise result = pass.

## Pass condition
robots.txt HTTP status code is not 503.

## Failure messages
- robots.txt returned a 503 Service Unavailable status, which blocks crawling.

## Examples
### Passing
robots.txt fetched successfully with 200 status.
```
User-agent: *
Allow: /
```

### Failing
robots.txt request returns 503.

### test case passing
```
User-agent: *
Allow: /
```

### test case failing
```
HTTP 503 Service Unavailable
```

### References
Reference: [Temporarily pause or disable a website](https://developers.google.com/search/docs/monitor-site/temporarily-pause-or-disable-website)