---
title: Use hyphens to separate words in URL path
impact: MEDIUM
impactDescription: Hyphens improve readability for users and search engines, aiding crawlability and ranking
tags: url, readability
inputFields:
  - name: html
    required: true
    description: HTML content of the page to extract href attributes.
---

## Use hyphens to separate words in URL path
Hyphens improve readability for users and search engines, aiding crawlability and ranking.

## Evidence to collect
- Collect each link's href value (a[href])

## Logic (pseudocode)
Input: html
1. Parse html and collect all href attributes from <a> tags.
2. For each href:
   a. Extract the path component (portion after domain, before '?' or '#').
   b. If the path contains an underscore '_' character, record as violation.
3. If any violations recorded, result = fail else pass.

## Pass condition
URL paths do not contain underscore characters.

## Failure messages
- URL path contains underscore: ${observed}

## Examples
### Passing
URL uses hyphens between words.
```html
<a href="https://example.com/summer-clothing/filter?color-profile=dark-grey">Link</a>
```

### Failing
URL uses underscores between words.
```html
<a href="https://example.com/summer_clothing/filter?color_profile=dark_grey">Link</a>
```

### test case passing
```html
<html><body><a href="https://example.com/summer-clothing"></a></body></html>
```

### test case failing
```html
<html><body><a href="https://example.com/summer_clothing"></a></body></html>
```

### References
Reference: [URL structure best practices for Google Search](https://developers.google.com/search/docs/advanced/crawling/url-structure)