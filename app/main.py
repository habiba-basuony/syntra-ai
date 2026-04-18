from fastapi import FastAPI
from app.api.v1.router import router
from app.core.exceptions import AIServiceException, ai_exception_handler
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Microservice for Syntra.AI — 3 Features: Mini Learning Paths, AI Analysis, Auto Documentation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Register custom exception handler
app.add_exception_handler(AIServiceException, ai_exception_handler)

# Register all routes
app.include_router(router)


@app.get("/")
async def root():
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "features": [
            "02 — Mini Learning Paths",
            "07 — AI Analysis & Recommendations",
            "08 — Auto Documentation & Reporting"
        ]
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
