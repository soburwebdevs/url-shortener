# URL Shortener API

A backend REST API that shortens long URLs into short, shareable links — built with Django REST Framework, PostgreSQL, and Docker.

## Live Demo

🔗 [https://url-shortener-azca.onrender.com/](https://url-shortener-azca.onrender.com/)

*Note: hosted on Render's free tier — the app may take 30-60 seconds to wake up if it's been idle.*

## Features

- **Custom User Model** — set up from project init, following Django best practices
- **Registration & Login** — token-based auth for API clients (Postman, frontends) and session-based auth for browsing the API directly
- **Token Authentication** — secure API access via DRF tokens
- **Create & manage short links** — authenticated users see only their own links; anonymous users can still create links
- **Automatic redirect** — visiting a short link redirects to the original URL
- **Click tracking** — every redirect increments a click counter
- **Self-documenting API root** — visit the base URL to see all available endpoints
- **Fully tested** — automated tests covering auth, permissions, and core logic
- **Dockerized** — Django + PostgreSQL run together via Docker Compose, production-ready with gunicorn and whitenoise
- **Deployed on Render** — with automated migrations and superuser creation on every deploy

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** DRF Token Authentication + Session Authentication
- **Containerization:** Docker, Docker Compose
- **Production server:** Gunicorn
- **Static files:** Whitenoise
- **Deployment:** Render

## Getting Started

### Prerequisites
- Docker and Docker Compose installed

### Setup

1. Clone the repository
```bash
   git clone https://github.com/soburwebdevs/url-shortener.git
   cd url-shortener
```

2. Create a `.env` file in the project root (see `.env.example` for the required variables)

3. Build and run with Docker Compose
```bash
   docker-compose up --build
```

4. In a separate terminal, run migrations and create a superuser
```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
```

5. Visit `http://localhost:8000/` to see the API root, or `http://localhost:8000/admin/` for the admin panel

## API Endpoints

| Method | Endpoint | Description | Auth required |
|--------|----------|--------------|----------------|
| GET | `/` | API root — lists all available endpoints | No |
| POST | `/account/register/` | Register a new user | No |
| POST | `/account/login/` | Log in, receive an auth token | No |
| POST | `/account/logout/` | Log out (deletes the auth token) | Yes |
| GET | `/links/` | List your links | Yes |
| POST | `/links/` | Create a short link | No (optional) |
| GET | `/links/<id>/` | Retrieve a specific link | Yes |
| GET | `/<short_code>/` | Redirect to original URL | No |

## Running Tests

```bash
docker-compose exec web python manage.py test
```

## What I Learned

Building this project involved solving several real-world backend problems: setting up a custom user model correctly from project initialization, debugging token authentication issues in automated tests, migrating from SQLite to PostgreSQL (including handling Postgres 15+ schema permission changes), properly securing credentials before containerizing with Docker (keeping secrets out of the built image entirely), and deploying to a platform without shell access — which meant automating migrations and superuser creation directly into the container's startup process.