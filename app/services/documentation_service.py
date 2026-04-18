from langchain_google_genai import ChatGoogleGenerativeAI
from app.chains.documentation_chain import run_documentation_chain
from app.models.requests.documentation_request import DocumentationRequest
from app.models.responses.documentation_response import DocumentationResponse


async def generate_documentation(
    request: DocumentationRequest,
    llm: ChatGoogleGenerativeAI
) -> DocumentationResponse:

    tasks_data = [task.model_dump() for task in request.tasks]

    raw = await run_documentation_chain(
        llm=llm,
        project_name=request.project_name,
        doc_type=request.doc_type.value,
        tasks=tasks_data,
        team_members=request.team_members,
        project_description=request.project_description,
        progress_summary=request.progress_summary
    )

    return DocumentationResponse(
        doc_type=raw["doc_type"],
        project_name=raw["project_name"],
        content=raw["content"]
    )
