import sqlite3

jobs = [
    {"title": "Backend Engineer", "company": "Loop", "description": "Looking for Python and SQL experience"},
    {"title": "Frontend Developer", "company": "Acme", "description": "Must know React and JavaScript"},
    {"title": "Software Engineer", "company": "Braven", "description": "Foundational knowledge of full-stack development"},
    {"title": "Jr.Analytics Engineer", "company": "CIBC", "description": "Simplify stack, reduce technical debt, and improve developer experience"},
    {"title": "Data Science", "company": "AArete", "description": "Develop custom AI/ML models and algorithms to apply to data sets"},
    {"title": "Data Scienctist", "company": "Ulta Beauty", "description": "Proficiency in Python and scientific related frameworks"}
]

skills_to_find = ["Python", "SQL", "React", "JavaScript", "TypeScript"]

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM jobs")
cursor.execute("DELETE FROM skills")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        company TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY,
        job_id INTEGER,
        skill_name TEXT
    )
""")

for job in jobs:
    found_skills = []
    for skill in skills_to_find:
        if skill in job["description"]:
            found_skills.append(skill)
    print(f"{job["title"]} {job["company"]}")
    print(found_skills)
    cursor.execute("INSERT INTO jobs (title,company) VALUES (?,?)", (job["title"], job["company"]))
    job_id = cursor.lastrowid 
    for skill in found_skills:
        cursor.execute("INSERT INTO skills (job_id, skill_name) VALUES (?,?)", (job_id, skill))


conn.commit()

cursor.execute("SELECT * FROM skills")
print(cursor.fetchall())