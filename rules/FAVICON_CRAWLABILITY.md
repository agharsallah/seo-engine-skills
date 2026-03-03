---
title: Ensure favicon and home page are crawlable by Googlebot
impact: HIGH
impactDescription: Googlebot-Image and Googlebot must be able to crawl the favicon file and the home page; blocking them prevents the favicon from appearing in search results.
tags: favicon, crawlability, seo
inputFields:
  - name: html
    required: true
    description: HTML of the site's home page to locate the favicon <link> element.
  - name: http_headers
    required: true
    description: HTTP response headers for the home page and favicon URL.
  - name: robots_txt
    required: true
    description: Contents of the site's robots.txt file.
---

## Ensure favicon and home page are crawlable by Googlebot
Googlebot-Image and Googlebot must be able to crawl the favicon file and the home page; blocking them prevents the favicon from appearing in search results.

## Evidence to collect
- Extracted favicon URL: `link[rel~='icon'], link[rel='apple-touch-icon'], link[rel='apple-touch-icon-precomposed']`
- Status code for the home page request
- Status code for the favicon request
- Disallow rules that block the favicon path or home page

## Logic (pseudocode)
1. Parse html to find favicon_href using the selector above.
2. Perform HTTP GET on home page URL; record status_home.
3. Perform HTTP GET on favicon_href; record status_favicon.
4. Load robots_txt and verify no Disallow rule matches home page path or favicon_href.
5. If status_home == 200 AND status_favicon == 200 AND not blocked by robots_txt => pass.
   Else => fail.

## Pass condition
Both the home page and the favicon URL return HTTP 200 and are not blocked by robots.txt.

## Failure messages
- Home page returned ${status_home} instead of 200.
- Favicon URL returned ${status_favicon} instead of 200.
- Robots.txt blocks crawling of ${blocked_path}.

## Examples
### Passing
Home page and favicon both return 200 and are not disallowed.
```html
<link rel="icon" href="/favicon.ico">
<!-- HTTP/1.1 200 OK (home page) -->
<!-- HTTP/1.1 200 OK (GET /favicon.ico) -->
<!-- robots.txt does not contain Disallow for /favicon.ico -->
```

### Failing
Favicon is blocked by robots.txt.
```html
<link rel="icon" href="/private/favicon.ico">
<!-- robots.txt contains "Disallow: /private/" -->
```

### test case passing
```html
<html><head><link rel='icon' href='/favicon.ico'></head></html>
<!-- Home page: 200, Favicon: 200, robots.txt: Allow: / -->
```

### test case failing
```html
<html><head><link rel='icon' href='/secret/favicon.ico'></head></html>
<!-- robots.txt: Disallow: /secret/ -->
```

### References
Reference: [Define Website Favicon for Search Results](https://developers.google.com/search/docs/appearance/favicon)