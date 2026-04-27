from fastapi import FastAPI
from app.config import settings   # import your config

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "App working",
        "db": settings.DATABASE_URL
    }

@app.get("/email-test")
def test_email():
    return {
        "smtp": settings.SMTP_HOST
    }

