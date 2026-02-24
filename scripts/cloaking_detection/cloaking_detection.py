#!/usr/bin/env python3
"""
Cloaking Detection Script

This script detects cloaking by comparing content served to different user agents
(regular browser vs. Googlebot) and calculating content similarity.
"""

import argparse
import json
import re
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class CloakingDetector:
    def __init__(self, similarity_threshold=0.9, request_delay=2):
        self.similarity_threshold = similarity_threshold
        self.request_delay = request_delay
        
    def fetch_content(self, url, user_agent):
        """Fetch HTML content from URL using specified user agent."""
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
            response.raise_for_status()
            return {
                'status_code': response.status_code,
                'content': response.text,
                'final_url': response.url,
                'error': None
            }
        except requests.exceptions.Timeout:
            return {'error': 'Request timeout', 'content': None}
        except requests.exceptions.ConnectionError:
            return {'error': 'Connection error', 'content': None}
        except requests.exceptions.HTTPError as e:
            return {'error': f'HTTP error: {e}', 'content': None}
        except Exception as e:
            return {'error': f'Unexpected error: {e}', 'content': None}
    
    def extract_visible_text(self, html_content):
        """Extract visible text content from HTML, removing scripts, styles, etc."""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style", "meta", "link", "noscript"]):
                script.decompose()
            
            # Get text and clean it up
            text = soup.get_text()
            
            # Normalize whitespace
            text = re.sub(r'\s+', ' ', text)
            text = text.strip().lower()
            
            # Remove very short words and common stop words that might cause noise
            words = text.split()
            meaningful_words = [word for word in words if len(word) >= 3]
            
            return {
                'text': text,
                'words': meaningful_words,
                'word_count': len(meaningful_words)
            }
            
        except Exception as e:
            return {
                'text': '',
                'words': [],
                'word_count': 0,
                'error': f'Text extraction error: {e}'
            }
    
    def calculate_jaccard_similarity(self, words1, words2):
        """Calculate Jaccard similarity between two word sets."""
        if not words1 and not words2:
            return 1.0  # Both empty, considered identical
        
        set1 = set(words1)
        set2 = set(words2)
        
        if not set1 and not set2:
            return 1.0
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        if union == 0:
            return 0.0
            
        return intersection / union
    
    def detect_cloaking(self, url, user_agent_regular=None, user_agent_googlebot=None):
        """
        Main cloaking detection function.
        Returns detailed analysis results.
        """
        # Default user agents
        if not user_agent_regular:
            user_agent_regular = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        
        if not user_agent_googlebot:
            user_agent_googlebot = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        
        results = {
            'url': url,
            'user_agents': {
                'regular': user_agent_regular,
                'googlebot': user_agent_googlebot
            },
            'similarity_threshold': self.similarity_threshold,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Fetch content for regular user
        print(f"Fetching content as regular user...", file=sys.stderr)
        regular_response = self.fetch_content(url, user_agent_regular)
        
        if regular_response.get('error'):
            results['error'] = f"Failed to fetch content as regular user: {regular_response['error']}"
            return results
        
        # Wait between requests to be respectful
        time.sleep(self.request_delay)
        
        # Fetch content for Googlebot
        print(f"Fetching content as Googlebot...", file=sys.stderr)
        googlebot_response = self.fetch_content(url, user_agent_googlebot)
        
        if googlebot_response.get('error'):
            results['error'] = f"Failed to fetch content as Googlebot: {googlebot_response['error']}"
            return results
        
        # Extract text from both responses
        regular_text = self.extract_visible_text(regular_response['content'])
        googlebot_text = self.extract_visible_text(googlebot_response['content'])
        
        if regular_text.get('error'):
            results['error'] = f"Regular user content extraction error: {regular_text['error']}"
            return results
            
        if googlebot_text.get('error'):
            results['error'] = f"Googlebot content extraction error: {googlebot_text['error']}"
            return results
        
        # Calculate similarity
        similarity = self.calculate_jaccard_similarity(
            regular_text['words'], 
            googlebot_text['words']
        )
        
        # Determine if cloaking is detected
        is_cloaking = similarity < self.similarity_threshold
        
        results.update({
            'regular_user': {
                'status_code': regular_response['status_code'],
                'final_url': regular_response['final_url'],
                'word_count': regular_text['word_count'],
                'sample_text': regular_text['text'][:200] + '...' if len(regular_text['text']) > 200 else regular_text['text']
            },
            'googlebot': {
                'status_code': googlebot_response['status_code'], 
                'final_url': googlebot_response['final_url'],
                'word_count': googlebot_text['word_count'],
                'sample_text': googlebot_text['text'][:200] + '...' if len(googlebot_text['text']) > 200 else googlebot_text['text']
            },
            'analysis': {
                'similarity_score': round(similarity, 4),
                'similarity_percentage': round(similarity * 100, 2),
                'threshold_percentage': round(self.similarity_threshold * 100, 2),
                'cloaking_detected': is_cloaking,
                'status': 'fail' if is_cloaking else 'pass'
            }
        })
        
        if is_cloaking:
            results['analysis']['details'] = (
                f"Cloaking detected: Content similarity between regular user "
                f"({regular_text['word_count']} words) and Googlebot "
                f"({googlebot_text['word_count']} words) is {similarity:.4f} "
                f"({similarity*100:.2f}%), below the required threshold of "
                f"{self.similarity_threshold*100:.2f}%. This suggests different "
                f"content is being served to search engines versus users."
            )
        else:
            results['analysis']['details'] = (
                f"No cloaking detected: Content similarity is {similarity:.4f} "
                f"({similarity*100:.2f}%), above the threshold of "
                f"{self.similarity_threshold*100:.2f}%."
            )
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description="Detect cloaking by comparing content served to different user agents"
    )
    parser.add_argument(
        "--url", 
        required=True, 
        help="URL to check for cloaking"
    )
    parser.add_argument(
        "--user-agent-regular",
        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        help="User agent string for regular browser simulation"
    )
    parser.add_argument(
        "--user-agent-googlebot",
        default="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        help="User agent string for Googlebot simulation"
    )
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.9,
        help="Minimum content similarity threshold (0-1) to pass the test"
    )
    parser.add_argument(
        "--request-delay",
        type=int,
        default=2,
        help="Delay in seconds between requests"
    )
    parser.add_argument(
        "--output-format",
        choices=['json', 'summary'],
        default='json',
        help="Output format: full json or summary"
    )
    
    args = parser.parse_args()
    
    # Validate URL
    parsed_url = urlparse(args.url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print(json.dumps({
            "error": f"Invalid URL: {args.url}. Please provide a complete URL with http:// or https://"
        }), indent=2)
        return
    
    # Validate threshold
    if not 0 <= args.similarity_threshold <= 1:
        print(json.dumps({
            "error": "Similarity threshold must be between 0 and 1"
        }), indent=2)
        return
    
    # Run detection
    detector = CloakingDetector(
        similarity_threshold=args.similarity_threshold,
        request_delay=args.request_delay
    )
    
    results = detector.detect_cloaking(
        url=args.url,
        user_agent_regular=args.user_agent_regular,
        user_agent_googlebot=args.user_agent_googlebot
    )
    
    if args.output_format == 'summary' and 'analysis' in results:
        # Output simplified summary
        summary = {
            "url": results["url"],
            "status": results["analysis"]["status"],
            "cloaking_detected": results["analysis"]["cloaking_detected"],
            "similarity_score": results["analysis"]["similarity_score"],
            "similarity_percentage": results["analysis"]["similarity_percentage"],
            "details": results["analysis"]["details"]
        }
        print(json.dumps(summary, indent=2))
    else:
        # Output full results
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()