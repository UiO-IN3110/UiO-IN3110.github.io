import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

assignment_dir = Path(__file__).parent.parent.absolute()

# Ensure assignment dir is on sys.path
# so that we can import `app` and `strompris`
sys.path.insert(0, str(assignment_dir))


@pytest.fixture
def client():
    """Fixture to return an HTTP client that can talk to our test app"""
    from app import app

    return TestClient(app)
