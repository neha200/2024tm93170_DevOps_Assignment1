# Ensures we can import your App modules and gives a clean app/client per test

import sys
import pathlib
import pytest

# Add repo root and App/ to sys.path so imports work in CI and locally
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "App"))

from App.flask_api import app as flask_app
from App import store

@pytest.fixture(autouse=True)
def reset_store():
    """Reset the in-memory workouts store before each test."""
    store._workouts.clear()
    store._next_id = 1
    yield

@pytest.fixture()
def client():
    flask_app.config.update(TESTING=True)
    return flask_app.test_client()
