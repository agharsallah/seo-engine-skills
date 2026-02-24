---
title: Consistent use of HTTPS scheme
impact: LOW
impactDescription: The documentation lists the page's protocol (HTTP vs HTTPS) as a factor that influences canonicalization
tags: protocol, canonical
inputFields:
  - name: url
    required: true
    description: The absolute URL of the page being evaluated.
---

## Consistent use of HTTPS scheme
The documentation lists the page's protocol (HTTP vs HTTPS) as a factor that influences canonicalization.

## Evidence to collect
- Captures the scheme part of the URL (^(https?)://)

## Logic (pseudocode)
Input: url
1. Extract the scheme (http or https) from the URL using a regex.
2. If scheme == "https", set consistent = true; else consistent = false.

## Pass condition
The page is served over HTTPS.

## Failure messages
- Page URL ${url} is not served over HTTPS.

## Examples
### Passing
URL uses HTTPS.
```
https://example.com/page
```

### Failing
URL uses HTTP.
```
http://example.com/page
```

### test case passing
```
https://example.com/page
```

### test case failing
```
http://example.com/page
```

### References
Reference: [What is URL Canonicalization](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls)