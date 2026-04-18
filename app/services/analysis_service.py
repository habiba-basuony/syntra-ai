from langchain_google_genai import ChatGoogleGenerativeAI
from app.chains.analysis_chain import run_analysis_chain
from app.models.requests.analysis_request import AnalysisRequest
from app.models.responses.analysis_response import AnalysisResponse, TaskItem


async def analyze_project(
    request: AnalysisRequest,
    llm: ChatGoogleGenerativeAI
) -> AnalysisResponse:

    team_data = [member.model_dump() for member in request.team]

    raw = await run_analysis_chain(
        llm=llm,
        project_idea=request.project_idea,
        team=team_data
    )

    tasks = [TaskItem(**task) for task in raw["tasks"]]

    return AnalysisResponse(
        feasibility=raw["feasibility"],
        estimated_timeline=raw["estimated_timeline"],
        risks=raw["risks"],
        suggested_tech_stack=raw["suggested_tech_stack"],
        tasks=tasks
    )
