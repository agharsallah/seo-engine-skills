# Hidden Text Detection Script

This script detects text or links that are visually hidden but present in HTML, which is a common SEO manipulation technique used to deceive search engines.

## Features

- **Browser-based Analysis**: Uses Selenium with headless Chrome for accurate rendering and computed style analysis
- **Static HTML Analysis**: Fallback mode for analyzing HTML content without browser rendering
- **Comprehensive Detection**: Identifies 7+ hiding techniques including CSS properties, positioning, and color matching
- **Smart Filtering**: Only flags elements with meaningful content (>2 words or links) to avoid false positives
- **Detailed Reporting**: Provides evidence with hiding methods and element selectors

## Installation

```bash
pip install -r requirements.txt
```

**Note**: This script requires Chrome/Chromium browser to be installed for Selenium WebDriver functionality.

### Installing Chrome on Linux
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install google-chrome-stable

# Or install chromium
sudo apt-get install chromium-browser
```

## Usage

### Analyze a URL (Recommended)
```bash
python hidden_text_detection.py --url "https://example.com"
```

### Analyze HTML Content (String)
```bash
python hidden_text_detection.py --html "<div style='display:none'>Hidden text</div>"
```

### Analyze a Local HTML File
```bash
python hidden_text_detection.py --html-file path/to/file.html
```

### Save Results to File
```bash
python hidden_text_detection.py --url "https://example.com" --output results.json
```

## Detection Methods

The script identifies text hidden using various techniques:

1. **CSS Display Properties**
   - `display: none`
   - `visibility: hidden`
   - `opacity: 0`

2. **Dimensional Hiding**
   - Zero width or height (`width: 0`, `height: 0`)
   - Zero font size (`font-size: 0`)

3. **Positioning Tricks**
   - Off-screen positioning (negative coordinates)
   - Negative text-indent values

4. **Color Matching**
   - Text color same as background color

5. **Browser Rendering Check**
   - Selenium's `is_displayed()` method validation

## Output Format

The script outputs JSON with the following structure:

```json
{
  "status": "success",
  "url": "https://example.com",
  "passed": false,
  "hidden_elements_count": 2,
  "hidden_elements": [
    {
      "tag": "div",
      "id": "hidden-content",
      "class": "seo-text",
      "text_content": "Hidden SEO keywords here...",
      "text_length": 125,
      "has_links": true,
      "link_count": 3,
      "hiding_method": "display: none",
      "selector": "div#hidden-content.seo-text"
    }
  ],
  "evidence": {
    "total_hidden_elements": 2,
    "elements_with_text": 2,
    "elements_with_links": 1
  },
  "message": "Hidden text detected in 2 element(s). Primary violation: display: none on div#hidden-content.seo-text"
}
```

## Exit Codes

- `0`: Test passed (no hidden text detected)
- `1`: Test failed (hidden text detected)
- `1`: Error occurred during analysis

## Common Use Cases

- **SEO Auditing**: Detect black-hat SEO techniques on websites
- **Compliance Checking**: Ensure content transparency for search engines
- **Security Analysis**: Identify potential cloaking or deceptive practices
- **Web Accessibility**: Find content that may be improperly hidden from users

## Technical Notes

- Uses headless Chrome for accurate CSS rendering
- Analyzes computed styles, not just inline CSS
- Handles dynamic JavaScript content
- Provides fallback static analysis for HTML-only inputs
- Considers accessibility content and avoids false positives for legitimate UI elements

## Limitations

- Requires Chrome/Chromium browser for URL analysis mode
- May not detect advanced JavaScript-based hiding techniques
- Static HTML analysis mode has limited CSS detection capabilities
- Performance depends on page load time and complexity