---
title: Detect excessive repetition of keywords indicative of keyword stuffing
impact: MEDIUM
impactDescription: Overusing keywords reduces content quality and is considered spam.
tags: keyword_stuffing
script: ../scripts/keyword_stuffing_detection/keyword_stuffing_detection.py
inputFields:
  - name: url
    required: false
    description: URL to analyze for keyword stuffing using browser rendering.
  - name: html
    required: false
    description: HTML content string to evaluate for keyword stuffing.
  - name: html_file
    required: false
    description: Path to local HTML file to analyze for keyword stuffing.
  - name: threshold
    required: false
    default: 0.05
    description: Keyword density threshold (0-1, default 0.05 = 5%).
---

## KEYWORD_STUFFING_DETECTION
Detects excessive repetition of keywords indicative of keyword stuffing using both browser-based and static HTML analysis.

## Evidence to collect
- Visible text content from HTML body element
- Word frequency counts and density calculations
- Top keywords and their usage statistics
- Text length and meaningful word analysis

## Logic (pseudocode)  
Input: url OR html OR html_file, threshold (optional)
1. If URL provided:
   - Load page in headless browser to handle JavaScript content
   - Extract rendered HTML and page title
2. If HTML content provided:
   - Use static HTML parsing for analysis
3. Extract visible text from <body> element:
   - Remove script, style, meta tags
   - Clean whitespace and normalize text
4. Tokenize and normalize words:
   - Convert to lowercase
   - Extract alphanumeric sequences (3+ characters)
   - Filter out common stop words (the, and, of, etc.)
5. Calculate keyword density for each word:
   - density = word_count / total_words
   - Compare against threshold (default 5%)
6. Flag violations where density exceeds threshold
7. Provide detailed statistics and top keyword analysis

## Technical Implementation Notes
- Uses Selenium WebDriver for accurate JavaScript rendering
- Comprehensive stop word filtering (60+ common words)
- Configurable density threshold with validation
- Analyzes meaningful words only (excludes very short words)
- Handles international character sets (UTF-8)
- Provides word count statistics and content preview

## Pass condition
No meaningful keyword exceeds the specified density threshold (default: 5% of total words).

## Failure messages
Keyword stuffing detected: '${keyword}' density ${density_percentage}% exceeds allowed maximum of ${threshold_percentage}%

## Examples
### Passing
- **Natural Content**: `<body>Welcome to our site about gardening tools and outdoor equipment.</body>` (2% keyword density)
- **Technical Content**: `<body>JavaScript variables and functions help developers create interactive web applications.</body>` (Legitimate repetition)
- **List Content**: `<body><ul><li>Red roses</li><li>Blue roses</li><li>White roses</li></ul></body>` (3% density in context)
- **Product Descriptions**: `<body>Professional gardening tools for serious gardeners who need reliable equipment.</body>` (Natural usage)

### Failing  
- **Obvious Stuffing**: `<body>Buy gardening tools gardening tools gardening tools gardening tools gardening tools.</body>` (~50% density)
- **Hidden Repetition**: `<body>Best SEO services for SEO optimization and SEO marketing by SEO experts offering SEO solutions for SEO success.</body>` (35% "SEO" density)
- **Keyword Lists**: `<body>Cheap pills discount pills pharmacy pills buy pills online pills medications pills.</body>` (40% "pills" density)
- **Unnatural Patterns**: `<body>Dog food for dogs who eat dog food from our dog food store selling dog food.</body>` (30% "dog" density)

### Edge Cases
- **Brand Names**: Legitimate brand repetition should be considered in context
- **Technical Documentation**: Code examples may have natural keyword repetition
- **Navigation Elements**: Menu items and headers with repeated terms
- **Multi-language Content**: Different density patterns in various languages
- **Short Content**: Small text samples may have misleading density calculations

### Threshold Considerations
- **5% (Default)**: Good for general web content and marketing pages
- **3% (Strict)**: Suitable for high-quality editorial content  
- **7% (Lenient)**: May be appropriate for technical documentation or product catalogs
- **Custom**: Adjust based on content type and industry standards

### References
Google Search Central - Keyword Stuffing — https://developers.google.com/search/docs/essentials/spam-policies#keyword-stuffing
Google Search Central - Keywords — https://developers.google.com/search/docs/appearance/keywords