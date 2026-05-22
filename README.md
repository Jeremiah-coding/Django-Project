# Django Project

This project is a Dockerized Django setup with three apps:

- departments
- courses
- students

## Requirements

- Docker Desktop
- Docker Compose

## Run with Docker

```bash
docker compose up --build
```

Open http://localhost:8000

## App Endpoints

- http://localhost:8000/departments/
- http://localhost:8000/courses/
- http://localhost:8000/students/

## Admin Access

- URL: http://localhost:8000/admin/
- Superuser username: admin
- Password: set locally when running createsuperuser (do not commit plaintext passwords)

To reset the admin password:

```bash
docker compose exec web python manage.py changepassword admin
```

## Stop

```bash
docker compose down
```
