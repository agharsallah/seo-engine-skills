---
title: Ensure resources are not blocked by robots.txt
impact: HIGH
impactDescription: Resources such as images, CSS, and JavaScript must be accessible to Google; if they are blocked by robots.txt Google cannot crawl the page properly.
tags: crawling, indexing, robots.txt
inputFields:
  - name: html
    required: true
    description: HTML content of the page to extract resource URLs.
  - name: robots_txt
    required: true
    description: Full contents of the site's robots.txt file.
---

## Ensure resources are not blocked by robots.txt
Resources such as images, CSS, and JavaScript must be accessible to Google; if they are blocked by robots.txt Google cannot crawl the page properly.

## Evidence to collect
- URLs of resources referenced in the page: `img[src], link[rel=stylesheet][href], script[src]`

## Logic (pseudocode)
Input: html, robots_txt
1. Parse html and extract all URLs from img[src], link[rel=stylesheet][href], script[src].
2. Parse robots_txt into a list of Disallow path patterns.
3. For each extracted URL:
   a. Convert URL to path relative to site root.
   b. If any Disallow pattern matches the path, record as blocked.
4. If any resource URL is recorded as blocked, the check fails.

## Pass condition
All extracted resource URLs are allowed by robots.txt.

## Failure messages
Resource URL ${url} is blocked by robots.txt.

## Examples
### Passing
Page references images and CSS files that are not disallowed in robots.txt.
```html
<html>
  <head>
    <link rel="stylesheet" href="/styles/main.css">
  </head>
  <body>
    <img src="/images/logo.png">
  </body>
</html>
# robots.txt
User-agent: *
Disallow: /private/
```

### Failing
Page references a script that is disallowed by robots.txt.
```html
<html>
  <head>
    <script src="/js/analytics.js"></script>
  </head>
</html>
# robots.txt
User-agent: *
Disallow: /js/
```

### test case passing
```html
<img src="/images/a.png"><link rel="stylesheet" href="/css/b.css">
<!-- robots.txt: User-agent: *\nDisallow: /private/ -->
```

### test case failing
```html
<script src="/js/blocked.js"></script>
<!-- robots.txt: User-agent: *\nDisallow: /js/ -->
```

### References
Reference: [Technical SEO Techniques and Strategies](https://developers.google.com/search/docs/technical-seo)