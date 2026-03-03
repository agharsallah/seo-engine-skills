---
title: Web Story must have self-referential canonical link
impact: HIGH
impactDescription: A self‑referential canonical link tells Google the definitive URL for the story, enabling correct indexing and avoiding duplicate content issues.
tags: canonical, indexing
inputFields:
  - name: html
    required: true
    description: HTML content of the Web Story page
  - name: url
    required: true
    description: The URL at which the Web Story is served
---

## Web Story must have self-referential canonical link
A self‑referential canonical link tells Google the definitive URL for the story, enabling correct indexing and avoiding duplicate content issues.

## Evidence to collect
- Canonical URL declared in the page: `link[rel='canonical']`

## Logic (pseudocode)
Inputs: html, url
1. Parse the HTML document.
2. Locate the first <link> element with rel="canonical".
3. If no such element exists, set observed = null and FAIL.
4. Extract the href attribute as observed_canonical.
5. Compare observed_canonical to the supplied url.
6. If they are identical (case‑sensitive), PASS; else FAIL.

## Pass condition
The page contains a <link rel="canonical"> whose href exactly matches the page URL.

## Failure messages
Canonical link missing or href (${observed}) does not match the page URL (${expected}).

## Examples
### Passing
Page includes correct self‑referential canonical link.
```html
<link rel="canonical" href="https://example.com/story.html">
```

### Failing
Canonical link points to a different URL or is missing.
```html
<!-- Missing canonical or wrong href -->
<link rel="canonical" href="https://example.com/other.html">
```

### test case passing
```html
<html><head><link rel='canonical' href='https://example.com/story.html'></head></html>
<!-- URL: https://example.com/story.html -->
```

### test case failing
```html
<html><head><link rel='canonical' href='https://example.com/other.html'></head></html>
<!-- URL: https://example.com/story.html -->
```

### References
Reference: [Enable Web Stories on Google](https://developers.google.com/search/docs/guides/web-stories)