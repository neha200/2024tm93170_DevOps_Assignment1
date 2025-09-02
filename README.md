# 2024tm93170_DevOps_Assignment1

This repository implements a **DevOps workflow** for a fitness and gym management system.
It demonstrates **Flask application development, unit testing, Dockerization, and CI/CD pipelines with GitHub Actions**.

---

## Project Overview

As a Junior DevOps Engineer, the goal is to:

1. Build a basic **Flask web + API application** for fitness tracking.
2. Use **Git + GitHub** for version control and collaboration.
3. Write **unit tests** with `pytest` to validate functionality.
4. Automate tests with **GitHub Actions**.
5. Package applications into **Docker images** for consistent deployment.
6. Push images to **Docker Hub** with proper versioning.
7. Gate CI/CD pipeline with **CHANGELOG.md** updates.

---

## Project Structure

```
ACEest_Fitness/
├── App/
│   ├── app.py              # Tkinter starter (kept for assessment record)
│   ├── flask_api.py        # REST API for members (/api/members)
│   ├── flask_web.py        # Web UI (add + view workouts)
│   └── __init__.py
│
├── Test/
│   ├── conftest.py         # Pytest fixture for Flask app
│   └── test_api.py         # Unit tests for API
│
├── UI/
│   ├── index.html          # Web page for workout logging
│   └── base.html
│
├── .github/workflows/ci.yml # CI/CD pipeline definition
├── Dockerfile              # API container
├── Dockerfile.web          # Web UI container
├── requirements.txt        # Python dependencies
├── CHANGELOG.md            # Version history (CI gated)
└── README.md               # Documentation
```

---

## Application Components

### 1. **Flask API (`flask_api.py`)**

* Endpoints:

  * `GET /health` → `{ "status": "ok" }`
  * `GET /api/members` → list members
  * `POST /api/members` → create new member
* Used for API testing and validation.

### 2. **Flask Web UI (`flask_web.py`)**

* Web-based workout tracker.
* Features:

  * Add new workout (name + duration).
  * View logged workouts.
* Templates: `UI/index.html` + `UI/base.html`.

### 3. **Tkinter App (`app.py`)**

* Original assignment starter.
* Replaced with Flask web app for web deployment.
* Kept in repo for traceability.

---

## Testing (Pytest)

* Unit tests live in `Test/`.
* Run locally:

```bash
# create venv and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run tests
pytest -q
```

---

## Dockerization

Two Dockerfiles are provided:

* **API (`Dockerfile`)**
  Runs `flask_api.py` with Gunicorn.

* **Web UI (`Dockerfile.web`)**
  Runs `flask_web.py` with Gunicorn and serves HTML templates.

Build & run locally:

```bash
# API
docker build -t aceest-fitness:api -f Dockerfile .
docker run --rm -p 8000:8000 aceest-fitness:api

# Web
docker build -t aceest-fitness:web -f Dockerfile.web .
docker run --rm -p 8000:8000 aceest-fitness:web
```

Visit:

* API → [http://localhost:8000/health](http://localhost:8000/health)
* Web → [http://localhost:8000/](http://localhost:8000/)

---

## CI/CD Pipeline

The CI/CD workflow (`.github/workflows/ci.yml`) implements:

### **Feature branch CI**

* Trigger: push to `feature/*` branch when `CHANGELOG.md` is updated.
* Steps:

  * Verify new changelog entry.
  * Build API image.
  * Run tests (`pytest`).
  * Smoke test API `/health`.

### **Release CI**

* Trigger: PR merged into `main`.
* Steps:

  * Check if `CHANGELOG.md` changed.
  * Build API image.
  * Run tests.
  * Smoke test API `/health`.

### **Docker Hub Publish**

* Runs only if release CI succeeds.
* Builds & pushes:

  * API image (`Dockerfile`) → tags: `latest`, `api-<sha>`
  * Web image (`Dockerfile.web`) → tags: `web-latest`, `web-<sha>`

---

## CHANGELOG Policy

* All feature work **must update `CHANGELOG.md`**.
* CI enforces presence of a new `## version` entry.
* Example entry:

```markdown
## [1.0.2] - 2025-09-01
- Added Web UI for workout tracking.
- Dockerized both API and Web apps.
- Integrated CI/CD with Docker Hub.
```

---

## How to Run Locally

1. Clone repo:

   ```bash
   git clone https://github.com/<your-username>/aceest-fitness.git
   cd aceest-fitness
   ```

2. Create virtualenv & install deps:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run API:

   ```bash
   python App/flask_api.py
   ```

4. Run Web UI:

   ```bash
   python App/flask_web.py
   ```

---

##  What This Project Demonstrates

* Flask API & Web development.
* Pytest integration for unit testing.
* Dockerization of services (API + Web).
* GitHub Actions CI/CD with branch & changelog gating.
* Secure image push to Docker Hub.
* Enforced PR-based workflow (no direct push to `main`).

---
