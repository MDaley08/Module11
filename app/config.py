from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #defaults if no .env
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    SECRET_KEY: str = "dev-only-insecure-key-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()