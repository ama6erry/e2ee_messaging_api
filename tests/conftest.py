# tests/conftest.py
import pytest

from api import create_app
from api.sessions.store import clear_sessions


@pytest.fixture
def app():
    app = create_app()
    app.config.update(TESTING=True)
    yield app
    clear_sessions()


@pytest.fixture
def client(app):
    return app.test_client()