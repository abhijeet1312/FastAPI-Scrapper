from typing import List
from fastapi import HTTPException
from services.cache_service import CacheService
from services.web_scraping_service import WebScrapingService
from services.keyword_service import KeywordService
from services.ai_analysis_service import AIAnalysisService
from model.website_models import BlogSuggestion

class WebsiteAnalysisService:
    def __init__(self):
        self.cache_service = CacheService()
        self.scraping_service = WebScrapingService()
        self.keyword_service = KeywordService()
        self.ai_service = AIAnalysisService()
    
    async def analyze_website(self, url: str) -> dict:
        """Analyze a website and return comprehensive insights"""
        cache_key = self.cache_service.get_cache_key(url)

        # Check cache first
        cached_result = self.cache_service.get_from_cache(cache_key)
        if cached_result:
            return cached_result

        try:
            # Fetch and parse website content
            title, description, h1_tags, outbound_links, text_content = self.scraping_service.fetch_page_content(url)

            # Extract keywords
            keywords = self.keyword_service.extract_keywords(text_content)

            # Analyze with Gemini AI
            company_summary, recommended_channels = await self.ai_service.analyze_with_gemini(text_content, keywords)

            # Prepare result
            result = {
                "url": url,
                "title": title,
                "description": description,
                "h1_tags": h1_tags,
                "outbound_links": outbound_links[:20],  # Limit to first 20
                "target_keywords": keywords,
                "company_summary": company_summary,
                "recommended_channels": recommended_channels
            }

            # Cache result
            self.cache_service.set_cache(cache_key, result)

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    
    async def suggest_blog_titles(self, url: str) -> List[BlogSuggestion]:
        """Suggest SEO-optimized blog titles for a company"""
        # Try to get existing analysis from cache
        cache_key = self.cache_service.get_cache_key(url)
        cached_analysis = self.cache_service.get_from_cache(cache_key)
        
        if cached_analysis:
            company_summary = cached_analysis.get("company_summary", "")
            keywords = cached_analysis.get("target_keywords", [])
        else:
            # Perform quick analysis
            try:
                title, description, h1_tags, outbound_links, text_content = self.scraping_service.fetch_page_content(url)
                keywords = self.keyword_service.extract_keywords(text_content)
                company_summary, _ = await self.ai_service.analyze_with_gemini(text_content, keywords)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to analyze website: {str(e)}")
        
        # Generate blog suggestions
        suggestions = await self.ai_service.suggest_blog_titles_with_gemini(company_summary, keywords)
        
        return suggestions
