---
title: Ensure login pages include a noindex robots meta tag
impact: HIGH
impactDescription: Prevents search engines from indexing login pages that may expose redacted content
tags: redaction, robots_meta
inputFields:
  - name: html
    required: true
    description: Full HTML source of the page to be evaluated
---

## Ensure login pages include a noindex robots meta tag
Login pages may expose redacted content; a noindex meta tag prevents search engines from indexing them.

## Evidence to collect
- Selector: form input[type='password'] (Detects login form)
- Selector: meta[name='robots'] (Meta tag that may contain 'noindex')

## Logic (pseudocode)
Inputs: html
1. Parse html into DOM.
2. If DOM contains element matching selector "form input[type='password']":
   a. Search for meta element matching selector "meta[name='robots']".
   b. If meta found and its content attribute includes the token "noindex" (case-insensitive):
        result = pass
      else:
        result = fail
3. If no password input found, result = not_applicable

## Pass condition
Login pages contain a robots meta tag whose content includes "noindex".

## Failure messages
- Login page missing noindex meta tag; observed content: ${observed_meta_content}

## Examples
### Passing
Page with a password field and a meta robots tag containing "noindex"
```html
<html><head><meta name="robots" content="noindex, nofollow"></head><body><form><input type="password"></form></body></html>
```

### Failing
Page with a password field but no noindex meta tag
```html
<html><head></head><body><form><input type="password"></form></body></html>
```

### test case passing
```html
<html><head><meta name="robots" content="noindex"></head><body><form><input type="password"></form></body></html>
```

### test case failing
```html
<html><head></head><body><form><input type="password"></form></body></html>
```

### References
Reference: [Keep redacted information out of Google Search](https://developers.google.com/search/docs/keep-redacted-info)