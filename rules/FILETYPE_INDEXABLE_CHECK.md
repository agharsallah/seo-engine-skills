---
title: File extension is indexable by Google
impact: LOW
impactDescription: Google can index specific text‑based and media file types; other extensions may not be indexed
tags: indexability, filetype
inputFields:
  - name: url
    required: true
    description: Full URL of the resource to evaluate
---

## File extension is indexable by Google
Google can index the content of the listed text‑based and media file types; resources with other extensions may not be indexed.

## Evidence to collect
- Regex: url (Extract the file extension from the URL path)

## Logic (pseudocode)
Inputs: url
1. Parse the URL and isolate the path component.
2. Extract the substring after the last '.' in the path as the extension (lowercase, without leading dot).
3. Define ALLOWED_EXTENSIONS as the set: ["pdf","ps","csv","epub","kml","kmz","gpx","hwp","htm","html","xls","xlsx","ppt","pptx","doc","docx","odp","ods","odt","rtf","svg","tex","txt","text","bas","c","cc","cpp","cxx","h","hpp","cs","java","pl","py","wml","wap","xml","bmp","gif","jpeg","png","webp","avif","3gp","3g2","asf","avi","divx","m2v","m3u","m3u8","m4v","mkv","mov","mp4","mpeg","ogv","qvt","ram","rm","vob","webm","wmv","xap"]
4. If the extracted extension is in ALLOWED_EXTENSIONS, result = PASS else result = FAIL.

## Pass condition
The extracted file extension is present in the list of indexable extensions.

## Failure messages
- File extension '${observed}' is not among Google-indexable types.

## Examples
### Passing
URL ending with an indexable extension
```
https://example.com/report.pdf
```

### Failing
URL ending with a non‑indexable extension
```
https://example.com/script.exe
```

### test case passing
```
https://example.com/document.docx
```

### test case failing
```
https://example.com/installer.exe
```

### References
Reference: [File types indexable by Google](https://developers.google.com/search/docs/advanced/crawling/file-types-indexable)