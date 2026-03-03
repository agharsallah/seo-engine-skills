---
title: Site should be served over HTTPS
impact: HIGH
impactDescription: HTTPS provides security for users and is recommended by Google as a ranking signal.
tags: security, https
inputFields:
  - name: url
    required: true
    description: The canonical URL of the site to evaluate.
---

## Site should be served over HTTPS
HTTPS provides security for users and is recommended by Google as a ranking signal.

## Evidence to collect
- URL scheme (http or https)

## Logic (pseudocode)
Input: url
1. Parse the URL and extract its scheme component.
2. If scheme equals "https", the check passes.
3. Otherwise, it fails.

## Pass condition
URL scheme is https.

## Failure messages
Site is served over HTTP instead of HTTPS.

## Examples
### Passing
URL uses HTTPS.
```
https://www.example.com
```

### Failing
URL uses HTTP.
```
http://www.example.com
```

### test case passing
```
https://www.example.com
```

### test case failing
```
http://www.example.com
```

### References
Reference: [Technical SEO Techniques and Strategies](https://developers.google.com/search/docs/technical-seo)