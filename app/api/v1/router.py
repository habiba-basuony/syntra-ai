from fastapi import APIRouter
from app.api.v1.routes import mini_paths, analysis, documentation

router = APIRouter(prefix="/api/ai")

router.include_router(mini_paths.router, tags=["Mini Learning Paths"])
router.include_router(analysis.router, tags=["AI Analysis"])
#router.include_router(documentation.router, tags=["Auto Documentation"])
