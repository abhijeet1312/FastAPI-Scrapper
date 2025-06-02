import json
import hashlib
import os
import redis
from typing import Optional, Dict

class CacheService:
    def __init__(self):
        self.redis_url = os.getenv("REDIS")
        self.redis_client = None
        self.memory_cache = {}
        self._initialize_redis()
    
    def _initialize_redis(self):
        try:
            if self.redis_url:
                self.redis_client = redis.Redis.from_url(self.redis_url, decode_responses=True)
            else:
                # fallback to local Redis
                self.redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
            self.redis_client.ping()
            print("✅ Connected to Redis")
        except Exception as e:
            print(f"❌ Redis not available ({e}), using in-memory cache")
            self.redis_client = None
    
    def get_cache_key(self, url: str) -> str:
        """Generate cache key for URL"""
        return f"website_analysis:{hashlib.md5(url.encode()).hexdigest()}"

    def get_from_cache(self, key: str) -> Optional[dict]:
        """Get data from cache"""
        try:
            if self.redis_client:
                data = self.redis_client.get(key)
                return json.loads(data) if data else None
            else:
                return self.memory_cache.get(key)
        except:
            return None

    def set_cache(self, key: str, data: dict, ttl: int = 3600):
        """Set data in cache"""
        try:
            if self.redis_client:
                self.redis_client.setex(key, ttl, json.dumps(data))
            else:
                self.memory_cache[key] = data
        except:
            pass
