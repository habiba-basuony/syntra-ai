from fastapi import APIRouter, Depends
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models.requests.documentation_request import DocumentationRequest
from app.models.responses.documentation_response import DocumentationResponse
from app.services.documentation_service import generate_documentation
from app.core.llm_factory import get_llm

router = APIRouter()


@router.post("/document", response_model=DocumentationResponse)
async def documentation_endpoint(
    request: DocumentationRequest,
    llm: ChatGoogleGenerativeAI = Depends(get_llm)
):
    """
    Feature 08 — Auto Documentation & Reporting
    Generates SRS, Weekly Reports, Gantt Charts, or Final Presentations
    based on project data and team progress.
    """
    return await generate_documentation(request, llm)
