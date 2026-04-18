from fastapi import APIRouter, Depends
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models.requests.analysis_request import AnalysisRequest
from app.models.responses.analysis_response import AnalysisResponse
from app.services.analysis_service import analyze_project
from app.core.llm_factory import get_llm

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analysis_endpoint(
    request: AnalysisRequest,
    llm: ChatGoogleGenerativeAI = Depends(get_llm)
):
    """
    Feature 07 — AI Analysis & Recommendations
    Evaluates a project idea, estimates timeline & risks,
    suggests tech stack, and distributes tasks across the team.
    """
    return await analyze_project(request, llm)
