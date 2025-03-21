from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Authorization Service"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15


    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


    class Config:
        env_file = ".env"

settings = Settings()