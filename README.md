# 🔍 Website Analyzer API

A powerful FastAPI-based web application that analyzes websites and provides comprehensive insights including SEO analysis, keyword extraction, company summaries, and AI-powered blog title suggestions.

## ✨ Features

- **🕸️ Web Scraping**: Extract title, meta description, H1 tags, and outbound links
- **🔑 Keyword Analysis**: Intelligent keyword extraction with frequency analysis
- **🤖 AI-Powered Insights**: Company analysis and marketing channel recommendations using Google Gemini AI
- **📝 Blog Suggestions**: SEO-optimized blog title recommendations with rationale
- **⚡ Caching**: Redis-backed caching with memory fallback for improved performance
- **🏗️ MVC Architecture**: Clean, maintainable code structure following best practices

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Redis (optional, falls back to memory cache)
- Google Gemini AI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/website-analyzer-api.git
   cd website-analyzer-api
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn requests beautifulsoup4 redis google-generativeai pydantic
   ```

3. **Set up environment variables**
   ```bash
   export REDIS_URL="redis://localhost:6379"  # Optional
   export GOOGLE_API_KEY="your-gemini-api-key"
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:5000`

## 📖 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 🏠 Root
```http
GET /
```
Returns API information and available endpoints.

#### 📊 Analyze Website
```http
POST /analyze
```

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "title": "Example Website",
  "description": "Website description",
  "h1_tags": ["Main Heading", "Secondary Heading"],
  "outbound_links": ["https://external-site.com"],
  "target_keywords": ["keyword1", "keyword2", "keyword3"],
  "company_summary": "Brief company description",
  "recommended_channels": ["Content Marketing", "SEO", "Social Media"]
}
```

#### 💡 Suggest Blog Titles
```http
POST /suggest-blogs
```

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "suggestions": [
    {
      "title": "10 Best Practices for Your Industry",
      "rationale": "Targets industry-specific keywords and provides value"
    },
    {
      "title": "Complete Guide to [Your Service]",
      "rationale": "Long-tail keyword targeting with comprehensive content"
    }
  ]
}
```

## 🏗️ Architecture

The application follows a clean MVC (Model-View-Controller) architecture:

```
📁 Project Structure
├── models/
│   └── website_models.py       # Pydantic models for data validation
├── services/
│   ├── cache_service.py        # Redis/memory caching
│   ├── web_scraping_service.py # Web scraping & content extraction
│   ├── keyword_service.py      # Keyword analysis
│   ├── ai_analysis_service.py  # AI-powered analysis
│   └── website_analysis_service.py # Main orchestration
├── controllers/
│   └── website_controller.py   # Request/response handling
└── main.py                     # FastAPI app & routes
```

### 🔄 Data Flow

```
FastAPI Route → Controller → WebsiteAnalysisService → Individual Services → Response
```

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing
- **[Redis](https://redis.io/)** - Caching layer
- **[Google Gemini AI](https://ai.google.dev/)** - AI-powered analysis
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation
- **[Requests](https://docs.python-requests.org/)** - HTTP requests

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `REDIS_URL` | Redis connection URL | No | `redis://localhost:6379` |
| `GOOGLE_API_KEY` | Google Gemini AI API key | Yes | - |

### Caching

The application uses a two-tier caching strategy:
1. **Primary**: Redis (if available)
2. **Fallback**: In-memory cache

Cache TTL: 1 hour (3600 seconds)

## 🔧 Development

### Running in Development Mode

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

### Testing

```bash
# Install testing dependencies
pip install pytest httpx

# Run tests
pytest
```

### API Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:5000/docs`
- **ReDoc**: `http://localhost:5000/redoc`



## 📊 Usage Examples

### Using Postman

**Analyze Website:**
- Method: `POST`
- URL: `http://localhost:5000/analyze`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
  "url": "https://example.com"
}
```

**Get Blog Suggestions:**
- Method: `POST`
- URL: `http://localhost:5000/suggest-blogs`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
  "url": "https://example.com"
}
```



## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [API Docs](http://localhost:5000/docs)
- **Issues**: [GitHub Issues](https://github.com/yourusername/website-analyzer-api/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/website-analyzer-api/discussions)

## 📞 Support

If you have any questions or need help, please:
1. Check the [documentation](http://localhost:5000/docs)
2. Search [existing issues](https://github.com/yourusername/website-analyzer-api/issues)
3. Create a [new issue](https://github.com/yourusername/website-analyzer-api/issues/new)

---

⭐ **Star this repository if you find it helpful!**
