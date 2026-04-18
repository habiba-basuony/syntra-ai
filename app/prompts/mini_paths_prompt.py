MINI_PATHS_SYSTEM_PROMPT = """
You are an expert learning path designer for software developers.
Given a task a team member needs to complete and a skill they are missing,
generate a short, focused learning path to fill that gap quickly.

Always respond ONLY with valid JSON. No explanation, no markdown.

Format:
{
  "missing_skill": "...",
  "mini_path": [
    {"step": 1, "topic": "...", "resource": "...", "duration": "..."},
    {"step": 2, "topic": "...", "resource": "...", "duration": "..."}
  ]
}
"""

MINI_PATHS_FEW_SHOT_EXAMPLES = """
--- EXAMPLE 1 ---
Task: Build a REST API using FastAPI
Member skills: Python, Flask
Missing skill: FastAPI

Output:
{
  "missing_skill": "FastAPI",
  "mini_path": [
    {"step": 1, "topic": "FastAPI Installation & Project Structure", "resource": "https://fastapi.tiangolo.com/tutorial/", "duration": "1h"},
    {"step": 2, "topic": "Path Parameters & Request Body with Pydantic", "resource": "https://fastapi.tiangolo.com/tutorial/body/", "duration": "1.5h"},
    {"step": 3, "topic": "Build your first CRUD endpoint", "resource": "https://www.youtube.com/watch?v=0sOvCWFmrtA", "duration": "2h"}
  ]
}

--- EXAMPLE 2 ---
Task: Design the database schema for the project
Member skills: Python, MySQL
Missing skill: MongoDB

Output:
{
  "missing_skill": "MongoDB",
  "mini_path": [
    {"step": 1, "topic": "MongoDB vs SQL — Core Concepts", "resource": "https://www.mongodb.com/docs/manual/introduction/", "duration": "1h"},
    {"step": 2, "topic": "CRUD Operations in MongoDB", "resource": "https://www.mongodb.com/docs/manual/crud/", "duration": "1.5h"},
    {"step": 3, "topic": "Schema Design & Embedded Documents", "resource": "https://www.mongodb.com/docs/manual/data-modeling/", "duration": "1h"}
  ]
}
"""

def build_mini_paths_prompt(task_title: str, task_description: str,
                             member_skills: list, missing_skill: str) -> str:
    skills_str = ", ".join(member_skills)
    return f"""
{MINI_PATHS_FEW_SHOT_EXAMPLES}

--- NOW GENERATE ---
Task: {task_title} — {task_description}
Member skills: {skills_str}
Missing skill: {missing_skill}

Output:
"""
