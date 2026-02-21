import os
import threading
from fastapi import APIRouter, HTTPException

from automation_api.core.config import get_settings
from automation_api.schemas.meroshare import (
    LoginTriggerResponse,
)
from automation_api.services.browser_manager import BrowserManager
from automation_api.services.meroshare.auth import MeroShareAuth

settings = get_settings()
router = APIRouter(prefix="", tags=["meroshare"])
login_lock = threading.Lock()


@router.post("/new-issues", response_model=LoginTriggerResponse)
def get_new_issues():
    acquired = login_lock.acquire(blocking=False)

    if not acquired:
        raise HTTPException(
            status_code=409,
            detail="Another login trigger is already running.",
        )

    manager = None
    try:
        default_headless = settings.meroshare_headless
        manager = BrowserManager(headless=default_headless)
        page = manager.start()

        auth = MeroShareAuth(page=page)
        auth.login()

        return LoginTriggerResponse(
            success=True,
            message="Meroshare login completed.",
            current_url=page.url,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail=f"Login trigger failed: {exc}"
        ) from exc
    finally:
        try:
            if manager:
                manager.close()
        finally:
            login_lock.release()
