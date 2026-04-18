# from langchain_google_genai import ChatGoogleGenerativeAI
# from app.core.config import settings


# def get_llm() -> ChatGoogleGenerativeAI:
#     """
#     Returns a configured Gemini 2.5 Flash LLM instance.
#     Called once per request via dependency injection.
#     """
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         google_api_key=settings.GEMINI_API_KEY,
#         temperature=0.7,
#     )
from langchain_groq import ChatGroq
from app.core.config import settings


def get_llm() -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0.7,
    )