import re
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
timesPath = "./times/"

@app.route("/api/run/update/<distance>", methods=["GET"])
def update_time(distance):
    distances = {
        "5": 5000,
        "10": 10000,
        "21": 21097.5,
        "42": 42195,
    }

    if distance not in distances:
        return jsonify({"error": "Dostępne dystanse to 5, 10, 21 i 42."}), 404

    time = request.args.get("time", "")
    if not re.fullmatch(r"[0-9]{2}:[0-5][0-9]:[0-5][0-9]", time):
        return jsonify({"error": "Podaj parametr time w formacie hh:mm:ss."}), 400

    times_dir = Path(timesPath)
    times_dir.mkdir(parents=True, exist_ok=True)
    (times_dir / f"{distance}.txt").write_text(time, encoding="utf-8")

    response = jsonify({
        "distance": distances[distance],
        "time": time,
        "completed": True,
    })
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route("/api/run/<distance>", methods=["GET"])
def time(distance):
    distances = {
        "5": 5000,
        "10": 10000,
        "21": 21097.5,
        "42": 42195,
    }
    if distance not in distances:
            return jsonify({"error": "Dostępne dystanse to 5, 10, 21 i 42."}), 404
    completion, content = handleFile(timesPath + distance + ".txt")
    return jsonify({"distance": distances[distance], "time": content, "completed" : completion})

def handleFile(filePath):
    try: 
        file = open(filePath, "r+")
        content = file.read().strip()
        file.close()
        completion = True
        if content == "":
            completion = False
    except FileNotFoundError:
        file = open(filePath, "x")
        completion = False
        content = ""
        file.close()
    return completion, content
