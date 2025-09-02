# Simple in-memory store used by both API and Web
# Each workout: {"id": int, "workout": str, "duration": int}

_workouts = []
_next_id = 1

def list_workouts():
    return list(_workouts)

def add_workout(workout: str, duration: int):
    global _next_id
    workout = (workout or "").strip()
    if not workout:
        raise ValueError("Workout is required")
    try:
        duration = int(duration)
    except Exception as e:
        raise ValueError("Duration must be an integer") from e
    if duration <= 0:
        raise ValueError("Duration must be positive")

    item = {"id": _next_id, "workout": workout, "duration": duration}
    _workouts.append(item)
    _next_id += 1
    return item
