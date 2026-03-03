# Favicon Dimensions Checker

This script verifies that favicon is square and at least 8x8 pixels.

## Usage

```bash
python3 favicon_dimensions.py <html_file>
```

## Arguments

- `html_file`: Path to HTML file to analyze for favicon

## Dependencies

```bash
pip install pillow requests beautifulsoup4 lxml
```

## Output

JSON result with:
- `passed`: Boolean indicating if favicon meets requirements
- `width`: Width of favicon in pixels
- `height`: Height of favicon in pixels
- `is_square`: Boolean indicating if width equals height
- `min_size_met`: Boolean indicating if dimensions are at least 8x8
- `favicon_url`: URL of the favicon analyzed
- `message`: Human-readable summary

## Example

```bash
python3 favicon_dimensions.py index.html
```

Returns:
```json
{
  "rule_id": "FAVICON_DIMENSIONS",
  "passed": true,
  "width": 48,
  "height": 48,
  "is_square": true,
  "min_size_met": true,
  "favicon_url": "https://example.com/favicon.ico",
  "message": "Favicon dimensions: 48x48px"
}
```

## Notes

- Script automatically downloads the favicon from the extracted URL
- Supports various favicon link formats (rel="icon", apple-touch-icon, etc.)
- Falls back to /favicon.ico if no favicon link is found
- Temporarily saves downloaded favicon for analysis