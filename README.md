# Python Basics

Small Python exercises and beginner FastAPI examples.

## Project contents

- `02_classactivity_request.py` fetches user data from JSONPlaceholder and prints each user's name, email, and city.
- `homework.py` exposes a sample invoice through a FastAPI endpoint.
- `Invoices.py` demonstrates creating, listing, updating, and deleting invoices with FastAPI.
- `fastapi_memory/step1_hello_api.py` is a minimal FastAPI app with a greeting endpoint.
- `requirements.txt` lists the project dependencies.

## Getting started

Use Python 3.10 or later. From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

To run the JSONPlaceholder exercise:

```powershell
python 02_classactivity_request.py
```

## Run the FastAPI examples

Start one example at a time from the project directory:

```powershell
uvicorn homework:app --reload
```

The `homework.py` example serves `GET /invoices`.

```powershell
uvicorn Invoices:app --reload
```

The `Invoices.py` example serves:

- `POST /invoices` to create an invoice
- `GET /all_invoices` to list invoices
- `PUT /update_invoice/{invoice_id}` to update an invoice
- `DELETE /delete_invoices/{invoice_id}` to delete an invoice

```powershell
uvicorn fastapi_memory.step1_hello_api:app --reload
```

The greeting example serves `GET /`.

For any running example, open <http://127.0.0.1:8000/docs> to try its endpoints in the interactive API documentation.
