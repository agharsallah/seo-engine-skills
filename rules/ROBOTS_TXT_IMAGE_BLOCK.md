---
title: Block image URLs via robots.txt Disallow rule
impact: LOW
impactDescription: Robots.txt Disallow rules prevent Googlebot-Image from indexing specified image URLs
tags: robots.txt, image removal
inputFields:
  - name: robots_txt
    required: true
    description: Content of the site's robots.txt file
---

## Block image URLs via robots.txt Disallow rule
Robots.txt Disallow rules prevent Googlebot-Image from indexing specified image URLs, removing them from search results.

## Evidence to collect
- Regex: User-agent:\\s*Googlebot-Image[\\s\\S]*?Disallow:\\s*(.+) (Capture Disallow paths for Googlebot-Image)

## Logic (pseudocode)
Input: robots_txt (string), target_image_path (string)
1. Find the block of lines starting with "User-agent: Googlebot-Image".
2. Within that block, extract all Disallow paths.
3. If any Disallow path matches target_image_path exactly or matches a pattern that would include it (e.g., wildcard *), then PASS.
4. Else FAIL.

## Pass condition
robots.txt contains a Disallow rule that matches the image URL under User-agent Googlebot-Image (or Googlebot).

## Failure messages
- No matching Disallow rule found for image URL ${image_url} in robots.txt.

## Examples
### Passing
robots.txt includes Disallow for /images/dogs.jpg under Googlebot-Image.
```
User-agent: Googlebot-Image
Disallow: /images/dogs.jpg
```

### Failing
robots.txt does not contain a Disallow rule for the image.
```
User-agent: *
Disallow: /private/
```

### test case passing
```
User-agent: Googlebot-Image
Disallow: /images/dogs.jpg
```

### test case failing
```
User-agent: *
Disallow: /private/
```

### References
Reference: [Remove images using robots.txt rules](https://developers.google.com/search/robots/intro.html)