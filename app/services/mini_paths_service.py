from langchain_google_genai import ChatGoogleGenerativeAI
from app.chains.mini_paths_chain import run_mini_paths_chain
from app.models.requests.mini_paths_request import MiniPathRequest
from app.models.responses.mini_paths_response import MiniPathResponse, PathStep


async def generate_mini_path(
    request: MiniPathRequest,
    llm: ChatGoogleGenerativeAI
) -> MiniPathResponse:

    raw = await run_mini_paths_chain(
        llm=llm,
        task_title=request.task_title,
        task_description=request.task_description,
        member_skills=request.member_skills,
        missing_skill=request.missing_skill
    )

    steps = [PathStep(**step) for step in raw["mini_path"]]

    return MiniPathResponse(
        missing_skill=raw["missing_skill"],
        mini_path=steps
    )
