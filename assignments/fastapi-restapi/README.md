# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small REST API using FastAPI to practice routing, request handling, and JSON responses.

## 📝 Tasks

### 🛠️ Create a basic API server

#### Description
Create a FastAPI application with at least two routes: a root (`/`) that returns a welcome message and `/items/{id}` that returns a JSON object for the requested `id`.

#### Requirements
- Implement the FastAPI app in `main.py`.
- Root route returns `{ "message": "Welcome to the FastAPI assignment" }`.
- `/items/{id}` returns `{ "id": <id>, "name": "Item <id>" }`.

### 🛠️ Add error handling (stretch)

#### Description
Add handling for non-integer ids and return an appropriate HTTP status code and error message.

#### Requirements
- Return HTTP 400 for invalid ids with a JSON error message.
