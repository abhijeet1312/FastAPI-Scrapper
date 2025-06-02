from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):
    url: HttpUrl

class WebsiteAnalysis(BaseModel):
    url: str
    title: str
    description: str
    h1_tags: List[str]
    outbound_links: List[str]
    target_keywords: List[str]
    company_summary: str
    recommended_channels: List[str]

class BlogSuggestion(BaseModel):
    title: str
    rationale: str

class BlogSuggestionsResponse(BaseModel):
    suggestions: List[BlogSuggestion]
