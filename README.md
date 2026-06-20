# Job Market Pipeline

A full-stack data pipeline that extracts in-demand skills from job postings, stores them in a relational database, and visualizes the results in a live React dashboard.

![Job market pipeline dashboard](./<img width="868" height="627" alt="job-market-pipeline" src="https://github.com/user-attachments/assets/1656244c-d5b7-4cc1-abf5-2780e059a58f" />
)

## Overview

This project simulates a small-scale analytics tool: given a list of job postings, it identifies which technical skills each role requires, structures that data relationally, and surfaces it through an API-backed frontend with computed statistics (total jobs, most in-demand skill, and roles with no matched skills).

Built in three phases:

### Phase 1 — Data extraction (Python)
A Python script (`job_pipeline.py`) processes a dataset of job postings, each containing a title, company, and description. For every posting, it scans the description against a predefined list of technical skills (Python, SQL, React, JavaScript, TypeScript) and extracts which ones are mentioned.

### Phase 2 — Relational storage (SQLite)
The extracted data is stored in a SQLite database using two related tables:
- `jobs` — one row per job posting (`id`, `title`, `company`)
- `skills` — one row per matched skill, linked back to its job via `job_id`

This normalized structure avoids cramming multiple skills into a single field, and allows clean queries like "which jobs require Python."

### Phase 3 — API and frontend (Flask + React)
A lightweight Flask server (`server.py`) exposes two endpoints — `/api/jobs` and `/api/skills` — that query the SQLite database and return JSON. A React frontend (`job-dashboard/`) fetches from both endpoints, joins the data client-side by `job_id`, and renders:
- A stat row showing total jobs, most in-demand skill, and how many jobs have no matched skills
- A card for each job listing its title, company, and matched skill pills

## Tech stack

**Backend:** Python, Flask, SQLite, Flask-CORS
**Frontend:** React, Vite

## Running locally

**Backend**
```bash
cd job_pipeline
python3 job_pipeline.py   # builds and populates the database
python3 server.py         # starts the API on http://127.0.0.1:5000
```

**Frontend**
```bash
cd job_pipeline/job-dashboard
npm install
npm run dev                # starts the app on http://localhost:5173
```

## What I'd build next

- Swap the static job list for a live scrape or public API of real postings
- Add a chart visualizing skill frequency over time
- Deploy the backend and frontend so the dashboard is publicly viewable without running locally
