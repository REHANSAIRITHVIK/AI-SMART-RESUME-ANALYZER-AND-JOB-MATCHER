# 🚀 AI Smart Resume Analyzer & Job Matcher

A full-stack intelligent web application that analyzes resumes using AI techniques and matches users with the most suitable job opportunities based on their skills.

---

## 🌟 Project Overview

The **AI Smart Resume Analyzer & Job Matcher** is designed to:

- 📄 Analyze resumes using AI-based skill extraction  
- 🎯 Match users with relevant job roles  
- 📊 Show match percentage for each job  
- 💰 Display salary and CTC details  
- 🏢 Showcase top companies and job openings  
- 📋 Track job applications  

This project simulates a **real-world job recommendation system** used by modern recruitment platforms.

---

## 🧠 Key Features

### 🔐 Authentication System
- User Registration & Login
- Secure password hashing
- Session-based authentication

### 📄 Resume Analyzer (AI)
- Upload resume files
- Extract skills automatically
- NLP-based parsing (extendable with spaCy)

### 🎯 Job Matching Engine
- Matches resume skills with job requirements
- Calculates match percentage
- Displays best-fit jobs

### 💼 Job Listings
- 20 predefined companies
- 20 job roles
- Salary & CTC information
- Vacancy details

### 🏢 Companies Section
- Displays top tech companies
- Includes logos, industry, and location

### 📋 Application Tracker
- Apply to jobs
- Track application status
- View applied roles

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Login

### 🔹 Frontend
- HTML5
- CSS3 (Glassmorphism + Gradient UI)
- JavaScript
- Bootstrap 5

### 🔹 Database
- SQLite

### 🔹 AI Components
- Skill Extraction Engine
- Job Matching Algorithm
- Salary Estimation Logic

---

## 📁 Project Structure

AI-SMART-RESUME-ANALYZER-AND-JOB-MATCHER/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│
│   ├── models/
│   │   ├── user.py
│   │   ├── company.py
│   │   ├── job.py
│   │   ├── application.py
│   │   ├── resume.py
│
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── dashboard_routes.py   ⭐ (MAIN LOGIC HERE)
│   │   ├── resume_routes.py
│   │   ├── job_routes.py
│   │   ├── application_routes.py
│
│   ├── services/   ⭐ (AI LOGIC)
│   │   ├── resume_parser.py
│   │   ├── job_matcher.py
│   │   ├── skill_extractor.py
│   │   ├── salary_estimator.py
│
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   ├── images/
│   │   │   ├── companies/   ⭐ (20 company logos)
│   │   │   │   ├── google.png
│   │   │   │   ├── amazon.png
│   │   │   │   ├── infosys.png
│   │   │   │   ├── tcs.png
│   │   │   │   ├── ...
│
│   ├── templates/
│   │   ├── layout.html
│   │   ├── dashboard.html   ⭐ (MOST IMPORTANT PAGE)
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── resume.html
│   │   ├── jobs.html
│   │   ├── applications.html
│   │   ├── companies.html
│
│
├── data/   ⭐ (STATIC DATA FOR 20 COMPANIES + JOBS)
│   ├── companies.json
│   ├── jobs.json
│
├── instance/
│   ├── database.db
│
├── uploads/   ⭐ (USER RESUMES STORED HERE)
│   ├── resumes/
│
├── run.py
├── requirements.txt
├── README.md
├── LICENSE.txt


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/REHANSAIRITHVIK/AI-SMART-RESUME-ANALYZER-AND-JOB-MATCHER.git
cd AI-SMART-RESUME-ANALYZER-AND-JOB-MATCHER

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate #windows

3 Install Dependencies
pip install -r requirements.txt

4 Run Application
python run.py

5 Open In Browser
http://127.0.0.1:5000

🧪 How It Works
User uploads resume
System extracts skills
AI matches jobs based on skills
Displays:
	Match %
	Salary & CTC
	Best job recommendations
	User applies → tracked in dashboard


🔥 Future Enhancements
Real NLP using spaCy
PDF/DOCX parsing
Deployment (AWS / Render)
Real-time job APIs
User-specific dashboards
Admin analytics panel


🎯 Use Cases
Students preparing for placements
Resume screening systems
Job recommendation platforms
Internship projects	

🔗 Live Demo

Check out the live application here: https://ai-smart-resume-analyzer-and-job-ma-six.vercel.app/


🧑‍💻 Developed By 

👨‍💻 DASIKA REHAN SAI RITHVIK

B.Sc. (Hons) in Computer Science – Nizam College Autonomous (Osmania University) 

Email: rehansairithvikdasika@gmail.com 

Mobile Number: 9581277713
