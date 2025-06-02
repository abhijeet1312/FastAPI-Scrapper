import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from fastapi import HTTPException

class WebScrapingService:
    @staticmethod
    def fetch_page_content(url: str) -> tuple:
        """Fetch and parse webpage content"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract meta information
            title = soup.find('title')
            title = title.get_text().strip() if title else ""
            
            description = soup.find('meta', attrs={'name': 'description'})
            description = description.get('content', '').strip() if description else ""
            
            # Extract H1 tags
            h1_tags = [h1.get_text().strip() for h1 in soup.find_all('h1')]
            
            # Extract outbound links
            links = soup.find_all('a', href=True)
            outbound_links = []
            domain = urlparse(url).netloc
            
            for link in links:
                href = link['href']
                full_url = urljoin(url, href)
                parsed = urlparse(full_url)
                
                if parsed.netloc and parsed.netloc != domain:
                    outbound_links.append(full_url)
            
            # Remove duplicates
            outbound_links = list(set(outbound_links))
            
            # Extract text content for keyword analysis
            text_content = soup.get_text()
            
            return title, description, h1_tags, outbound_links, text_content
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error fetching webpage: {str(e)}")
