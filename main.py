from fastapi import FastAPI
from controllers.website_controller import WebsiteController
from model.website_models import URLRequest, WebsiteAnalysis, BlogSuggestionsResponse

# Initialize FastAPI app
app = FastAPI(title="Website Analyzer API", version="1.0.0")

# Initialize controller
website_controller = WebsiteController()

@app.get("/")
async def root():
    return {"message": "Website Analyzer API", "endpoints": ["/analyze", "/suggest-blogs"]}

@app.post("/analyze", response_model=WebsiteAnalysis)
async def analyze_website(request: URLRequest):
    """Analyze a website and return comprehensive insights"""
    return await website_controller.analyze_website(request)

@app.post("/suggest-blogs", response_model=BlogSuggestionsResponse)
async def suggest_blog_titles(request: URLRequest):
    """Suggest SEO-optimized blog titles for a company"""
    return await website_controller.suggest_blog_titles(request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)