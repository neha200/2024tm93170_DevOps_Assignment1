def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200 and r.get_json()["status"] == "ok"

def test_index(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "ACEest Fitness" in r.get_json()["message"]

def test_members_flow(client):
    r = client.get("/api/members")
    assert r.status_code == 200 and isinstance(r.get_json(), list)

    create = client.post("/api/members", json={"name": "Alex", "plan": "monthly"})
    assert create.status_code == 201
    body = create.get_json()
    assert body["name"] == "Alex" and body["plan"] == "monthly"
