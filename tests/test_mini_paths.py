import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_mini_path_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/mini-path", json={
            "task_title": "Build REST API",
            "task_description": "Create CRUD endpoints using FastAPI",
            "member_skills": ["Python", "Flask"],
            "missing_skill": "FastAPI"
        })
    assert response.status_code == 200
    data = response.json()
    assert "mini_path" in data
    assert len(data["mini_path"]) > 0
    assert data["missing_skill"] == "FastAPI"


@pytest.mark.asyncio
async def test_mini_path_missing_fields():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/ai/mini-path", json={
            "task_title": "Build REST API"
            # missing required fields
        })
    assert response.status_code == 422
