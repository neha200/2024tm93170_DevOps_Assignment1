from flask import Flask, jsonify, request, abort
app = Flask(__name__)

_members = [
    {"id": 1, "name": "Sam", "plan": "monthly"},
    {"id": 2, "name": "Riya", "plan": "annual"},
]

def _next_id(): return max((m["id"] for m in _members), default=0) + 1

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/")
def index():
    return jsonify({"message": "ACEest Fitness API"}), 200

@app.get("/api/members")
def list_members():
    return jsonify(_members), 200

@app.post("/api/members")
def create_member():
    if not request.is_json:
        abort(400, "Expected JSON")
    data = request.get_json(silent=True) or {}
    name, plan = data.get("name"), data.get("plan")
    if not name or not plan:
        abort(400, "name and plan required")
    item = {"id": _next_id(), "name": name, "plan": plan}
    _members.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
