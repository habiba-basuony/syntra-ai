DOCUMENTATION_SYSTEM_PROMPT = """
You are an expert software engineering documentation writer.
Given project data, generate professional technical documentation.
The output must be clean, structured, and ready to use.

Always respond ONLY with valid JSON. No explanation, no markdown outside the content field.

Format:
{
  "doc_type": "...",
  "project_name": "...",
  "content": "full document text here"
}
"""

DOCUMENTATION_FEW_SHOT_EXAMPLES = """
--- EXAMPLE 1 — SRS ---
Project: TaskFlow
Doc type: SRS
Team: Ahmed (Backend), Sara (Frontend)
Tasks: [Login API - Ahmed - Done, Dashboard UI - Sara - In Progress]
Description: A project management tool for small teams

Output:
{
  "doc_type": "SRS",
  "project_name": "TaskFlow",
  "content": "SOFTWARE REQUIREMENTS SPECIFICATION\\nTaskFlow — Project Management Tool\\n\\n1. INTRODUCTION\\nTaskFlow is a web-based project management tool designed for small teams to organize tasks, track progress, and collaborate effectively.\\n\\n2. SYSTEM OVERVIEW\\nThe system consists of a React frontend and a Node.js backend connected to MongoDB.\\n\\n3. FUNCTIONAL REQUIREMENTS\\n3.1 Authentication\\n- Users must be able to register and login securely\\n- JWT-based session management\\n3.2 Task Management\\n- Users can create, assign, update, and delete tasks\\n- Tasks have status: Todo, In Progress, Done\\n\\n4. NON-FUNCTIONAL REQUIREMENTS\\n- Response time under 500ms\\n- Support up to 100 concurrent users\\n\\n5. TEAM & RESPONSIBILITIES\\n- Ahmed: Backend API development\\n- Sara: Frontend UI development"
}

--- EXAMPLE 2 — Weekly Report ---
Project: EduTrack
Doc type: weekly_report
Team: Nour (Fullstack), Karim (ML)
Tasks: [Course API - Nour - Done, Quiz UI - Nour - In Progress, ML Model - Karim - In Progress]
Description: E-learning platform with AI progress tracking
Progress: Backend 70% done, ML model training started

Output:
{
  "doc_type": "weekly_report",
  "project_name": "EduTrack",
  "content": "WEEKLY PROGRESS REPORT\\nEduTrack — E-Learning Platform\\nWeek of: [Current Week]\\n\\nSUMMARY\\nGood progress this week. Backend APIs are 70% complete and ML model training has begun.\\n\\nCOMPLETED THIS WEEK\\n- Course CRUD API fully implemented and tested (Nour)\\n- ML dataset preprocessing completed (Karim)\\n\\nIN PROGRESS\\n- Quiz UI component — 40% complete (Nour)\\n- ML progress tracking model — training phase (Karim)\\n\\nNEXT WEEK PLAN\\n- Complete Quiz UI and connect to backend\\n- Evaluate ML model and expose as FastAPI endpoint\\n\\nBLOCKERS\\n- None currently\\n\\nOVERALL STATUS: On Track"
}
"""

def build_documentation_prompt(project_name: str, doc_type: str,
                                tasks: list, team_members: list,
                                project_description: str,
                                progress_summary: str = None) -> str:
    tasks_str = ", ".join([f"{t['title']} - {t['assigned_to']} - {t['status']}" for t in tasks])
    team_str = ", ".join(team_members)
    progress_str = progress_summary or "No summary provided"

    return f"""
{DOCUMENTATION_FEW_SHOT_EXAMPLES}

--- NOW GENERATE ---
Project: {project_name}
Doc type: {doc_type}
Team: {team_str}
Tasks: [{tasks_str}]
Description: {project_description}
Progress: {progress_str}

Output:
"""
