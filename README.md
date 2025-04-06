# My Django First Project

My idea is implementing Django-based Identity and Access Management (IAM) system that handles user authentication and authorization.

## Features

- User Registration
- User Authentication
- User Management
- Role-based Access Control

## Prerequisites

- Python 3.8+
- PostgreSQL
- pipenv

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd django-first-project
```

2. Install dependencies using pipenv

```bash
pipenv install
```

3. Activate the virtual environment

```bash
pipenv shell
```

4. Set up the environment variables

```bash
cp .env.example .env
```

5. Run migrations

```bash
pipenv run python manage.py migrate
```

6. Run the development server

```bash
pip env python manage.py runserver
```

## API Endpoints

### User Management

- POST /api/iam/user/register - Register new user
- GET /api/iam/user/{id} - Get user details
- GET /api/iam/users - List users

## Development

### Project Structure

```plaintext
django-iam-app/
├── apps/
│   └── iam/
│       ├── models/
│       ├── services/
│       ├── repositories/
│       ├── serializers/
│       ├── views/
│       └── middlewares/
├── config/
└── manage.py
```
