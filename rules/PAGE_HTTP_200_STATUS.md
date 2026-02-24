---
title: Page returns HTTP 200 status
impact: CRITICAL
impactDescription: Google indexes only pages that respond with a successful 200 status.
tags: http,status
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers containing the status code to evaluate.
---

## PAGE_HTTP_200_STATUS
If the server doesn’t return **200 OK**, the page is not eligible for normal indexing.

## Evidence to collect
- **http_status: status_code** — Numeric status code from response headers

## Logic (pseudocode)
Input: http_headers
1. status = http_headers.status_code
2. If status == 200 -> pass; else -> fail

## Pass condition
HTTP status code equals 200.

## Failure messages
Page returned HTTP status ${observed} instead of 200

## Examples
### Passing
HTTP/1.1 200 OK
Content-Type: text/html

### Failing
HTTP/1.1 404 Not Found
Content-Type: text/html

### References
Google Search technical requirements — “The page works (it's not an error page)” — https://developers.google.com/search/docs/advanced/crawling/overview

