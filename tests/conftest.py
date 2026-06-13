import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app
from app.dependencies import get_session
from app.db.session import CSVSession

SAMPLE_DATA = [
    {"title": "Clean Code", "type": "book", "category": "software-engineering", "notes": "Great book", "link": "https://example.com/clean-code"},
    {"title": "The Pragmatic Programmer", "type": "book", "category": "software-engineering", "notes": "Timeless advice", "link": "https://example.com/pragmatic"},
    {"title": "FastAPI Docs", "type": "article", "category": "python", "notes": "Official docs", "link": "https://fastapi.tiangolo.com"},
    {"title": "Real Python", "type": "website", "category": "python", "notes": "Tutorials", "link": "https://realpython.com"},
    {"title": "Docker Deep Dive", "type": "book", "category": "devops", "notes": "Beginner guide", "link": "https://example.com/docker"},
]


@pytest.fixture
def mock_session():
    """A CSVSession pre-loaded with sample data (no file I/O)."""
    session = MagicMock(spec=CSVSession)
    session.data = SAMPLE_DATA
    return session


@pytest.fixture
def client(mock_session):
    """TestClient with the CSV session dependency overridden."""
    app.dependency_overrides[get_session] = lambda: mock_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
