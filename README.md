# UserCraft — CRUD REST API

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-v3.0.0-000000?style=flat-square&logo=flask&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=flat-square&logo=uv&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A simple RESTful API built with **Flask** that implements full **CRUD** (Create, Read, Update, Delete) operations for managing user records, following REST conventions and proper HTTP status codes.

## Features

- ✅ Create a new user (`POST`)
- ✅ Retrieve a user by ID (`GET`)
- ✅ Update a user's information — partial or full update (`PUT`)
- ✅ Delete a user by ID (`DELETE`)
- ✅ Proper HTTP status codes (`200`, `400`, `404`)
- ✅ JSON request/response format
- ✅ Passwords are never exposed in API responses

## Tech Stack

- **Language:** Python 3.14
- **Framework:** Flask
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Data format:** JSON
- **Testing tool:** Postman
- **Containerization:** Docker & Docker Compose

## Project Structure

```
UserCraft/
├── crud.py              # Main application file (routes & logic)
├── pyproject.toml       # Project metadata & dependencies
├── uv.lock              # Locked dependency versions (managed by uv)
├── Dockerfile           # Container image definition
├── docker-compose.yml   # Container orchestration
├── .dockerignore        # Files excluded from the Docker build context
├── .gitignore
├── LICENSE
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.14 or higher
- [uv](https://docs.astral.sh/uv/) — used for dependency management and virtual environments
- (Optional) Docker & Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asalbaharlouie/UserCraft.git
   cd UserCraft
   ```

2. Install dependencies (uv reads `pyproject.toml` / `uv.lock` and automatically creates and manages the virtual environment):
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run crud.py
   ```

The API will be available at:
```
http://localhost:8000
```

### Running with Docker

Build and run directly:
```bash
docker build -t usercraft .
docker run -p 8000:8000 usercraft
```

Or with Docker Compose (recommended):
```bash
docker compose up --build
```

The API will be available at `http://localhost:8000` either way.

### Publishing the image to Docker Hub

```bash
# Log in to Docker Hub (only needed once per machine)
docker login

# Build the image, tagged with your Docker Hub username
docker build -t <your-dockerhub-username>/usercraft:latest .

# Push it to Docker Hub
docker push <your-dockerhub-username>/usercraft:latest
```

Once pushed, anyone can run the project without cloning the repo at all:
```bash
docker run -p 8000:8000 <your-dockerhub-username>/usercraft:latest
```

## API Endpoints

### 1. Create a User

```
POST /
```

**Request body:**
```json
{
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com",
    "password": "12345678"
}
```

**Success response — `200 OK`:**
```json
{
    "id": 1,
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

**Error response (missing/invalid fields) — `400 Bad Request`:**
```json
{
    "response": "bad request"
}
```

---

### 2. Get a User by ID

```
GET /<id>
```

**Example:**
```
GET /2
```

**Success response — `200 OK`:**
```json
{
    "id": 2,
    "name": "navid",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

> Note: The password field is never included in the response.

**Error response (user not found) — `404 Not Found`:**
```json
{
    "response": "Client does not exist"
}
```

---

### 3. Update a User

```
PUT /
```

Supports **partial updates** — only the fields included in the request body will be updated.

**Example — update only the name:**
```json
{
    "id": 2,
    "name": "reza"
}
```

**Example — update family and email:**
```json
{
    "id": 3,
    "family": "test",
    "email": "test@gmail.com"
}
```

**Success response — `200 OK`:**
```json
{
    "id": 2,
    "name": "reza",
    "family": "sadeghi",
    "email": "ns@gmail.com"
}
```

**Error response (user not found) — `404 Not Found`:**
```json
{
    "response": "Client does not exist"
}
```

---

### 4. Delete a User

```
DELETE /<id>
```

**Example:**
```
DELETE /3
```

**Success response — `200 OK`:**
```json
{
    "response": "User deleted successfully"
}
```

**Error response (user not found) — `404 Not Found`:**
```json
{
    "response": "Client does not exist"
}
```

## Testing with Postman

1. Open Postman and create a new request.
2. Set the request method (`GET`, `POST`, `PUT`, or `DELETE`) according to the endpoint.
3. Set the URL to `http://localhost:8000/...` as shown above.
4. For `POST` and `PUT` requests:
   - Go to the **Body** tab
   - Select **raw**
   - Set the format to **JSON**
   - Paste the request body as shown in the examples above
5. Click **Send** and check the response body and status code.

## Notes

- Data is currently stored **in memory** (a Python dictionary), meaning all records are lost when the server restarts. This is intentional for learning/testing purposes.
- HTTP does not define an official `UPDATE` method — this project uses `PUT` to handle updates, including partial updates.
- The app runs with Flask's `debug=True` for local development convenience. For a "production-style" Docker image, consider removing `debug=True` from `crud.py` before building, since Flask's debug reloader spawns an extra process that isn't needed (or well-behaved) inside a container.

## Author

**Asal Baharlouie**
Built as a learning project to practice REST API design, HTTP methods and status codes, and containerizing a Python application with Docker.

## License

This project is licensed under the [MIT License](LICENSE).
