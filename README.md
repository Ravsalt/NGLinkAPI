# NGLinkAPI

NGLinkAPI is a Python library that allows you to interact with the NGL (Not Gonna Lie) API to submit questions and receive responses. It is designed to be simple and easy to integrate into web applications using Flask.

## Features

- Interact with the NGL API for submitting questions via POST requests.
- Flask application to handle submissions.
- Logging for tracking requests and responses.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.6 or higher
- `pip` for managing Python dependencies

## Installation

### Clone the Repository

Clone the repository to your local machine:

```bash
#Clone The repo
git clone https://github.com/ravsalt/NGLinkAPI.git

cd NGLinkAPI

python app.py
# running the app
```

### API Usage

## Base URL

All API requests should be made to the following base URL:

https://localhost:5000/api/submit

Endpoint: /api/submit

This endpoint allows you to submit a question to the NGL API.
Method: POST
Request Parameters:

    username (required): The username of the person submitting the question.
    question (required): The question being submitted.
    deviceId (required): The unique identifier for the device (e.g., UUID).
    gameSlug (optional): The game slug (can be left empty).
    referrer (optional): The referrer information (can be left empty).

Example Request:

```bash
curl -X POST https://<your-deployed-domain-or-ip>/api/submit \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=test_user&question=What is Flask?&deviceId=1234abcd&gameSlug=game_example&referrer=test_referrer"
```