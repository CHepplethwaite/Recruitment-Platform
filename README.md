---
![Status](https://img.shields.io/badge/Status-In%20Development-yellow) 

# Django Recruitement Platform

A modern, production-ready **recruitment platform built with Django**.
It enables employers to post job listings, candidates to apply, and recruiters to manage talent pipelines.
The platform includes user profiles, application workflow, authentication, and scalable backend architecture.

---

## 🚀 Features

### 🔹 Candidates

* Create and update profile
* Upload CV / resume
* Browse job listings
* Save jobs for later
* Apply directly from dashboard

### 🔹 Employers / Recruiters

* Post and manage job listings
* View applicants
* Shortlist candidates
* Control job visibility and status

### 🔹 Core System

* Secure authentication (registration, login, logout)
* Role-based access (employer vs applicant)
* Search and filter jobs by category, location, type
* Responsive frontend for mobile and desktop

---

## 🏗️ Tech Stack

* **Backend:** Django
* **Frontend:** Django Templates (or specify React/Angular if applicable)
* **Database:** PostgreSQL (recommended) or SQLite (development)
* **Storage:** Django file storage for resumes
* **Authentication:** Django auth system
* **Deployment Ready:** Gunicorn / Nginx (production)

---

## 📦 Project Structure

```
project/
├── core/             # Settings, URLs, global config
├── jobs/             # Job listings & search
├── accounts/         # Authentication and user roles
├── profiles/         # Candidate and employer profiles
├── applications/     # Application workflow
├── static/           # Frontend assets
├── templates/        # UI templates
└── manage.py
```

---

## 🔐 Roles

### Candidate

* Create a professional profile
* Manage resume
* Browse and apply for jobs
* Track applications

### Employer

* Create company profile
* Post jobs
* Manage listings
* Review applicants

---

## 📊 Roadmap

* [ ] Resume parsing or CV AI matching
* [ ] Email notifications
* [ ] Application status tracking (accepted / rejected / interview)
* [ ] Job scraping from external portals
* [ ] Recruiter analytics dashboard
* [ ] Company branding pages
* [ ] API endpoints for mobile apps

---

## 🤝 Contributions

PRs and feature suggestions are welcome.
Please open an issue before submitting major changes.

---



