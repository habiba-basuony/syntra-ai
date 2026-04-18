import json
import re


def clean_llm_json(raw_text: str) -> dict:
    """
    Cleans LLM response and parses it as JSON.
    Handles cases where Gemini wraps output in markdown code blocks.
    """
    text = raw_text.strip()

    # Remove markdown code blocks: ```json ... ``` or ``` ... ```
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = text.strip()

    return json.loads(text)