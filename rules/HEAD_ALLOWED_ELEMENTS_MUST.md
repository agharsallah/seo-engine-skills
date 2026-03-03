---
title: Only allowed elements in <head>
impact: HIGH
impactDescription: Google processes only the allowed elements in the <head>; any invalid element causes the rest of the metadata to be ignored
tags: metadata, head, validation
inputFields:
  - name: html
    required: true
    description: HTML content of the page
---

## Only allowed elements in &lt;head&gt;
Google processes only the allowed elements in the &lt;head&gt;; any invalid element causes the rest of the metadata to be ignored.

## Evidence to collect
- Selector: head > * (Collect tag names of all direct children of &lt;head&gt;)

## Logic (pseudocode)
Inputs: html
1. Parse html and locate the &lt;head&gt; element.
2. For each direct child element of &lt;head&gt; in document order:
   a. Get the tag name.
   b. If tag name not in ALLOWED = {title, meta, link, script, style, base, noscript, template}:
        record as invalid and fail.
3. If no invalid tags found, pass.

## Pass condition
All direct child elements of &lt;head&gt; are in the allowed set {title, meta, link, script, style, base, noscript, template}.

## Failure messages
- Invalid element &lt;${observed}&gt; found in &lt;head&gt;; only allowed elements are title, meta, link, script, style, base, noscript, template.

## Examples
### Passing
Head contains only allowed elements.
```html
<head>
  <title>Example</title>
  <meta name="description" content="...">
  <link rel="canonical" href="https://example.com/">
</head>
```

### Failing
Head contains an invalid element.
```html
<head>
  <title>Example</title>
  <iframe src="..."></iframe>
  <meta name="description" content="...">
</head>
```

### test case passing
```html
<html><head><title>Test</title><meta charset='utf-8'></head></html>
```

### test case failing
```html
<html><head><title>Test</title><iframe src=''></iframe></head></html>
```

### References
Reference: [Valid Page Metadata for Google Search](https://developers.google.com/search/docs/appearance/metadata)