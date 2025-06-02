from model.website_models import URLRequest, WebsiteAnalysis, BlogSuggestionsResponse
from services.website_analysis_service import WebsiteAnalysisService

class WebsiteController:
    def __init__(self):
        self.analysis_service = WebsiteAnalysisService()
    
    async def analyze_website(self, request: URLRequest) -> WebsiteAnalysis:
        """Analyze a website and return comprehensive insights"""
        url_str = str(request.url)
        result = await self.analysis_service.analyze_website(url_str)
        return WebsiteAnalysis(**result)
    
    async def suggest_blog_titles(self, request: URLRequest) -> BlogSuggestionsResponse:
        """Suggest SEO-optimized blog titles for a company"""
        url_str = str(request.url)
        suggestions = await self.analysis_service.suggest_blog_titles(url_str)
        return BlogSuggestionsResponse(suggestions=suggestions)
