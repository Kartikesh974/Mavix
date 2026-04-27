from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "test@gmail.com"
    SMTP_PASSWORD: str = "test123"
    
    EMAIL_RECIPIENT: str = "test@gmail.com"
    SECRET_KEY: str = "abc123"

    model_config = ConfigDict(env_file=".env")

settings = Settings()