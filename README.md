# Guide to the Project

This project is a basic analytics API built using FastAPI that exposes both public and protected endpoints. The focus of this task is on implementing API key authentication to securely protect sensitive analytics data.

## Task Requirements

- **Implement API Key Authentication:** Use FastAPI's dependency injection to secure the `/analytics/report` endpoint. Only clients with a valid API key should be able to access this data.
- **Standardized Responses:** Update and utilize Pydantic response models to ensure that both successful data and error responses are consistent and clearly structured.
- **Hardcoded API Keys:** Security is provided via a hardcoded list of valid API keys. Persistent storage, user management, or admin APIs for key management are *not* required and should not be added.
- **Error Handling:** When API key authentication fails, return an appropriate status code (`401 Unauthorized`) and a standardized error response model.
- **No Unnecessary Features:** Do **not** implement persistent storage, user registration, logging, or additional endpoints.

## Files Provided

- `main.py`: The FastAPI application, routes, and authentication logic.
- `models.py`: Pydantic response models for successful reports and error responses.
- `Dockerfile`, `install.sh`, `run.sh`: For environment provisioning and deployment.

## What You Need to Do

- Secure `/analytics/report` endpoint so it is only accessible with a valid API key from the provided list.
- Standardize both success and unauthorized error responses using the corresponding models in `models.py`.
- Use FastAPI dependency injection for API key validation. No persistent storage or complex user management.
- Update models and handlers as needed for clarity and maintainability. Only touch `main.py` and `models.py`.

## Verifying Your Solution

- Ensure requests to `/analytics/report` without a correct `x-api-key` header receive a `401` status code and the error response model.
- Requests with a valid API key from the list should receive a structured analytics report response.
- The API should not expose any sensitive information in error messages, only the error response model’s fields.
- Other endpoints (e.g., `/ping`) remain unprotected for demonstration.
