from typing import Optional

from pydantic import BaseModel, Field


class LoginTriggerRequest(BaseModel):
    headless: Optional[bool] = None
    save_session: bool = True
    state_path: str = "state.json"
    timeout_ms: int = Field(default=45000, ge=5000, le=180000)


class LoginTriggerResponse(BaseModel):
    success: bool
    message: str
    current_url: Optional[str] = None
    state_path: Optional[str] = None
