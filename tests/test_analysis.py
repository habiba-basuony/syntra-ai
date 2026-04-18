import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_analysis_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/analyze", json={
            "project_idea": "Build a food delivery app with real-time tracking",
            "team": [
                {
                    "name": "Ahmed",
                    "role": "Backend",
                    "skills": ["Node.js", "MongoDB"],
                    "hours_per_week": 20
                },
                {
                    "name": "Sara",
                    "role": "Frontend",
                    "skills": ["React", "Tailwind"],
                    "hours_per_week": 15
                }
            ]
        })
    assert response.status_code == 200
    data = response.json()
    assert "feasibility" in data
    assert "tasks" in data
    assert len(data["tasks"]) > 0


@pytest.mark.asyncio
async def test_analysis_empty_team():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/analyze", json={
            "project_idea": "Some project",
            "team": []
        })
    assert response.status_code == 200
