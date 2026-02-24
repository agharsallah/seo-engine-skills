---
title: Do not use robots.txt for canonicalization
impact: LOW
impactDescription: Documentation explicitly advises against using robots.txt for canonicalization
tags: robots.txt, canonical
inputFields:
  - name: robots_txt
    required: true
    description: Content of the robots.txt file.
---

## Do not use robots.txt for canonicalization
Documentation explicitly advises against using robots.txt for canonicalization.

## Evidence to collect
- Search for any occurrence of the word 'canonical' in robots.txt

## Logic (pseudocode)
Input: robots_txt
1. Search the file for the case-insensitive word "canonical".
2. If found, result = fail; else pass.

## Pass condition
robots.txt does not contain the term "canonical".

## Failure messages
- robots.txt contains canonical directives which are not supported for canonicalization.

## Examples
### Passing
robots.txt without canonical references.
```
User-agent: *
Disallow:
```

### Failing
robots.txt containing a canonical directive.
```
User-agent: *
Disallow: /private/
# canonical: https://example.com/page.html
```

### test case passing
```
User-agent: *
Disallow:
```

### test case failing
```
User-agent: *
Disallow:
# canonical: https://example.com/page.html
```

### References
Reference: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/advanced/canonical/rel-canonical)