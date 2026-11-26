"""
Kết nối Redis dùng chung cho rate limiter và cost guard.
Không ping Redis lúc import để app vẫn khởi động được khi Redis chưa sẵn sàng.
"""
import redis

from app.config import settings

r: redis.Redis | None = (
    redis.from_url(
        settings.redis_url,
        decode_responses=True,
        socket_connect_timeout=1.0,
        socket_timeout=1.0,
    )
    if settings.redis_url
    else None
)


def redis_healthy() -> bool:
    """Kiểm tra kết nối Redis cho GET /ready."""
    if r is None:
        return False
    try:
        return bool(r.ping())
    except redis.RedisError:
        return False
