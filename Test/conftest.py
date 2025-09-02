# Test/conftest.py
import sys, pathlib, pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "App"

# put repo root and App/ on sys.path (works even with spaces)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from App.flask_api import app as flask_app

@pytest.fixture
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as c:
        yield c
