---
title: Deleted or merged content returns appropriate error
impact: HIGH
impactDescription: Returning 404 or 410 signals to Google that content is gone and prevents indexing of dead pages
tags: http, error
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers for the URL
---

## Deleted or merged content returns appropriate error
Returning 404 or 410 signals to Google that content is gone and prevents indexing of dead pages.

## Evidence to collect
- Header: status_code (HTTP status code)

## Logic (pseudocode)
Input: http_headers
1. Extract status_code.
2. Check if status_code is 404 or 410.

## Pass condition
Status code is 404 or 410

## Failure messages
- Removed URL returned ${observed}, expected 404 or 410

## Examples
### Passing
Removed page returns 404
```
GET /old-removed -> 404
```

### Failing
Removed page returns 200
```
GET /old-removed -> 200 OK
```

### test case passing
```json
{
  "http_headers": {
    "status_code": 404
  }
}
```

### test case failing
```json
{
  "http_headers": {
    "status_code": 200
  }
}
```

### References
Reference: [Provide errors for deleted or merged content](https://developers.google.com/search/site-move-with-url-changes.html#prepare-new-site)