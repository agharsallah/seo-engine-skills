---
title: Ensure page is not disallowed by robots.txt
impact: HIGH
impactDescription: Pages disallowed by robots.txt cannot be crawled, which prevents Google from discovering and indexing them.
tags: crawling, robots_txt
inputFields:
  - name: robots_txt
    required: true
    description: Content of the site's robots.txt file
  - name: url
    required: true
    description: Full URL of the page being evaluated
---

## Ensure page is not disallowed by robots.txt
Pages disallowed by robots.txt cannot be crawled, which prevents Google from discovering and indexing them.

## Evidence to collect
- Disallow rules for User-agent * or Googlebot compared against the page path

## Logic (pseudocode)
Inputs: robots_txt (string), url (string)
1. Parse the URL to obtain its path component.
2. Extract all Disallow directives applicable to User-agent * or Googlebot from robots_txt.
3. For each Disallow rule, treat it as a path prefix.
4. If the page path starts with any Disallow prefix, set disallowed = true.
5. Otherwise, disallowed = false.

## Pass condition
No Disallow rule in robots.txt matches the page URL path.

## Failure messages
Page URL ${url} is disallowed by robots.txt.

## Examples
### Passing
Page URL not matched by any Disallow rule.
```
robots_txt:
  User-agent: *
  Disallow: /private/
url: https://example.com/public/page.html
```

### Failing
Page URL matches a Disallow rule.
```
robots_txt:
  User-agent: *
  Disallow: /private/
url: https://example.com/private/secret.html
```

### test case passing
```
User-agent: *
Disallow: /admin/
URL: https://example.com/blog/post.html
```

### test case failing
```
User-agent: *
Disallow: /blog/
URL: https://example.com/blog/post.html
```

### References
Reference: [In-depth guide to how Google Search works](https://developers.google.com/search/docs/crawling-indexing/overview)