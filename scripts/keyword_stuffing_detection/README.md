# Keyword Stuffing Detection Script

This script detects excessive repetition of keywords indicative of keyword stuffing, which is a common SEO spam technique that reduces content quality and violates search engine guidelines.

## Features

- **Browser-based Analysis**: Uses Selenium with headless Chrome for accurate content extraction from dynamic pages
- **Static HTML Analysis**: Fallback mode for analyzing HTML content without browser rendering  
- **Smart Word Analysis**: Filters stop words and focuses on meaningful keywords (3+ characters)
- **Configurable Threshold**: Customizable keyword density threshold (default: 5%)
- **Detailed Reporting**: Provides word counts, densities, and top keyword statistics
- **Multiple Input Methods**: Supports URLs, HTML strings, and local HTML files

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
python keyword_stuffing_detection.py --url "https://example.com"
```

### Analyze HTML Content (String)
```bash
python keyword_stuffing_detection.py --html "<html><body>SEO content here</body></html>"
```

### Analyze a Local HTML File
```bash
python keyword_stuffing_detection.py --html-file path/to/file.html
```

### Custom Density Threshold
```bash
python keyword_stuffing_detection.py --url "https://example.com" --threshold 0.03
```

### Save Results to File
```bash
python keyword_stuffing_detection.py --url "https://example.com" --output results.json
```

## Detection Logic

The script analyzes keyword density using the following process:

1. **Text Extraction**: Extracts visible text from HTML `<body>` element
2. **Normalization**: Converts to lowercase and removes punctuation
3. **Tokenization**: Splits into individual words (3+ characters)
4. **Stop Word Filtering**: Removes common words (the, and, of, etc.)
5. **Density Calculation**: `density = word_count / total_words`
6. **Threshold Check**: Flags keywords exceeding the density threshold (default: 5%)

### Stop Words Excluded
The script automatically excludes common stop words including:
- Articles: the, a, an
- Conjunctions: and, or, but
- Prepositions: in, on, at, to, for, of, with, by
- Common verbs: is, are, was, were, have, has, had
- Pronouns: i, you, he, she, it, we, they

## Output Format

The script outputs JSON with the following structure:

```json
{
  "status": "success",
  "url": "https://example.com",
  "title": "Page Title",
  "passed": false,
  "violations_count": 2,
  "violations": [
    {
      "keyword": "gardening",
      "count": 15,
      "density": 0.075,
      "density_percentage": 7.5,
      "threshold": 0.05,
      "threshold_percentage": 5.0
    }
  ],
  "stats": {
    "total_words": 200,
    "meaningful_words": 120,
    "unique_words": 85,
    "density_threshold": 0.05,
    "top_keywords": [
      {
        "keyword": "gardening",
        "count": 15,
        "density": 0.075,
        "density_percentage": 7.5
      }
    ]
  },
  "text_preview": "Welcome to our gardening site where we sell gardening tools...",
  "message": "Keyword stuffing detected: 'gardening' density 7.5% exceeds allowed maximum of 5.0%"
}
```

## Command Line Options

- `--url`: URL to analyze for keyword stuffing
- `--html`: HTML content string to analyze
- `--html-file`: Path to a local HTML file to analyze
- `--threshold`: Keyword density threshold (0-1, default: 0.05 = 5%)  
- `--output`: Output file for results (default: keyword_stuffing_results.json)

## Exit Codes

- `0`: Test passed (no keyword stuffing detected)
- `1`: Test failed (keyword stuffing detected) or error occurred

## Common Use Cases

- **SEO Auditing**: Identify pages with excessive keyword repetition
- **Content Quality Control**: Ensure natural keyword usage in content
- **Competitor Analysis**: Check competitor sites for keyword stuffing
- **Pre-publication Review**: Validate content before publishing
- **Bulk Site Analysis**: Batch process multiple pages or files

## Detection Examples

### Passing Content
```html
<body>
Welcome to our gardening website. We offer high-quality tools 
and expert advice for your garden maintenance needs.
</body>
```
**Result**: Natural keyword distribution, no violations.

### Failing Content  
```html
<body>
Gardening tools gardening tools best gardening tools cheap gardening 
tools buy gardening tools online gardening tools sale gardening tools.
</body>
```
**Result**: "gardening" density ~25%, "tools" density ~25% - both exceed 5% threshold.

## Technical Notes

- Uses headless Chrome for accurate JavaScript rendering
- Analyzes computed text content, not raw HTML
- Handles dynamic content and single-page applications  
- Considers word context and excludes navigation/UI text
- Provides detailed statistics for content analysis
- Supports international character sets (UTF-8)

## Limitations

- Requires Chrome/Chromium browser for URL analysis mode
- May not detect sophisticated keyword variations or synonyms
- Static HTML analysis mode has limited dynamic content support
- Performance depends on page load time and content complexity
- Threshold tuning may be needed for different content types

## Best Practices

- **Threshold Tuning**: Adjust `--threshold` based on content type (technical content may need higher thresholds)
- **Context Consideration**: Review violations manually - some repetition may be legitimate
- **Bulk Analysis**: Use with automation tools for large-scale SEO audits
- **Regular Monitoring**: Include in CI/CD pipelines for content quality gates