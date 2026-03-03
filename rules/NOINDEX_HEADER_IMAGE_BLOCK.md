---
title: Block image URLs via noindex X-Robots-Tag header
impact: HIGH
impactDescription: X-Robots-Tag header tells Googlebot not to index the image, but the URL must be crawlable for the header to be read
tags: noindex, X-Robots-Tag, image removal
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers of the image URL
  - name: robots_txt
    required: true
    description: Content of the site's robots.txt file
---

## Block image URLs via noindex X-Robots-Tag header
The noindex X-Robots-Tag header tells Googlebot not to index the image, but the URL must be crawlable for the header to be read.

## Evidence to collect
- Header: X-Robots-Tag (Header value should contain 'noindex')
- Regex: User-agent:\\s*Googlebot-Image[\\s\\S]*?Disallow:\\s*(.+) (Check if image path is disallowed)

## Logic (pseudocode)
Inputs: http_headers (dict), robots_txt (string), image_path (string)
1. Verify that http_headers contains "X-Robots-Tag".
2. Verify that the value of "X-Robots-Tag" includes the token "noindex" (case-insensitive).
3. Parse robots_txt for Disallow rules under User-agent Googlebot-Image (or Googlebot).
4. If any Disallow rule matches image_path, then crawling is blocked → FAIL (must allow crawling).
5. If step 2 passes and step 4 passes (i.e., not blocked), then PASS.
6. Otherwise, FAIL.

## Pass condition
Image response includes X-Robots-Tag header with 'noindex' and the image URL is not blocked by robots.txt.

## Failure messages
- Missing X-Robots-Tag header with 'noindex' for image ${image_url}.
- Image URL ${image_url} is blocked by robots.txt, preventing Googlebot from reading the X-Robots-Tag header.

## Examples
### Passing
Image response includes X-Robots-Tag: noindex and robots.txt does not disallow the image.
```
HTTP/1.1 200 OK
X-Robots-Tag: noindex
```

### Failing
Image response missing X-Robots-Tag header.
```
HTTP/1.1 200 OK
(no X-Robots-Tag)
```

### test case passing
```json
{
  "http_headers": {
    "X-Robots-Tag": "noindex"
  },
  "robots_txt": "User-agent: *\nDisallow: /private/\n"
}
```

### test case failing
```json
{
  "http_headers": {},
  "robots_txt": "User-agent: *\nDisallow: /private/\n"
}
```

### References
Reference: [Remove images with the `noindex` `X-Robots-Tag` HTTP header](https://developers.google.com/search/robots-meta-tag.html#xrobotstag-implementation)