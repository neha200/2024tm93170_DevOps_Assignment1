from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash
from App import store  # <-- use shared store

TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "UI"
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))
app.secret_key = "dev-secret"

@app.get("/")
def home():
    return render_template("index.html", workouts=store.list_workouts())

@app.post("/add")
def add_workout():
    try:
        store.add_workout(request.form.get("workout"), request.form.get("duration"))
        flash("Workout added!", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
