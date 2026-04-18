from fastapi import APIRouter, Depends
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models.requests.mini_paths_request import MiniPathRequest
from app.models.responses.mini_paths_response import MiniPathResponse
from app.services.mini_paths_service import generate_mini_path
from app.core.llm_factory import get_llm

router = APIRouter()


@router.post("/mini-path", response_model=MiniPathResponse)
async def mini_path_endpoint(
    request: MiniPathRequest,
    llm: ChatGoogleGenerativeAI = Depends(get_llm)
):
    """
    Feature 02 — Mini Learning Paths
    Generates a short learning path to fill a skill gap for a team member.
    Triggered by Feature 06 when a skill gap is detected.
    """
    return await generate_mini_path(request, llm)
