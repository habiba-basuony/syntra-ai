import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_documentation_srs():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/document", json={
            "project_name": "TaskFlow",
            "doc_type": "SRS",
            "tasks": [
                {"title": "Login API", "assigned_to": "Ahmed", "status": "Done", "due_date": "2026-05-01"},
                {"title": "Dashboard UI", "assigned_to": "Sara", "status": "In Progress", "due_date": "2026-05-10"}
            ],
            "team_members": ["Ahmed", "Sara"],
            "project_description": "A project management tool for small teams",
            "progress_summary": "Backend 70% complete"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["doc_type"] == "SRS"
    assert "content" in data
    assert len(data["content"]) > 100


@pytest.mark.asyncio
async def test_documentation_weekly_report():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/document", json={
            "project_name": "EduTrack",
            "doc_type": "weekly_report",
            "tasks": [
                {"title": "ML Model", "assigned_to": "Karim", "status": "In Progress"}
            ],
            "team_members": ["Karim"],
            "project_description": "E-learning platform",
        })
    assert response.status_code == 200
