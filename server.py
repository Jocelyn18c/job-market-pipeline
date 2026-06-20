from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/api/jobs")

def get_jobs():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/api/skills")

def get_skills():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skills")
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True, port=5000)