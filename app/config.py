from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SMTP_SERVER: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAIL_RECIPIENT: str
    SECRET_KEY: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()