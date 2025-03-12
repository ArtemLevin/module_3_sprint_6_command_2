from .base import BaseTokenService
from .redis.redis_client import redis_client


ACCESS_TOKEN_PREFIX = "access_token:"
REFRESH_TOKEN_PREFIX = "refresh_token:"

class RedisTokenService(BaseTokenService):
    def save_token(self, user_id: str, token: str, token_type: str, expires_in: int):
        key = f"{ACCESS_TOKEN_PREFIX if token_type == 'access' else REFRESH_TOKEN_PREFIX}{user_id}"
        redis_client.setex(key, expires_in, token)

    def get_token(self, user_id: str, token_type: str) -> str:
        key = f"{ACCESS_TOKEN_PREFIX if token_type == 'access' else REFRESH_TOKEN_PREFIX}{user_id}"
        return redis_client.get(key)

    def delete_token(self, user_id: str, token_type: str):
        key = f"{ACCESS_TOKEN_PREFIX if token_type == 'access' else REFRESH_TOKEN_PREFIX}{user_id}"
        redis_client.delete(key)

    def is_token_valid(self, user_id: str, token: str, token_type: str) -> bool:
        stored_token = self.get_token(user_id, token_type)
        return stored_token == token