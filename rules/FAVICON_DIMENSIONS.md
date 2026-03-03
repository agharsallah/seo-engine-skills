---
title: Verify favicon is square and at least 8x8 pixels
impact: MEDIUM
impactDescription: Google requires the favicon to be a square image with a minimum size of 8x8 px to be eligible for display in search results.
tags: favicon, dimensions, seo
inputFields:
  - name: html
    required: true
    description: HTML of the home page to locate the favicon link.
  - name: favicon_image
    required: true
    description: Binary image data of the favicon referenced by the link.
---

## Verify favicon is square and at least 8x8 pixels
Google requires the favicon to be a square image with a minimum size of 8x8 px to be eligible for display in search results.

## Evidence to collect
- Favicon URL: `link[rel~='icon'], link[rel='apple-touch-icon'], link[rel='apple-touch-icon-precomposed']`
- Width of the fetched favicon image in pixels
- Height of the fetched favicon image in pixels

## Logic (pseudocode)
1. Extract favicon_href from html using the selector.
2. Fetch the image at favicon_href and obtain width and height.
3. If width == height AND width >= 8 THEN pass ELSE fail.

## Pass condition
The favicon image is square (width equals height) and its width (and height) is at least 8 px.

## Failure messages
Favicon dimensions are ${width}x${height}px; must be square and at least 8x8px.

## Examples
### Passing
48x48 square PNG favicon.
```html
<link rel="icon" href="/favicon.png">
<!-- Image size: 48px × 48px -->
```

### Failing
16x32 rectangular favicon.
```html
<link rel="icon" href="/favicon.ico">
<!-- Image size: 16px × 32px -->
```

### test case passing
```html
<link rel='icon' href='/favicon.png'>
<!-- Width: 48, Height: 48 -->
```

### test case failing
```html
<link rel='icon' href='/favicon.ico'>
<!-- Width: 16, Height: 32 -->
```

### References
Reference: [Define Website Favicon for Search Results](https://developers.google.com/search/docs/appearance/favicon)