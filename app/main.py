from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import enquiry
from app.database import engine, Base
import asyncio

app = FastAPI(title="IT Company API", version="1.0.0")

# CORS - allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(enquiry.router)

@app.on_event("startup")
async def startup():
    # Create tables (for development only; use Alembic in production)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "IT Company API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}