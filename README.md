# URL Shortener API

A backend REST API that shortens long URLs into short, shareable links — built with Django REST Framework, PostgreSQL, and Docker.

## Features

- **Custom User Model** — set up from project init, following Django best practices
- **Token Authentication** — secure API access via DRF tokens
- **Create & manage short links** — authenticated users see only their own links; anonymous users can still create links
- **Automatic redirect** — visiting a short link redirects to the original URL
- **Click tracking** — every redirect increments a click counter
- **Fully tested** — 5 automated tests covering auth, permissions, and core logic
- **Dockerized** — Django + PostgreSQL run together via Docker Compose, production-ready with gunicorn and whitenoise

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** DRF Token Authentication
- **Containerization:** Docker, Docker Compose
- **Production server:** Gunicorn
- **Static files:** Whitenoise

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

5. Visit `http://localhost:8000/links/` to use the API, or `http://localhost:8000/admin/` for the admin panel

## API Endpoints

| Method | Endpoint | Description | Auth required |
|--------|----------|--------------|----------------|
| GET | `/links/` | List your links | Yes |
| POST | `/links/` | Create a short link | No (optional) |
| GET | `/links/<id>/` | Retrieve a specific link | Yes |
| GET | `/<short_code>/` | Redirect to original URL | No |

## Running Tests

```bash
docker-compose exec web python manage.py test
```

## What I Learned

Building this project involved solving several real-world backend problems: setting up a custom user model correctly from project initialization, debugging token authentication issues in automated tests, migrating from SQLite to PostgreSQL (including handling Postgres 15+ schema permission changes), and properly securing credentials before containerizing with Docker (keeping secrets out of the built image entirely).