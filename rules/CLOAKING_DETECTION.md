---
title: Detect cloaking by comparing content served to Googlebot vs regular users
impact: HIGH
impactDescription: Cloaking presents different content to search engines and users to manipulate rankings and mislead users.
tags: cloaking
script: ../scripts/cloaking_detection/cloaking_detection.py
inputFields:
  - name: url
    required: true
    description: URL to fetch and compare content for cloaking detection.
  - name: user_agent_regular
    required: false
    default: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    description: User agent string for regular browser simulation.
  - name: user_agent_googlebot
    required: false
    default: "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    description: User agent string for Googlebot simulation.
  - name: similarity_threshold
    required: false
    default: 0.9
    description: Minimum content similarity threshold (0-1) to pass the test.
---

## CLOAKING_DETECTION
Detects cloaking by comparing the content served to Googlebot and regular users.

## Evidence to collect
- Text content from both Googlebot and user HTML
- Similarity score between the two

## Logic (pseudocode)  
Input: url, user_agent_regular, user_agent_googlebot, similarity_threshold
1. Fetch HTML content from the URL using regular browser user agent
2. Fetch HTML content from the same URL using Googlebot user agent  
3. Extract visible text content from both HTML documents (strip tags, scripts, styles)
4. Normalize whitespace and convert to lowercase for both text contents
5. Calculate similarity using Jaccard similarity:
   - Split text into word sets for both contents  
   - Jaccard = intersection(words1, words2) / union(words1, words2)
6. If similarity >= similarity_threshold then PASS else FAIL
7. Return similarity score and verdict

## Technical Implementation Notes
- Use requests library with custom User-Agent headers
- Handle redirects and HTTP errors gracefully
- Use BeautifulSoup or similar for HTML parsing and text extraction  
- Remove navigation, footer, and other non-content elements if possible
- Consider rate limiting between requests to avoid being blocked

## Pass condition
The content served to Googlebot and to regular users is substantially identical (similarity ≥ 90%).

## Failure messages
Cloaking detected: Content similarity between regular user (${words_user} words) and Googlebot (${words_googlebot} words) is ${similarity_score} (${similarity_percentage}%), below the required threshold of ${threshold_percentage}%. This suggests different content is being served to search engines versus users.

## Examples
### Passing
- **Identical Content**: Both user agents receive the same homepage with product listings
- **Minor Differences**: User sees personalized "Welcome back!" but core content identical (>90% similarity)
- **Dynamic Content**: Time-based content (date/time stamps) that changes but main content remains same

### Failing  
- **Keyword Stuffing**: Googlebot sees "buy cheap discount pharmacy pills medications" while users see normal homepage
- **Different Pages**: Users see a blog post while Googlebot is served a keyword-optimized landing page
- **Hidden Content**: Search engines see text content while users are redirected to a video-only page
- **Spam Redirection**: Googlebot sees legitimate content while users are redirected to unrelated affiliate pages

### Edge Cases
- **JavaScript-heavy sites**: May appear different to crawlers that don't execute JS
- **Geo-targeting**: Different content by location should be consistent for same region  
- **A/B testing**: Random variations should not trigger false positives

### References
Google Search documentation — https://developers.google.com/search/docs/advanced/crawling/cloaking