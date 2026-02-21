from typing import Optional

from pydantic import BaseModel


class LoginTriggerResponse(BaseModel):
    success: bool
    message: str
    current_url: Optional[str] = None


class NewIssueResponse(BaseModel):
    message: str
