from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
from models import AnalyticsReportResponse, ErrorResponse

# Hardcoded valid API keys (in practice, use persistent storage)
VALID_API_KEYS = [
    "12345-analytics-key",
    "67890-analytics-key"
]

app = FastAPI()

# Unprotected endpoint (placeholder for demonstration)
@app.get("/ping")
def ping():
    return {"message": "pong"}


def api_key_auth(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key is None or api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return api_key


@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                error="Unauthorized",
                message=exc.detail
            ).dict(),
        )
    # fall back to default
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


@app.get("/analytics/report", response_model=AnalyticsReportResponse, responses={
    401: {"model": ErrorResponse}
})
def get_analytics_report(api_key: str = Depends(api_key_auth)):
    # Dummy analytics data
    return AnalyticsReportResponse(
        report_name="Active Users Last 24h",
        total_users=357,
        data=[{"hour": i, "active_users": 10 + i%7} for i in range(24)]
    )
