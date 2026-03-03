---
title: Redirect chain length limit
impact: MEDIUM
impactDescription: Long redirect chains add latency and may exceed Googlebot's limit
tags: redirect, chain
inputFields:
  - name: url
    required: true
    description: Starting URL to evaluate redirect chain
---

## Redirect chain length limit
Long redirect chains add latency and may exceed Googlebot's limit.

## Evidence to collect
- Metric: redirect_hops (Number of redirects followed until final destination)

## Logic (pseudocode)
Input: url
1. Follow redirects from url, counting each 3xx response until a non-redirect response is received or a loop is detected.
2. Record hop_count.

## Pass condition
hop_count <= 5

## Failure messages
- Redirect chain has ${observed} hops, exceeding the recommended maximum of 5

## Examples
### Passing
Three-step redirect chain
```
1 -> 2 -> 3 -> final (3 hops)
```

### Failing
Seven-step redirect chain
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> final (7 hops)
```

### test case passing
```
http://example.com/start3
```

### test case failing
```
http://example.com/start7
```

### References
Reference: [Avoid chaining redirects](https://developers.google.com/search/301-redirects.html)