import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from app.prompts.documentation_prompt import DOCUMENTATION_SYSTEM_PROMPT, build_documentation_prompt
from app.core.exceptions import AIServiceException
from app.core.utils import clean_llm_json


async def run_documentation_chain(
    llm: ChatGoogleGenerativeAI,
    project_name: str,
    doc_type: str,
    tasks: list,
    team_members: list,
    project_description: str,
    progress_summary: str = None
) -> dict:
    try:
        human_prompt = build_documentation_prompt(
            project_name, doc_type, tasks,
            team_members, project_description, progress_summary
        )

        messages = [
            SystemMessage(content=DOCUMENTATION_SYSTEM_PROMPT),
            HumanMessage(content=human_prompt)
        ]

        response = await llm.ainvoke(messages)
        result = clean_llm_json(response.content)
        return result

    except json.JSONDecodeError as e:
        raise AIServiceException(f"LLM returned invalid JSON for documentation: {str(e)}", 500)
    except Exception as e:
        raise AIServiceException(f"Documentation chain failed: {str(e)}", 500)