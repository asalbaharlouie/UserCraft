# UserCraft — CRUD REST API

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-v3.0.0-000000?style=flat-square&logo=flask&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=flat-square&logo=uv&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A simple RESTful API built with **Flask** that implements full **CRUD** (Create, Read, Update, Delete) operations for managing user records, following REST conventions and HTTP status codes.

The project is also containerized with **Docker** and uses **Gunicorn** to run the Flask application in a production-style container environment.

It also includes a **CI/CD pipeline with GitHub Actions** that automatically tests, builds, publishes, and deploys the application.

---

## Features

- ✅ Create a new user (`POST`)
- ✅ Retrieve a user by ID (`GET`)
- ✅ Update a user's information — partial or full update (`PUT`)
- ✅ Delete a user by ID (`DELETE`)
- ✅ Proper HTTP status codes (`200`, `400`, `404`)
- ✅ JSON request/response format
- ✅ Passwords are never exposed in API responses
- ✅ Automated tests with `pytest`
- ✅ Dockerized application
- ✅ Gunicorn for running Flask in the container
- ✅ Docker Compose for container management
- ✅ Docker Hub image publishing
- ✅ Automated CI/CD with GitHub Actions
- ✅ Automatic deployment to a remote Linux server

---

## Tech Stack

- **Language:** Python 3.14
- **Framework:** Flask
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Testing:** pytest
- **Data format:** JSON
- **Testing tool:** Postman
- **Application server:** Gunicorn
- **Containerization:** Docker
- **Container orchestration:** Docker Compose
- **Container registry:** Docker Hub
- **CI/CD:** GitHub Actions
- **Server:** Ubuntu Linux

---

## Architecture

The application follows this general deployment flow:

```text
Developer
   │
   │ git push
   ↓
GitHub
   │
   ↓
GitHub Actions
   │
   ├── Run tests
   │
   ├── Build Docker image
   │
   ├── Push image to Docker Hub
   │
   └── SSH into server
          │
          ↓
       Docker Compose
          │
          ↓
      Docker Container
          │
          ↓
       Gunicorn
          │
          ↓
        Flask
```

For an API request from Postman:

```text
Postman
   │
   ↓
Internet
   │
   ↓
Linux Server
   │
   ↓
Docker Container
   │
   ↓
Gunicorn
   │
   ↓
Flask Application
```

---

## Project Structure

```text
UserCraft/
├── crud.py                 # Main application file (routes & logic)
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # Locked dependency versions
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Container configuration
├── .dockerignore           # Files excluded from Docker build context
├── .gitignore
├── LICENSE
├── README.md               # Project documentation
└── .github/
    └── workflows/
        ├── ci.yml          # Automated tests
        └── docker.yml      # Build, push and deploy pipeline
```

---

# Getting Started

## Prerequisites

- Python 3.14 or higher
- [uv](https://docs.astral.sh/uv/) — used for dependency management and virtual environments
- Git
- (Optional) Docker & Docker Compose
- (Optional) Postman for API testing

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/asalbaharlouie/UserCraft.git
cd UserCraft
```

2. Install dependencies:

```bash
uv sync
```

`uv` reads `pyproject.toml` and `uv.lock` and creates/manages the project's virtual environment.

3. Run the application locally:

```bash
uv run crud.py
```

The API will be available at:

```text
http://localhost:8000
```

---

# Running with Docker

## Build and Run Directly

Build the Docker image:

```bash
docker build -t usercraft .
```

Run the container:

```bash
docker run -p 8000:8000 usercraft
```

The API will be available at:

```text
http://localhost:8000
```

---

## Running with Docker Compose

Start the application with:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

Docker Compose can also be used on the deployment server to pull and run the published image from Docker Hub.

---

# Docker Image

The application image is published to Docker Hub:

```text
asalbaharlouie/usercraft
```

You can pull the image with:

```bash
docker pull asalbaharlouie/usercraft:latest
```

Or run it directly:

```bash
docker run -p 8000:8000 asalbaharlouie/usercraft:latest
```

This allows the application to be run without cloning the GitHub repository.

---

# Publishing the Image to Docker Hub

Log in to Docker Hub:

```bash
docker login
```

Build the image:

```bash
docker build -t asalbaharlouie/usercraft:latest .
```

Push the image:

```bash
docker push asalbaharlouie/usercraft:latest
```

The image can then be pulled from Docker Hub by the deployment server or any other machine.

---

# CI/CD Pipeline

The project uses **GitHub Actions** to automate testing, Docker image building, publishing, and deployment.

The general pipeline is:

```text
git push
   ↓
GitHub Actions
   ↓
Run tests
   ↓
Build Docker image
   ↓
Push image to Docker Hub
   ↓
SSH into deployment server
   ↓
docker compose pull
   ↓
docker compose up -d
```

This means that after pushing changes to the `main` branch, the application can be automatically updated on the remote server.

### CI

The CI workflow runs the automated tests using `pytest`.

```text
Code
 ↓
GitHub Actions
 ↓
Install dependencies
 ↓
Run pytest
```

### CD

The deployment workflow:

1. Builds the Docker image.
2. Pushes the image to Docker Hub.
3. Connects to the server through SSH.
4. Pulls the latest Docker image.
5. Restarts the application using Docker Compose.

```text
GitHub
   ↓
Docker Build
   ↓
Docker Hub
   ↓
Remote Server
   ↓
Docker Compose
   ↓
Updated Application
```

---

# API Endpoints

## 1. Create a User

```text
POST /users
```

### Request Body

```json
{
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com",
    "password": "12345678"
}
```

### Success Response — `200 OK`

```json
{
    "id": 1,
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

### Error Response — `400 Bad Request`

```json
{
    "response": "bad request"
}
```

---

## 2. Get a User by ID

```text
GET /<id>
```

### Example

```text
GET /2
```

### Success Response — `200 OK`

```json
{
    "id": 2,
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

> Note: The password field is never included in the response.

### Error Response — `404 Not Found`

```json
{
    "response": "Client does not exist"
}
```

---

## 3. Update a User

```text
PUT /
```

The endpoint supports partial updates. Only the fields included in the request body are updated.

### Example — Update Only the Name

```json
{
    "id": 2,
    "name": "reza"
}
```

### Example — Update Family and Email

```json
{
    "id": 3,
    "family": "test",
    "email": "test@gmail.com"
}
```

### Success Response — `200 OK`

```json
{
    "id": 2,
    "name": "reza",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

### Error Response — `404 Not Found`

```json
{
    "response": "Client does not exist"
}
```

---

## 4. Delete a User

```text
DELETE /<id>
```

### Example

```text
DELETE /3
```

### Success Response — `200 OK`

```json
{
    "response": "User deleted successfully"
}
```

### Error Response — `404 Not Found`

```json
{
    "response": "Client does not exist"
}
```

---

# Testing with Postman

Postman can be used to manually test the API.

## Local Testing

When running the application locally, use:

```text
http://localhost:8000
```

For example:

```text
GET http://localhost:8000/1
```

or:

```text
POST http://localhost:8000/users
```

For `POST` and `PUT` requests:

1. Open Postman.
2. Select the appropriate HTTP method.
3. Enter the API URL.
4. Go to **Body**.
5. Select **raw**.
6. Select **JSON**.
7. Enter the request body.
8. Click **Send**.
9. Check the response body and HTTP status code.

---

# Testing the Deployed Server

After deployment, the API can also be accessed through the remote server.

Example:

```text
http://<SERVER_IP>:8000
```

For example:

```text
http://52.59.219.107:8000
```

A request then follows this path:

```text
Postman
   ↓
Internet
   ↓
Server
   ↓
Docker
   ↓
Gunicorn
   ↓
Flask
```

This allows the same API to be tested remotely instead of only through `localhost`.

---

# Docker and Gunicorn

The Docker image uses Gunicorn to run the Flask application.

The Dockerfile contains:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "crud:app"]
```

This means Gunicorn runs the Flask application defined as:

```text
crud:app
```

where:

- `crud` refers to `crud.py`
- `app` refers to the Flask application object

The application listens on port `8000`.

---

# Deployment Server

The application is deployed to a remote Ubuntu Linux server.

The server runs:

```text
Docker
   ↓
Docker Compose
   ↓
UserCraft Container
   ↓
Gunicorn
   ↓
Flask
```

The deployment server does not need the source code repository to run the application.

Instead, Docker Compose pulls the published image from Docker Hub:

```bash
docker compose pull
```

and starts the updated container:

```bash
docker compose up -d
```

---

# Notes

- Data is currently stored **in memory** using a Python dictionary.
- All records are lost when the application restarts.
- This behavior is intentional for learning and testing purposes.
- The project currently does not use a database.
- Passwords are not returned in API responses.
- The application uses `PUT` for update operations, including partial updates.
- Gunicorn is used to run the Flask application inside the Docker container.
- The Docker image is published to Docker Hub.
- GitHub Actions is used to automate testing, image building, publishing, and deployment.

---

# Future Improvements

Possible future improvements include:

- Add a database such as PostgreSQL
- Hash passwords instead of storing them directly
- Add authentication and authorization
- Improve API validation
- Add more comprehensive automated tests
- Add API documentation with OpenAPI/Swagger
- Add Nginx as a reverse proxy
- Enable HTTPS/TLS
- Use a domain name
- Improve production logging
- Add health checks
- Use versioned Docker image tags instead of only `latest`
- Improve deployment security
- Add monitoring and observability

---

# Learning Goals

This project was built as a hands-on learning project to practice:

- REST API development
- Flask
- HTTP methods and status codes
- JSON APIs
- API testing with Postman
- Python dependency management with `uv`
- Docker
- Docker Compose
- Gunicorn
- Docker Hub
- Linux server administration
- SSH
- GitHub Actions
- CI/CD
- Automated deployment

---

# Author

**Asal Baharlouie**

Built as a learning project to practice REST API development, HTTP concepts, containerization, CI/CD, and automated deployment.

---

# License

This project is licensed under the [MIT License](LICENSE).
