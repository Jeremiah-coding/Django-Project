# Django Project

University Course Directory built with Django MVT, Docker, and PostgreSQL.

## Project Structure

- `university_portal/`
- `departments/`
- `courses/`
- `students/`
- `templates/`

## Requirements

- Docker Desktop
- Docker Compose

## How To Run The Project

```bash
docker compose up --build -d
```

Open:

- http://localhost:8000/

To stop:

```bash
docker compose down
```

## How To Create Migrations

```bash
docker compose exec web python manage.py makemigrations
```

## How To Migrate The Database

```bash
docker compose exec web python manage.py migrate
```

## How To Create A Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

Non-interactive example:

```bash
docker compose exec web python manage.py createsuperuser --noinput --username admin --email admin@example.com
```

## Available Pages

- Home page: `http://localhost:8000/`
- Department list: `http://localhost:8000/departments/`
- Department detail: `http://localhost:8000/departments/<department_id>/`
- Course detail: `http://localhost:8000/courses/<course_id>/`
- Admin panel: `http://localhost:8000/admin/`

Note: `http://localhost:8000/courses/` resolves into course detail flow in this strict guideline setup.

## Admin Access Note

- Username used in this project: `admin`
- Keep passwords local only. Do not commit real secrets to Git.
