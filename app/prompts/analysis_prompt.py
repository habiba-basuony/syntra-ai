ANALYSIS_SYSTEM_PROMPT = """
You are an expert software project manager and technical lead.
Given a project idea and a team's skills, analyze the project and produce:
1. Feasibility assessment
2. Estimated timeline
3. Key risks
4. Suggested tech stack based on team skills
5. Task breakdown assigned to the right team members

Always respond ONLY with valid JSON. No explanation, no markdown.

Format:
{
  "feasibility": "High | Medium | Low",
  "estimated_timeline": "X weeks",
  "risks": ["risk1", "risk2"],
  "suggested_tech_stack": ["tech1", "tech2"],
  "tasks": [
    {
      "title": "...",
      "description": "...",
      "assigned_to": "member_name",
      "skills_needed": ["skill1"],
      "estimated_hours": 10
    }
  ]
}
"""

ANALYSIS_FEW_SHOT_EXAMPLES = """
--- EXAMPLE 1 ---
Project idea: Build a food delivery mobile app with real-time tracking
Team:
- Ahmed | Backend | Node.js, MongoDB, Express | 20h/week
- Sara | Frontend | React Native, Tailwind | 15h/week
- Omar | DevOps | Docker, AWS | 10h/week

Output:
{
  "feasibility": "High",
  "estimated_timeline": "10 weeks",
  "risks": [
    "Real-time tracking requires WebSocket expertise — team may need ramp-up time",
    "Mobile deployment to App Store/Play Store adds 1-2 weeks"
  ],
  "suggested_tech_stack": ["Node.js", "Express", "MongoDB", "React Native", "Socket.IO", "Docker", "AWS EC2"],
  "tasks": [
    {"title": "Design MongoDB schema", "description": "Design collections for users, orders, restaurants, drivers", "assigned_to": "Ahmed", "skills_needed": ["MongoDB"], "estimated_hours": 8},
    {"title": "Build Auth API", "description": "JWT-based login and registration endpoints", "assigned_to": "Ahmed", "skills_needed": ["Node.js", "Express"], "estimated_hours": 12},
    {"title": "Build Home Screen UI", "description": "Restaurant listing with filters", "assigned_to": "Sara", "skills_needed": ["React Native", "Tailwind"], "estimated_hours": 15},
    {"title": "Setup Docker & CI/CD", "description": "Containerize backend and deploy to AWS", "assigned_to": "Omar", "skills_needed": ["Docker", "AWS"], "estimated_hours": 10}
  ]
}

--- EXAMPLE 2 ---
Project idea: E-learning platform with quizzes and progress tracking
Team:
- Nour | Fullstack | React, Node.js, PostgreSQL | 25h/week
- Karim | ML | Python, Scikit-learn | 20h/week

Output:
{
  "feasibility": "High",
  "estimated_timeline": "8 weeks",
  "risks": [
    "One fullstack developer is a bottleneck — frontend and backend may block each other",
    "ML integration with Node.js backend requires clear API contracts"
  ],
  "suggested_tech_stack": ["React", "Node.js", "PostgreSQL", "Python", "FastAPI", "Scikit-learn"],
  "tasks": [
    {"title": "Build course CRUD API", "description": "Endpoints for creating, reading, updating courses", "assigned_to": "Nour", "skills_needed": ["Node.js", "PostgreSQL"], "estimated_hours": 20},
    {"title": "Build quiz frontend", "description": "Interactive quiz UI with timer and score display", "assigned_to": "Nour", "skills_needed": ["React"], "estimated_hours": 18},
    {"title": "Build progress tracking ML model", "description": "Predict student performance based on quiz scores", "assigned_to": "Karim", "skills_needed": ["Python", "Scikit-learn"], "estimated_hours": 25},
    {"title": "Expose ML as FastAPI endpoint", "description": "Wrap ML model in a REST API", "assigned_to": "Karim", "skills_needed": ["FastAPI", "Python"], "estimated_hours": 8}
  ]
}
"""

def build_analysis_prompt(project_idea: str, team: list) -> str:
    team_str = ""
    for member in team:
        skills = ", ".join(member["skills"])
        team_str += f"- {member['name']} | {member['role']} | {skills} | {member['hours_per_week']}h/week\n"

    return f"""
{ANALYSIS_FEW_SHOT_EXAMPLES}

--- NOW GENERATE ---
Project idea: {project_idea}
Team:
{team_str}

Output:
"""
