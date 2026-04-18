import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from app.prompts.mini_paths_prompt import MINI_PATHS_SYSTEM_PROMPT, build_mini_paths_prompt
from app.core.exceptions import AIServiceException
from app.core.utils import clean_llm_json


async def run_mini_paths_chain(
    llm: ChatGoogleGenerativeAI,
    task_title: str,
    task_description: str,
    member_skills: list,
    missing_skill: str
) -> dict:
    try:
        human_prompt = build_mini_paths_prompt(
            task_title, task_description, member_skills, missing_skill
        )

        messages = [
            SystemMessage(content=MINI_PATHS_SYSTEM_PROMPT),
            HumanMessage(content=human_prompt)
        ]

        response = await llm.ainvoke(messages)
        result = clean_llm_json(response.content)
        return result

    except json.JSONDecodeError as e:
        raise AIServiceException(f"LLM returned invalid JSON for mini paths: {str(e)}", 500)
    except Exception as e:
        raise AIServiceException(f"Mini paths chain failed: {str(e)}", 500)