---
title: Detect hidden text or links intended solely for search engines
impact: MEDIUM
impactDescription: Hidden text or links are used to manipulate rankings without providing value to users.
tags: hidden_text
script: ../scripts/hidden_text_detection/hidden_text_detection.py
inputFields:
  - name: url
    required: false
    description: URL to analyze for hidden text using browser rendering engine.
  - name: html
    required: false
    description: HTML content to evaluate for hidden text patterns (static analysis).
---

## HIDDEN_TEXT_DETECTION
Detects hidden text or links intended solely for search engines using both static HTML analysis and browser-based rendering detection.

## Evidence to collect
- Elements with CSS properties that hide content visually
- Text content and links within hidden elements
- Computed styles and rendered dimensions
- Positioning and opacity values

## Logic (pseudocode)  
Input: url OR html
1. If URL provided:
   - Load page in headless browser
   - Find all elements containing text or links
   - For each element, check computed CSS properties:
     - display: none, visibility: hidden, opacity: 0
     - Zero width/height dimensions
     - Off-screen positioning (negative coordinates)
     - Negative text-indent values
     - Zero font-size
     - Text color matching background color
   - Use browser's is_displayed() method as final check
2. If HTML provided:
   - Parse HTML and find elements with style attributes
   - Check for common hiding patterns in inline styles
   - Detect text content or links in hidden elements
3. Flag elements with meaningful content (>2 words or links) that are hidden
4. Return detailed analysis with hiding methods and affected elements

## Technical Implementation Notes
- Uses Selenium WebDriver with headless Chrome for accurate rendering
- Analyzes computed CSS properties, not just inline styles
- Handles dynamic content and JavaScript-rendered elements  
- Detects various hiding techniques: CSS, positioning, color, dimensions
- Fallback static analysis for HTML-only inputs
- Considers text length and link presence to avoid false positives
- Provides detailed evidence with hiding methods and element selectors

## Pass condition
No elements with hidden styles contain meaningful text content (>2 words) or links.

## Failure messages
Hidden text detected in ${count} element(s). Primary violation: ${hiding_method} on ${element_selector} containing "${text_preview}"

## Examples
### Passing
- **Empty Hidden Elements**: `<div style="display:none"></div>` - No content to hide
- **Legitimate Hidden UI**: `<div style="display:none" id="modal">Modal dialog content</div>` - Short UI text 
- **CSS Animation Elements**: Elements temporarily hidden during transitions
- **Screen Reader Content**: `<span class="sr-only">Screen reader text</span>` - Accessibility content (single words)

### Failing  
- **Hidden Keyword Stuffing**: `<div style="display:none">cheap discount pharmacy pills buy online</div>`
- **Invisible Links**: `<a href="/spam-page" style="visibility:hidden">Hidden spam link</a>`
- **Off-screen Text**: `<p style="position:absolute;left:-9999px">SEO keyword content here</p>`
- **Zero Font Size**: `<span style="font-size:0px">Hidden text for search engines</span>`
- **Color Matching**: `<div style="color:white;background:white">White text on white background</div>`
- **Text Indent Hiding**: `<h1 style="text-indent:-9999px">Hidden heading with keywords</h1>`
- **Zero Dimensions**: `<div style="width:0;height:0;overflow:hidden">Hidden content block</div>`

### Edge Cases
- **Dynamic Content**: JavaScript-generated hidden content may require URL-based analysis
- **CSS Classes**: External stylesheets hiding content won't be detected in HTML-only mode
- **Legitimate Hiding**: Skip lists, mobile navigation, and accessibility content with minimal text
- **Partial Hiding**: Content partially hidden (clipped) rather than completely invisible

### References
Google Search Central - Hidden Text and Links — https://developers.google.com/search/docs/essentials/spam-policies#hidden-text-and-links
Google Search documentation — https://developers.google.com/search/docs/appearance/hidden-content