# Python API Testing Framework using Pytest and Requests

This project is a beginner-to-intermediate level API testing framework built using Python, Pytest, and Requests.

It demonstrates how to test REST APIs using real-world testing practices including positive and negative scenarios, response validation, reusable API clients, and pytest fixtures.

The project uses JSONPlaceholder, a mock REST API, for testing purposes.

#Tech Stack

- Python
- Pytest
- Requests
- Pytest-HTML

#Features

- GET API testing with response validation
- POST API testing with payload verification
- Reusable API client for cleaner code
- Pytest fixtures for test setup
- Positive and negative test scenarios
- Nested JSON validation
- Response time validation
- HTML test report generation

#Project Structure

python-api-testing-project/
├── tests/                # Test cases
│   ├── test_users_api.py
│   └── test_post_request.py
│
├── utils/                # Reusable API utilities
│   ├── api_client.py
│   └── config.py
│
├── conftest.py           # Pytest configuration
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── report.html           # Test report (generated)

#How to Run
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run tests:
   pytest -v
4. Generate HTML report:
   pytest --html=report.html

#Note:
Note: JSONPlaceholder is a mock API. POST, PUT, and DELETE requests do not persist data on the server. Tests validate response correctness but not data persistence.