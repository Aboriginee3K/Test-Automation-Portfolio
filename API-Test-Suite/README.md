# REST API Test Suite

# Overview
Automated API testing suite for ReqRes.in(https://reqres.in/), demonstrating how to validate RESTful services using Python.

This project focuses on the "backend" side of QA, ensuring that data is correctly retrieved (GET), created (POST), and that appropriate HTTP status codes (200, 201, 404) are returned.

# Tech Stack
* Python 3
* Requests
* Pytest
* JSON

# Test Scenarios
1. GET /users/2: Verify successful data retrieval and JSON structure.
2. POST /users: Verify creating a new resource and checking response payload.
3. GET /users/999: Verify error handling (404 Not Found).

# How to Run
1. Install dependencies:
   pip install -r requirements.txt’‘’

2. Run tests:
   ‘’‘pytest -v -s’‘’