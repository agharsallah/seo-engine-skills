---
title: Ensure exported images are in non-vector formats (PNG or WEBP)
impact: MEDIUM
impactDescription: Vector formats may retain hidden layers or metadata that can be indexed
tags: redaction, image_format
inputFields:
  - name: html
    required: true
    description: HTML source containing img elements
---

## Ensure exported images are in non-vector formats (PNG or WEBP)
Vector formats may retain hidden layers or metadata that can be indexed.

## Evidence to collect
- Selector: img (Collect source URLs of all images on the page)

## Logic (pseudocode)
Inputs: html
1. Parse html and extract all img elements' src attributes.
2. For each src, extract file extension (substring after last '.').
3. If any extension is not in the allowed set {"png","webp"} (case-insensitive):
      result = fail
   else:
      result = pass

## Pass condition
All image src URLs end with .png or .webp (case-insensitive).

## Failure messages
- Image with disallowed format found; observed src: ${observed}

## Examples
### Passing
Page with only PNG and WEBP images
```html
<html><body><img src="photo.png"><img src="icon.webp"></body></html>
```

### Failing
Page with a JPEG image
```html
<html><body><img src="photo.jpg"></body></html>
```

### test case passing
```html
<html><body><img src="photo.png"><img src="icon.webp"></body></html>
```

### test case failing
```html
<html><body><img src="photo.jpg"></body></html>
```

### References
Reference: [Keep redacted information out of Google Search](https://developers.google.com/search/docs/keep-redacted-info)