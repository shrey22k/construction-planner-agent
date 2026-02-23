# Construction Planning Assistant Agent  
Agentic AI | Project No: AAI-38 | Group 03D8

An AI-driven construction planning system that converts a high-level construction goal into an optimized execution plan by autonomously handling task decomposition, dependency management, scheduling, risk analysis, and visualization.

---

## Project Overview

Construction project planning is complex due to multiple interdependent tasks, limited resources, time constraints, and risks.  
Manual planning is often error-prone and inefficient.

The Construction Planning Assistant Agent addresses this by:
- Accepting a single high-level construction goal
- Automatically generating a structured and optimized construction plan
- Providing risk insights and visual timelines through a web interface

---

## Objectives

- Decompose high-level construction goals into actionable tasks  
- Detect and manage task dependencies  
- Validate resource availability  
- Estimate time and cost  
- Optimize task execution order  
- Analyze project risks  
- Visualize the construction schedule using a Gantt chart  

---

## System Architecture (High Level)

The system follows a Client–Server architecture with a multi-agent AI planning layer.

### Architecture Layers
- Frontend Layer  
  - HTML, CSS, JavaScript  
  - Collects user input and displays results  

- Backend Layer  
  - Python and Flask  
  - Orchestrates the planning workflow via REST APIs  

- AI Planning Layer  
  - Planner Agent  
  - Dependency Analyzer  
  - Resource Validator  
  - Cost and Time Estimator  
  - Scheduler  
  - Risk Manager  
  - Gantt Chart Generator  

The backend is stateless, ensuring scalability and simplicity.

---

## Workflow Summary

1. User enters a construction goal via the web interface  
2. Goal is sent to the backend using a REST API  
3. Planner Agent decomposes the goal into tasks  
4. Dependency Analyzer builds a DAG  
5. Resource Agent validates availability  
6. Cost and Time Estimator computes estimates  
7. Scheduler optimizes task order  
8. Risk Manager evaluates delays  
9. Gantt chart is generated  
10. Final plan is returned to the UI  

---

## Core Components

| Component | Description |
|---------|------------|
| Planner Agent | Breaks goal into tasks |
| Dependency Graph | Builds task dependency DAG |
| Resource Agent | Validates resource availability |
| Cost Estimator | Estimates time and cost |
| Scheduler Agent | Optimizes task execution order |
| Risk Manager | Identifies and manages risks |
| Gantt Generator | Visualizes the schedule |
| Web UI | Displays system output |

---

## Features

- AI-based task decomposition  
- Resource validation (mocked for academic use)  
- Time and cost estimation  
- Risk analysis with mitigation suggestions  
- Gantt chart visualization  
- Web-based user interface  

---

## Data Handling

- In-memory structured data  
- JSON-based API communication  
- No external database dependency  
- Session-level data retention only  

---

## Security and Performance

### Security
- Controlled API access using CORS  
- No authentication (academic demonstration)  
- No sensitive data storage  

### Performance
- Lightweight REST APIs  
- Typical response time under two seconds  

---

## Technologies Used

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- Flask  

### AI and Planning
- Groq LLM for task decomposition  
- Rule-based fallback planner  

### Visualization
- Python-based Gantt chart generation  

---

## How to Run the Project

```bash
git clone <your-repository-url>
cd backend
pip install -r requirements.txt
python app.py
