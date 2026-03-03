---
title: Verify Search Console verification assets are present on the new site
impact: MEDIUM
impactDescription: Ownership verification must continue to work after the hosting move
tags: verification, search_console
inputFields:
  - name: html
    required: true
    description: HTML content of the homepage or verification page.
---

## Verify Search Console verification assets are present on the new site
Ownership verification must continue to work after the hosting move.

## Evidence to collect
- Selector: meta[name="google-site-verification"] (Verification token should be non‑empty.)

## Logic (pseudocode)
Input: html
1. Search html for &lt;meta name="google-site-verification" content="..."&gt;.
2. If such a tag exists and content is not empty, set pass.
3. Otherwise, set fail.

## Pass condition
Presence of a non‑empty google-site-verification meta tag.

## Failure messages
- Search Console verification meta tag missing or empty.

## Examples
### Passing
Verification meta tag present.
```html
<meta name="google-site-verification" content="abc123">
```

### Failing
Verification meta tag absent.
```html
<!-- No verification tag -->
```

### test case passing
```html
<html><head><meta name="google-site-verification" content="abc123"></head></html>
```

### test case failing
```html
<html><head></head></html>
```

### References
Reference: [Changing Your Web Hosting and SEO](https://developers.google.com/search/docs/hosting/migrate)