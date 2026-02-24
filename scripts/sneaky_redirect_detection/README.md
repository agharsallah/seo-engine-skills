# Sneaky Redirect Detection Script

This script detects sneaky redirects that serve different content or destinations to users versus search engine crawlers (Googlebot). This is a deceptive practice used to manipulate search rankings and can result in penalties from search engines.

## Features

- **Dual User Agent Testing**: Tests URLs with both regular browser and Googlebot user agents
- **Complete Redirect Chain Analysis**: Tracks and compares entire redirect sequences
- **Manual Data Analysis**: Supports analysis of pre-collected redirect data  
- **Detailed Difference Detection**: Identifies discrepancies in URLs, status codes, and redirect patterns
- **Comprehensive Reporting**: Provides detailed analysis with severity levels
- **Retry Logic**: Handles temporary network issues with intelligent retry strategies

## Installation

```bash
pip install -r requirements.txt
```

**Note**: This script only requires the `requests` library and does not need browser dependencies like Chrome/Chromium.

## Usage

### Analyze a URL (Recommended)
```bash
python sneaky_redirect_detection.py --url "https://example.com/page"
```

### Manual Analysis (Pre-collected Data)
```bash
python sneaky_redirect_detection.py \
  --final-url-googlebot "https://example.com/seo-page" \
  --final-url-user "https://example.com/user-page" \
  --http-status-googlebot 200 \
  --http-status-user 200
```

### Custom Configuration
```bash
python sneaky_redirect_detection.py --url "https://example.com" --max-redirects 5 --timeout 15
```

### Save Results to File
```bash
python sneaky_redirect_detection.py --url "https://example.com" --output results.json
```

## Detection Logic

The script analyzes redirect behavior using the following process:

1. **Dual Request Testing**: Makes identical requests with different user agents:
   - Regular Browser: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...`
   - Googlebot: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`

2. **Redirect Chain Tracking**: Follows up to 10 redirects (configurable) for each user agent:
   - Records each step: URL, status code, headers, redirect type
   - Handles relative and absolute redirects correctly
   - Tracks timing and content information

3. **Difference Analysis**: Compares results between user agents:
   - Final destination URLs
   - Final HTTP status codes  
   - Number of redirects in chain
   - Individual redirect steps and patterns

4. **Severity Assessment**: Categorizes differences by impact:
   - **HIGH**: Different final URLs or status codes (definitive sneaky redirect)
   - **MEDIUM**: Different redirect counts or intermediate steps
   - **LOW**: Minor timing or header differences

## Output Format

The script outputs JSON with comprehensive analysis:

```json
{
  "status": "success",
  "url": "https://example.com",
  "passed": false,
  "sneaky_redirects_detected": true,
  "differences_count": 2,
  "high_severity_count": 1,
  "differences": [
    {
      "type": "final_url_mismatch",
      "description": "Final URLs differ between user agents", 
      "regular_value": "https://example.com/user-page",
      "googlebot_value": "https://example.com/seo-page",
      "severity": "HIGH"
    }
  ],
  "regular_user_result": {
    "final_url": "https://example.com/user-page",
    "final_status_code": 200,
    "redirect_count": 2,
    "redirect_chain": [...],
    "success": true
  },
  "googlebot_result": {
    "final_url": "https://example.com/seo-page", 
    "final_status_code": 200,
    "redirect_count": 1,
    "redirect_chain": [...],
    "success": true
  },
  "analysis": {
    "same_final_url": false,
    "same_final_status": true,
    "same_redirect_count": false
  },
  "message": "Sneaky redirect detected: Final URLs differ between user agents - Regular: https://example.com/user-page, Googlebot: https://example.com/seo-page"
}
```

## Command Line Options

### URL Analysis Mode
- `--url`: URL to analyze for sneaky redirects
- `--max-redirects`: Maximum redirects to follow (default: 10)
- `--timeout`: Request timeout in seconds (default: 30)

### Manual Analysis Mode  
- `--final-url-googlebot`: Final URL after redirect for Googlebot
- `--final-url-user`: Final URL after redirect for regular user
- `--http-status-googlebot`: HTTP status code for Googlebot
- `--http-status-user`: HTTP status code for user

### Output Options
- `--output`: Output file for results (default: sneaky_redirect_results.json)

## Exit Codes

- `0`: Test passed (no sneaky redirects detected)
- `1`: Test failed (sneaky redirects detected) or error occurred

## Common Use Cases

- **SEO Auditing**: Check if sites use different redirect behavior for search engines
- **Competitor Analysis**: Analyze competitor redirect strategies for compliance
- **Security Assessment**: Identify potential cloaking or deceptive redirect practices
- **Compliance Monitoring**: Ensure redirect practices comply with search engine guidelines
- **Penalty Investigation**: Diagnose potential causes of search engine penalties

## Detection Examples

### Passing (No Sneaky Redirects)
**Scenario**: Both user agents receive identical treatment
- Regular User: `example.com` → `example.com/new-page` (301)
- Googlebot: `example.com` → `example.com/new-page` (301)

**Result**: ✅ Pass - Identical redirect behavior

### Failing (Sneaky Redirects Detected)  

**Scenario 1**: Different Final Destinations
- Regular User: `example.com` → `example.com/products` (302)  
- Googlebot: `example.com` → `example.com/seo-keywords` (302)

**Result**: ❌ Fail - Different final URLs (HIGH severity)

**Scenario 2**: Different Status Codes
- Regular User: `example.com` → `404 Not Found`
- Googlebot: `example.com` → `example.com/content` (200)

**Result**: ❌ Fail - Different status codes (HIGH severity)

**Scenario 3**: Different Redirect Chains  
- Regular User: `example.com` → `www.example.com` → `www.example.com/page` (2 redirects)
- Googlebot: `example.com` → `www.example.com/page` (1 redirect)

**Result**: ❌ Fail - Different redirect patterns (MEDIUM severity)

## Technical Notes

- **Request Headers**: Uses realistic browser and Googlebot User-Agent strings
- **Redirect Handling**: Properly handles all HTTP redirect codes (301, 302, 303, 307, 308)
- **Relative URL Resolution**: Correctly resolves relative redirects to absolute URLs
- **Error Handling**: Graceful handling of network issues, timeouts, and malformed responses
- **Rate Limiting**: Includes delays between requests to be respectful to servers
- **Retry Logic**: Automatic retry for transient network failures

## Limitations

- **JavaScript Redirects**: Cannot detect client-side JavaScript redirects
- **Timing-Based Redirects**: May miss redirects that depend on precise timing
- **IP-Based Detection**: Sites using IP-based user agent verification may behave differently
- **Rate Limiting**: Some sites may block or throttle automated requests
- **Complex Cloaking**: Advanced cloaking techniques may require more sophisticated detection

## Security Considerations

- **Respectful Testing**: Includes appropriate delays and follows robots.txt guidelines  
- **User Agent Honesty**: Uses legitimate, recognizable user agent strings
- **Request Volume**: Limits requests to avoid overwhelming target servers
- **Error Reporting**: Provides detailed error information for troubleshooting

## Best Practices

- **Regular Monitoring**: Include in automated SEO compliance checking
- **Documentation**: Keep records of redirect analysis for compliance audits
- **Multiple Testing**: Test different entry points and URL patterns
- **Manual Verification**: Confirm automated findings with manual browser testing
- **Compliance**: Ensure your own redirects pass testing before deployment

## Troubleshooting

### Common Issues
- **Timeout Errors**: Increase `--timeout` value for slow-loading sites
- **Too Many Redirects**: Increase `--max-redirects` or investigate redirect loops
- **Network Issues**: Check internet connectivity and DNS resolution
- **Blocked Requests**: Site may be blocking automated requests or specific user agents

### Getting Help
- Check the JSON output for detailed error messages
- Review redirect chains to understand the flow
- Test manually in browsers to verify automated findings
- Consider rate limiting if receiving 429 status codes