import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [jobs, setJobs] = useState([]);
  const [skills, setSkills] = useState([]);
  const noSkillsCount = jobs.filter(job => skills.filter(skill => skill[1] === job[0]).length === 0).length;

  const skillCounts = {};
    skills.forEach(skill => {
      const name = skill[2];
      skillCounts[name] = (skillCounts[name] || 0) + 1;
  });

  const topSkill = Object.entries(skillCounts).reduce((max, entry) => entry[1] > max[1] ? entry : max, ["", 0]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/jobs")
      .then(response => response.json())
      .then(data => setJobs(data));
    fetch("http://127.0.0.1:5000/api/skills")
      .then(response => response.json())
      .then(data => setSkills(data));
  }, []);

  return (
    <div className="dashboard">
      <h1>Job market pipeline 💼</h1>
      <p className= "subtitle">Tracking {jobs.length} roles across Chicago tech 🏙️</p>

    <div className="stats">
      <div className="stat-card">
        <p className="stat-label">Total jobs</p>
        <p className="stat-value">{jobs.length}</p>
      </div>
      <div className="stat-card">
        <p className="stat-label">No skills matched</p>
        <p className="stat-value">{noSkillsCount} of {jobs.length}</p>
      </div>
      <div className="stat-card">
        <p className="stat-label">Top skill</p>
        <p className="stat-value">{topSkill[0]}</p>
      </div>
    </div>

    <div className="job-list">
    {jobs.map(job => (
      <div className="job-card" key={job[0]}>
        <div>
          <p className="job-title">{job[1]}</p>
          <p className="job-company">{job[2]}</p>
        </div>
        <div className="skills">
          {skills.filter(skill => skill[1] === job[0]).map(skill => (
            <span className="skill-pill" key={skill[0]}>{skill[2]}</span>
          ))}
        </div>
      </div>
        ))}
   </div>
  </div>
  )
}

export default App
