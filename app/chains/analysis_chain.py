import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from app.prompts.analysis_prompt import ANALYSIS_SYSTEM_PROMPT, build_analysis_prompt
from app.core.exceptions import AIServiceException
from app.core.utils import clean_llm_json


async def run_analysis_chain(
    llm: ChatGoogleGenerativeAI,
    project_idea: str,
    team: list
) -> dict:
    try:
        human_prompt = build_analysis_prompt(project_idea, team)

        messages = [
            SystemMessage(content=ANALYSIS_SYSTEM_PROMPT),
            HumanMessage(content=human_prompt)
        ]

        response = await llm.ainvoke(messages)
        result = clean_llm_json(response.content)
        return result

    except json.JSONDecodeError as e:
        raise AIServiceException(f"LLM returned invalid JSON for analysis: {str(e)}", 500)
    except Exception as e:
        raise AIServiceException(f"Analysis chain failed: {str(e)}", 500)