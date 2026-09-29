"""Blog publication date display and sorting."""

from app.services.blog_publication import (
    normalize_publication_date,
    publication_sort_key,
    resolve_publication_date,
)


def test_normalize_publication_date_handles_partial_dates():
    assert normalize_publication_date("2025-10") == "2025-10-01"
    assert normalize_publication_date("2024") == "2024-01-01"
    assert normalize_publication_date("2025-06-23") == "2025-06-23"
    assert normalize_publication_date(None) is None


def test_resolve_publication_date_prefers_scholarly_date_for_research():
    item = {
        "source_type": "agent_research",
        "published_date": "2025-05-14",
        "published_at": "2026-09-07T12:02:00",
    }
    assert resolve_publication_date(item) == "2025-05-14"


def test_resolve_publication_date_falls_back_for_manual_posts():
    item = {
        "source_type": "manual",
        "published_at": "2026-03-01T10:00:00",
    }
    assert resolve_publication_date(item) == "2026-03-01"


def test_resolve_publication_date_missing_for_research_without_date():
    item = {
        "source_type": "agent_research",
        "published_at": "2026-09-07T12:02:00",
    }
    assert resolve_publication_date(item) is None


def test_publication_sort_key_orders_newest_first():
    items = [
        {"source_type": "agent_research", "published_date": "2024-01-01", "id": "old"},
        {"source_type": "agent_research", "published_date": "2026-08-31", "id": "new"},
        {"source_type": "agent_research", "published_at": "2026-09-07T12:00:00", "id": "undated"},
    ]
    ordered = sorted(items, key=publication_sort_key, reverse=True)
    assert [item["id"] for item in ordered] == ["new", "old", "undated"]


def test_list_blog_sorted_by_publication_date():
    from fastapi.testclient import TestClient

    from app.main import app

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    assert rows
    assert rows[0]["published_date"] == "2026-09-25"
    assert rows[0]["slug"] == (
        "industrial-hemp-response-to-waterlogging-stress-influence-of-duration-and-growth"
    )

    dates = [row.get("published_date") for row in rows if row.get("published_date")]
    assert dates == sorted(dates, reverse=True)


ISSUE47_DOIS = [
    "10.1186/s42238-026-00498-6",
    "10.1038/s41598-026-59272-6",
    "10.3390/sci8090261",
    "10.14311/app.2026.59.0021",
    "10.1001/jamanetworkopen.2026.31306",
    "10.1021/acs.jnatprod.6c00674",
    "10.1038/s41538-026-01158-y",
    "10.1186/s42238-026-00489-7",
    "10.1007/s10853-026-13577-z",
    "10.1007/s10570-026-07205-x",
]


def test_issue47_research_posts_are_published():
    from fastapi.testclient import TestClient

    from app.main import app
    from app.repositories.json_store import blog_store

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    citations = " ".join(row.get("citation") or "" for row in rows)
    for doi in ISSUE47_DOIS:
        assert doi in citations

    seed_rows = blog_store.read_all()
    issue47_rows = [
        row
        for row in seed_rows
        if row.get("id", "").startswith("blog-research-20260921-")
    ]
    assert len(issue47_rows) == 10
    for row in issue47_rows:
        assert row.get("source_type") == "agent_research"
        assert row.get("title_pt")
        assert row.get("i18n", {}).get("en", {}).get("excerpt")
        assert "## Por que importa" in row.get("content_markdown", "")
        assert "PLACEHOLDER" not in row.get("content_markdown", "")


ISSUE28_DOIS = [
    "10.1186/s12870-026-09909-5",
    "10.3389/fpls.2026.1930650",
    "10.1186/s42238-026-00485-x",
    "10.12912/27197050/231235",
    "10.3390/f17091068",
    "10.1038/s41386-026-02533-9",
    "10.1007/s40261-026-01595-3",
    "10.1186/s42238-026-00492-y",
    "10.1208/s12248-026-01281-4",
    "10.1186/s42238-026-00487-9",
    "10.3390/fib14090095",
    "10.1016/j.clcb.2026.100232",
]


def test_issue28_research_posts_are_published():
    from fastapi.testclient import TestClient

    from app.main import app
    from app.repositories.json_store import blog_store

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    citations = " ".join(row.get("citation") or "" for row in rows)
    for doi in ISSUE28_DOIS:
        assert doi in citations

    seed_rows = blog_store.read_all()
    issue28_rows = [
        row
        for row in seed_rows
        if row.get("id", "").startswith("blog-research-20260914-")
    ]
    assert len(issue28_rows) == 12
    for row in issue28_rows:
        assert row.get("source_type") == "agent_research"
        assert row.get("title_pt")
        assert row.get("i18n", {}).get("en", {}).get("excerpt")
        assert "## Por que importa" in row.get("content_markdown", "")


def test_research_posts_expose_institution_metadata():
    from app.repositories.json_store import blog_store

    research_rows = [
        row for row in blog_store.read_all() if row.get("source_type") == "agent_research"
    ]
    assert research_rows
    for row in research_rows:
        assert row.get("research_institution"), row["id"]
        assert row.get("research_country_code"), row["id"]


def test_list_blog_includes_research_institution_fields():
    from fastapi.testclient import TestClient

    from app.main import app

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    research = [row for row in response.json() if row.get("source_type") == "agent_research"]
    assert research
    assert research[0].get("research_institution")
    assert research[0].get("research_country_code")


def test_to_blog_post_carries_published_date():
    from app.models.schemas import ScientificPaperRaw
    from app.services.paper_normalizer import ScientificPaperNormalizer

    normalizer = ScientificPaperNormalizer()
    raw = ScientificPaperRaw(
        title="Sample Paper",
        authors=["A. Author"],
        abstract="Abstract text.",
        published_date="2025-03-15",
    )
    blog = normalizer.to_blog_post(normalizer.normalize(raw))
    assert blog.published_date == "2025-03-15"


ISSUE49_DOIS = [
    "10.1111/tpj.16769",
    "10.1038/s41598-024-58931-w",
    "10.1002/agj2.21537",
    "10.1371/journal.pone.0315951",
    "10.1161/JAHA.123.030178",
    "10.1001/jamanetworkopen.2024.34354",
    "10.1001/jamainternmed.2024.3270",
    "10.1001/jamapediatrics.2024.4352",
    "10.1017/S0033291724000990",
    "10.1001/jamahealthforum.2023.4897",
    "10.1001/jamapsychiatry.2024.0698",
    "10.1016/j.jaac.2024.02.016",
    "10.1016/j.jclepro.2024.143689",
    "10.1016/j.clce.2024.100123",
    "10.1016/j.indcrop.2024.118487",
]


ISSUE60_DOIS = [
    "10.1186/s42238-026-00507-8",
    "10.3390/crops6050090",
    "10.1007/s43939-026-00983-y",
    "10.1186/s42238-026-00508-7",
    "10.1186/s12906-026-05585-y",
    "10.1186/s42238-026-00501-0",
    "10.1111/ajad.70202",
    "10.1186/s42238-026-00495-9",
    "10.1186/s42238-026-00499-5",
    "10.1001/jamanetworkopen.2026.31213",
    "10.3389/fpubh.2026.1915903",
    "10.47481/yjad.1945143",
]


def test_issue60_research_posts_are_published():
    from fastapi.testclient import TestClient

    from app.main import app
    from app.repositories.json_store import blog_store

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    citations = " ".join(row.get("citation") or "" for row in rows)
    for doi in ISSUE60_DOIS:
        assert doi in citations

    seed_rows = blog_store.read_all()
    issue60_rows = [
        row
        for row in seed_rows
        if row.get("id", "").startswith("blog-research-20260928-")
    ]
    assert len(issue60_rows) == 12
    for row in issue60_rows:
        assert row.get("source_type") == "agent_research"
        assert row.get("title_pt")
        assert row.get("i18n", {}).get("en", {}).get("excerpt")
        assert "## Por que importa" in row.get("content_markdown", "")
        assert row.get("research_institution")
        assert row.get("research_country_code")
        assert row.get("research_area")
        assert "PLACEHOLDER" not in row.get("content_markdown", "")


def test_issue49_research_posts_are_published():
    from fastapi.testclient import TestClient

    from app.main import app
    from app.repositories.json_store import blog_store

    api = TestClient(app)
    response = api.get("/api/v1/blog", params={"limit": 100})
    assert response.status_code == 200
    rows = response.json()
    citations = " ".join(row.get("citation") or "" for row in rows)
    for doi in ISSUE49_DOIS:
        assert doi in citations

    seed_rows = blog_store.read_all()
    issue49_rows = [
        row
        for row in seed_rows
        if row.get("id", "").startswith("blog-research-20260927-")
    ]
    assert len(issue49_rows) == 15
    for row in issue49_rows:
        assert row.get("source_type") == "agent_research"
        assert row.get("title_pt")
        assert row.get("i18n", {}).get("en", {}).get("excerpt")
        assert "## Por que importa" in row.get("content_markdown", "")
        assert row.get("research_institution")
        assert row.get("research_country_code")
        assert "PLACEHOLDER" not in row.get("content_markdown", "")
