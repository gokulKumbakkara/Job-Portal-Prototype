# FastAPI Job Portal Prototype

*A prototype Job Portal API built with FastAPI, created while following a Udemy course on FastAPI.*

It demonstrates how to build a backend for a job portal with CRUD operations, authentication, and database integration.

## Features

- User registration & authentication using JSON Web Tokens (JWT)
- Create, read, update, and delete job listings with validation using Pydantic
- Search and filter jobs by various criteria such as job title, location, and category
- Database integration with support for both SQLite and PostgreSQL using SQLAlchemy
- Built with **FastAPI** for speed and efficiency, served using the Uvicorn ASGI server

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy |
| Database | SQLite / PostgreSQL (`psycopg2`) |
| ASGI server | Uvicorn |
| Auth | JWT (`python-jose`), Passlib[bcrypt] |
| Templating | Jinja2 |
| Config | python-dotenv |
| Testing | pytest, requests |

Dependencies are declared in `backend/requirements.txt`.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gokulKumbakkara/Job-Portal-Prototype.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Job-Portal-Prototype
   ```
3. Install the required dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Create a database using either SQLite or PostgreSQL, and update the `database.ini` file accordingly

## Usage

1. Navigate to the project directory: `cd Job-Portal-Prototype`
2. Activate the virtual environment (if using one): `source venv/bin/activate`
3. Run the application:
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```
4. Access the API documentation at `http://localhost:8000/docs`

## Project Structure

- `backend/` — backend code directory
  - `main.py` — FastAPI application entry point
  - `apis/` — API route definitions
  - `core/` — core configuration and utilities
  - `db/` — database setup and session management
  - `schemas/` — Pydantic schema definitions
  - `webapps/` — web-facing templates/handlers
  - `tests/` — automated tests
  - `requirements.txt` — dependency requirements file

## Contributing

To contribute to the project, follow these steps:
1. Fork the repository using the GitHub web interface
2. Clone the forked repository
3. Create a new branch: `git branch feature/your-feature`
4. Make changes to the code and commit them: `git commit -m "Your commit message"`
5. Push the changes to your forked repository: `git push origin feature/your-feature`
6. Create a pull request to merge your changes into the main repository
