## NeuroKids Physio Studio – FastAPI Website

This project is a small marketing website for **NeuroKids Physio Studio**, the online neuro and pediatric physiotherapy practice of **Aklima Munaf Shaikh, PT**.

It is built with **FastAPI**, **Jinja2 templates**, and a custom responsive design focused on clarity and warmth for parents and neuro rehab patients.

---

## Features

- **Hero section** introducing Neuro & Pediatric physiotherapy services.
- **About section** describing Aklima’s background and treatment philosophy.
- **Conditions treated** highlighting neuro and pediatric focus (stroke, cerebral palsy, developmental delay, etc.).
- **Services** cards for pain relief, post‑surgery, neurological, and pediatric physiotherapy.
- **Patient testimonials** including neuro and pediatric success stories.
- **Contact form** to request an online consultation (name, phone, email, concern).
- **Responsive layout** with a light purple theme and custom logo.

---

## Tech Stack

- **Backend**: FastAPI (Python)
- **Templates**: Jinja2
- **Server**: Uvicorn (ASGI)
- **Styling**: Custom CSS (no frontend framework)

Project structure (simplified):

- `main.py` – FastAPI app, routing, template rendering.
- `templates/base.html` – shared layout, header, footer.
- `templates/index.html` – main landing page content.
- `static/css/style.css` – typography, layout, color theme, and components.
- `pyproject.toml` / `requirements.txt` – Python dependencies.

---

## Running Locally

1. **Clone the repo**

	```bash
	git clone <your-repo-url>
	cd Aklima_Website
	```

2. **Create a virtual environment (using uv)**

	```bash
	uv venv --python 3.12
	source .venv/bin/activate
	```

3. **Install dependencies**

	With `uv`:

	```bash
	uv pip install -r requirements.txt
	```

	Or with plain `pip`:

	```bash
	pip install -r requirements.txt
	```

4. **Run the development server**

	```bash
	uvicorn main:app --reload
	```

5. **Open the site**

	Visit: http://127.0.0.1:8000

---

## Deployment (Render example)

1. Push this project to GitHub (or GitLab/Bitbucket).
2. Create a **Web Service** on [Render](https://render.com):
	- **Build Command**: `pip install -r requirements.txt`
	- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. After the first deploy, Render will give you a public URL for the site.

The app reads the `PORT` environment variable in `main.py`, so it should work out of the box on most Python hosting platforms.

---

## Customizing

- **Text & copy**: edit `templates/index.html` for headings, sections, and testimonials.
- **Colors & layout**: edit `static/css/style.css` (light purple palette, spacing, and responsive rules).
- **Contact email**: update the address in `templates/base.html` and `templates/index.html`.

This setup is intentionally simple so you can easily evolve it as the practice grows (e.g., add a blog, FAQs, or more pages).
