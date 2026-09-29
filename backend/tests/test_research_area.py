"""Tests for research area inference and blog exposure."""

from fastapi.testclient import TestClient

from app.main import app
from app.models.schemas import ResearchArea
from app.services.research_area import infer_research_area

client = TestClient(app)


def test_infer_medicinal_from_medical_tag():
    area = infer_research_area(
        tags=["medical", "research"],
        title="Cannabidiol for chronic pain",
        excerpt="",
    )
    assert area == ResearchArea.MEDICINAL


def test_infer_agronomy_from_cultivation_tag():
    area = infer_research_area(
        tags=["cultivation", "research"],
        title="Yield traits in industrial hemp",
        excerpt="",
    )
    assert area == ResearchArea.AGRONOMIA


def test_infer_construction_from_hempcrete_textile_tag():
    area = infer_research_area(
        tags=["textile", "research"],
        title="Thermal and mechanical properties of hempcrete with low-carbon binders",
        excerpt="",
    )
    assert area == ResearchArea.CONSTRUCAO


def test_infer_regulatorio_from_policy_tag():
    area = infer_research_area(
        tags=["policy", "research"],
        title="Cannabis retail systems",
        excerpt="",
    )
    assert area == ResearchArea.REGULATORIO


def test_list_blog_includes_research_area():
    response = client.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    assert rows
    assert all(row.get("research_area") for row in rows)
