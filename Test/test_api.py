def test_health_ok(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}

def test_list_initially_empty(client):
    r = client.get("/api/workouts")
    assert r.status_code == 200
    assert r.get_json() == []

def test_add_requires_json(client):
    r = client.post("/api/workouts", data="not-json", content_type="text/plain")
    assert r.status_code == 400

def test_add_requires_fields(client):
    r = client.post("/api/workouts", json={"workout": "Run"})
    assert r.status_code == 400
    r = client.post("/api/workouts", json={"duration": 30})
    assert r.status_code == 400

def test_add_requires_positive_integer_duration(client):
    r = client.post("/api/workouts", json={"workout": "Run", "duration": "abc"})
    assert r.status_code == 400

    r = client.post("/api/workouts", json={"workout": "Run", "duration": 0})
    assert r.status_code == 400

def test_add_success_and_list(client):
    r = client.post("/api/workouts", json={"workout": "Run", "duration": 30})
    assert r.status_code == 201
    created = r.get_json()
    assert created["id"] == 1
    assert created["workout"] == "Run"
    assert created["duration"] == 30

    r2 = client.get("/api/workouts")
    assert r2.status_code == 200
    assert r2.get_json() == [created]

    # Add a second one to verify incremental IDs
    r3 = client.post("/api/workouts", json={"workout": "Swim", "duration": 45})
    assert r3.status_code == 201
    assert r3.get_json()["id"] == 2
