from flask import Flask, jsonify, request, abort
import store

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/")
def index():
    return jsonify({"message": "ACEest Fitness API"}), 200

# ---- Workouts API (matches flask_web.py behavior) ----

@app.get("/api/workouts")
def api_list_workouts():
    return jsonify(store.list_workouts()), 200

@app.post("/api/workouts")
def api_create_workout():
    # Accept JSON: {"workout": "Run", "duration": 30}
    if not request.is_json:
        abort(400, "Expected JSON body")
    data = request.get_json(silent=True) or {}
    try:
        item = store.add_workout(data.get("workout"), data.get("duration"))
    except ValueError as e:
        abort(400, str(e))
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
