---
title: rel="canonical" HTTP header must use an absolute URL
impact: MEDIUM
impactDescription: Documentation states that absolute URLs must be used in the rel="canonical" HTTP header
tags: canonical, http
inputFields:
  - name: http_headers
    required: true
    description: Dictionary of response headers.
---

## rel="canonical" HTTP header must use an absolute URL
Documentation states that absolute URLs must be used in the rel="canonical" HTTP header.

## Evidence to collect
- Parse Link header for rel="canonical"

## Logic (pseudocode)
Input: http_headers
1. Retrieve all 'Link' header values.
2. For each value, split by commas and parse parameters.
3. If a segment has rel="canonical", extract the URL inside <>.
4. If URL matches ^https?://, pass; else fail.

## Pass condition
The URL associated with rel="canonical" in the Link header is absolute.

## Failure messages
- Canonical Link header URL '${observed}' is not absolute.

## Examples
### Passing
Proper absolute URL in Link header.
```
Link: <https://example.com/page.html>; rel="canonical"
```

### Failing
Relative URL in Link header.
```
Link: </page.html>; rel="canonical"
```

### test case passing
```
Link: <https://example.com/page.html>; rel="canonical"
```

### test case failing
```
Link: </page.html>; rel="canonical"
```

### References
Reference: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/advanced/canonical/rel-canonical)