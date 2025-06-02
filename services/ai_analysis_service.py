import google.generativeai as genai
from typing import List
from model.website_models import BlogSuggestion

class AIAnalysisService:
    @staticmethod
    async def analyze_with_gemini(text_content: str, keywords: List[str]) -> tuple:
        """Analyze content using Gemini AI"""
        try:
            # Initialize Gemini model
            model = genai.GenerativeModel('models/gemini-2.0-flash')
            
            # Prepare prompt for company analysis
            analysis_prompt = f"""
            Based on the following website content and keywords, provide:
            1. A brief summary of what the company offers (2-3 sentences)
            2. Recommended marketing channels based on the product/service type (list 3-5 channels)
            
            Content preview: {text_content[:2000]}...
            Keywords: {', '.join(keywords)}
            
            Format your response as:
            SUMMARY: [company summary]
            CHANNELS: [channel1, channel2, channel3, etc.]
            """
            
            response = model.generate_content(analysis_prompt)
            
            # Parse response
            lines = response.text.strip().split('\n')
            summary = ""
            channels = []
            
            for line in lines:
                if line.startswith('SUMMARY:'):
                    summary = line.replace('SUMMARY:', '').strip()
                elif line.startswith('CHANNELS:'):
                    channels_text = line.replace('CHANNELS:', '').strip()
                    channels = [ch.strip() for ch in channels_text.split(',')]
            
            return summary, channels
            
        except Exception as e:
            # Fallback analysis if Gemini fails
            print(f"Gemini analysis failed: {e}")
            return "Technology/software company based on website content", ["Content Marketing", "SEO", "Social Media", "Email Marketing"]

    @staticmethod
    async def suggest_blog_titles_with_gemini(company_summary: str, keywords: List[str]) -> List[BlogSuggestion]:
        """Generate blog title suggestions using Gemini AI"""
        try:
            model = genai.GenerativeModel('models/gemini-2.0-flash')
            
            prompt = f"""
            Based on this company summary and keywords, suggest 3 SEO-optimized blog titles that would help drive traffic:
            
            Company: {company_summary}
            Keywords: {', '.join(keywords[:10])}
            
            Format each suggestion as:
            TITLE: [blog title]
            RATIONALE: [why this title would work for SEO]
            
            Make titles engaging and keyword-rich.
            """
            
            response = model.generate_content(prompt)
            
            # Parse response
            suggestions = []
            lines = response.text.strip().split('\n')
            current_title = ""
            
            for line in lines:
                if line.startswith('TITLE:'):
                    current_title = line.replace('TITLE:', '').strip()
                elif line.startswith('RATIONALE:') and current_title:
                    rationale = line.replace('RATIONALE:', '').strip()
                    suggestions.append(BlogSuggestion(title=current_title, rationale=rationale))
                    current_title = ""
            
            return suggestions if suggestions else [
                BlogSuggestion(title="10 Tips for Better Online Presence", rationale="General SEO-friendly title"),
                BlogSuggestion(title="Industry Trends and Insights", rationale="Targets industry keywords"),
                BlogSuggestion(title="Complete Guide to [Your Service]", rationale="Long-tail keyword targeting")
            ]
            
        except Exception as e:
            print(f"Blog suggestion failed: {e}")
            return [
                BlogSuggestion(title="10 Tips for Better Online Presence", rationale="General SEO-friendly title"),
                BlogSuggestion(title="Industry Trends and Insights", rationale="Targets industry keywords"),
                BlogSuggestion(title="Complete Guide to Your Service", rationale="Long-tail keyword targeting")
            ]
