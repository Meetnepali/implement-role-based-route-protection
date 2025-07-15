from pydantic import BaseModel
from typing import List, Dict, Any

class AnalyticsReportResponse(BaseModel):
    report_name: str
    total_users: int
    data: List[Dict[str, Any]]

class ErrorResponse(BaseModel):
    error: str
    message: str
