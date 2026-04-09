# 💼 FastAPI Job Portal Prototype
This project is a **prototype Job Portal API** built with **FastAPI**, created while following a Udemy course on FastAPI. It demonstrates how to build a backend for a job portal with **CRUD operations**, authentication, and database integration.

## 🚀 Features
- 👤 User registration & authentication using JSON Web Tokens (JWT)
- 📝 Create, read, update, and delete job listings with validation using Pydantic
- 🔍 Search and filter jobs by various criteria such as job title, location, and category
- 💾 Database integration with support for both SQLite and PostgreSQL using SQLAlchemy
- ⚡ Built with **FastAPI** for speed and efficiency, and served using Uvicorn ASGI server

## 🛠️ Tech Stack
- **FastAPI**: Web framework for building the API
- **Pydantic**: Data validation library for ensuring data consistency
- **SQLAlchemy**: Object-Relational Mapping (ORM) tool for database handling
- **SQLite / PostgreSQL**: Database backends for storing and retrieving data
- **Uvicorn**: ASGI server for serving the FastAPI application

## 📦 Installation
To install the project, follow these steps:
1. Clone the repository using `git clone https://github.com/your-username/Job-Portal-Prototype.git`
2. Navigate to the project directory using `cd Job-Portal-Prototype`
3. Install the required dependencies using `pip install -r backend/requirements.txt`
4. Create a database using either SQLite or PostgreSQL, and update the `database.ini` file accordingly

## 🚀 Usage
To run the project, follow these steps:
1. Navigate to the project directory using `cd Job-Portal-Prototype`
2. Activate the virtual environment using `source venv/bin/activate` (if using a virtual environment)
3. Run the application using `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
4. Access the API documentation using `http://localhost:8000/docs`

## 🗂️ Folder Structure
The project follows a simple folder structure:
- `README.md`: Project README file
- `backend`: Backend code directory
  - `main.py`: FastAPI application entry point
  - `models`: Database model definitions
  - `routes`: API route definitions
  - `schemas`: Pydantic schema definitions
  - `utils`: Utility functions
  - `requirements.txt`: Dependency requirements file

## 🤝 Contributing
To contribute to the project, follow these steps:
1. Fork the repository using the GitHub web interface
2. Clone the forked repository using `git clone https://github.com/your-username/Job-Portal-Prototype.git`
3. Create a new branch using `git branch feature/your-feature`
4. Make changes to the code and commit them using `git commit -m "Your commit message"`
5. Push the changes to your forked repository using `git push origin feature/your-feature`
6. Create a pull request using the GitHub web interface to merge your changes into the main repository