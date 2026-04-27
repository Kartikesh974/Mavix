from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend Live ✅",
        "db": settings.DATABASE_URL
    }