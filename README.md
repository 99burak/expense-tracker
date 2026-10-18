# Expense Tracker API

A RESTful expense tracking API built with Python, FastAPI, SQLAlchemy, and SQLite. The application allows users to create, retrieve, update, delete, and filter expense records.

## Features

- Create new expenses
- List all expenses
- Retrieve an expense by ID
- Update existing expenses
- Delete expenses
- Filter expenses by name
- Validate request data with Pydantic
- Store expense records in an SQLite database
- Handle missing expense records with HTTP 404 responses

## Tech Stack

- **Python**
- **FastAPI** — REST API framework
- **SQLAlchemy** — ORM and database queries
- **SQLite** — Database
- **Pydantic** — Request and response validation
- **uv** — Python project and dependency management

## Requirements

- Python
- uv

## Installation

Clone the repository:

```bash
git clone https://github.com/99burak/expense-tracker.git
cd expense-tracker
```

Install dependencies:

```bash
uv sync
```

## Run the Application

```bash
uv run uvicorn app.app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | List all expenses |
| GET | `/expenses?name=market` | Filter expenses by name |
| GET | `/expenses/{id}` | Retrieve an expense by ID |
| PUT | `/expenses/{id}` | Update an expense |
| DELETE | `/expenses/{id}` | Delete an expense |

## Example Request

Create an expense using `POST /expenses`:

```json
{
  "name": "Groceries",
  "description": "Weekly grocery shopping",
  "date": "2026-10-18",
  "amount": 450.00
}
```

## Error Handling

The API returns HTTP `404 Not Found` when an expense with the requested ID does not exist.

## Project Structure

```text
expense-tracker/
├── app/
│   ├── app.py
│   ├── database.py
│   └── schemas.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Learning Goals

This project was built to practice:

- Designing RESTful API endpoints
- Implementing CRUD operations
- Working with SQLAlchemy and relational databases
- Validating data with Pydantic
- Using query and path parameters
- Handling HTTP errors
- Managing a Python project with uv

## License

This project is intended for educational and portfolio purposes.
