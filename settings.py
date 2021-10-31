from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8000
    DATABASE_URL: str = "sqlite:///./database.sqlite3"

    JWT_SECRET: str = ".env"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 3600


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)
