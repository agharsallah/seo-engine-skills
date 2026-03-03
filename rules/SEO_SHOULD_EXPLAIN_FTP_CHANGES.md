---
title: SEO with FTP access must explain changes
impact: LOW
impactDescription: Transparency about changes made via FTP ensures the site owner can verify compliance and avoid hidden manipulations.
tags: transparency, ftp
inputFields:
  - name: ftp_access_granted
    required: true
    description: Boolean indicating whether the SEO has FTP access to the site.
  - name: change_explanations_provided
    required: true
    description: Boolean indicating whether the SEO has provided explanations for all changes made via FTP.
---

## SEO with FTP access must explain changes
Transparency about changes made via FTP ensures the site owner can verify compliance and avoid hidden manipulations.

## Evidence to collect
- FTP access status and explanation status (manual verification required)

## Logic (pseudocode)
Inputs: ftp_access_granted, change_explanations_provided
1. If ftp_access_granted is false, the check is not applicable.
2. If ftp_access_granted is true, verify change_explanations_provided is true.
3. Pass if explanations are provided; otherwise fail.

## Pass condition
When FTP access is granted, the SEO provides explanations for all changes.

## Failure messages
FTP access granted without explanations for changes.

## Examples
### Passing
FTP access granted and explanations provided.
```
ftp_access_granted: true
change_explanations_provided: true
```

### Failing
FTP access granted but no explanations.
```
ftp_access_granted: true
change_explanations_provided: false
```

### test case passing
```
FTP Access: Yes
Explanations Provided: Yes
```

### test case failing
```
FTP Access: Yes
Explanations Provided: No
```

### References
Reference: [Helpful guidelines](https://developers.google.com/search/docs/seo/choose-an-seo)