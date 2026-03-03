---
title: Ensure HTTP redirect headers are sent before any body content in PHP redirects
impact: HIGH
impactDescription: Redirect responses must have an empty body (0 bytes) after sending headers
tags: php, redirect, headers, seo
inputFields:
  - name: http_headers
    required: true
    description: HTTP response headers returned by the URL
  - name: response_body
    required: true
    description: Raw response body content returned by the URL
---

## Ensure HTTP redirect headers are sent before any body content in PHP redirects
The documentation states "You must set the headers before sending anything to the screen" for PHP redirects, requiring headers to precede any output.

## Evidence to collect
- Header value: Status (Redirect status code)
- Header value: Location (Redirect target URL)
- Metric: body_length (Length of response body in bytes)

## Logic (pseudocode)
Inputs: http_headers, response_body
1. Extract status_code from http_headers["Status"]
2. If status_code not in [301,302,303,307,308], skip (not applicable)
3. Compute body_length = length_in_bytes(response_body)
4. If body_length == 0, PASS
5. Else, FAIL

## Pass condition
Redirect responses must have an empty body (0 bytes) after sending headers.

## Failure messages
- Redirect response contains body content (${observed} bytes), violating the requirement to set headers before output.

## Examples
### Passing
PHP redirect with headers set before any output.
```php
<?php
header('HTTP/1.1 301 Moved Permanently');
header('Location: https://www.example.com/newurl');
exit();
?>
```

### Failing
PHP redirect where output is sent before headers.
```php
<?php
echo "Redirecting...";
header('HTTP/1.1 301 Moved Permanently');
header('Location: https://www.example.com/newurl');
exit();
?>
```

### test case passing
```json
{
  "http_headers": {
    "Status": "301 Moved Permanently",
    "Location": "https://www.example.com/newurl"
  },
  "response_body": ""
}
```

### test case failing
```json
{
  "http_headers": {
    "Status": "301 Moved Permanently",
    "Location": "https://www.example.com/newurl"
  },
  "response_body": "Redirecting..."
}
```

### References
Reference: [Redirects and Google Search](https://developers.google.com/search/docs/redirects)