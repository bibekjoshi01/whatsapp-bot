import os
import threading

from fastapi import APIRouter, HTTPException

from automation_api.core.env import env_bool, require_env
from automation_api.schemas.meroshare import (
    LoginTriggerRequest,
    LoginTriggerResponse,
)

router = APIRouter(prefix="/trigger", tags=["meroshare"])
login_lock = threading.Lock()


@router.post("/login", response_model=LoginTriggerResponse)
def trigger_login(payload: LoginTriggerRequest):
    acquired = login_lock.acquire(blocking=False)
    if not acquired:
        raise HTTPException(
            status_code=409,
            detail="Another login trigger is already running.",
        )

    manager = None
    try:
        try:
            from automation_api.services.meroshare.auth import MeroShareAuth
            from automation_api.services.meroshare.browser_manager import BrowserManager
        except ModuleNotFoundError as exc:
            raise HTTPException(
                status_code=500,
                detail=(
                    "Missing Python dependency for automation. "
                    "Run: pip install -r requirements.txt"
                ),
            ) from exc

        username = require_env("MEROSHARE_USERNAME")
        password = require_env("MEROSHARE_PASSWORD")
        dp_id = os.getenv("MEROSHARE_DP_ID")

        default_headless = env_bool("MEROSHARE_HEADLESS", True)
        headless = payload.headless if payload.headless is not None else default_headless

        manager = BrowserManager(headless=headless)
        page = manager.start()

        auth = MeroShareAuth(page=page, timeout_ms=payload.timeout_ms)
        auth.login(username=username, password=password, dp_id=dp_id)

        saved_state = None
        if payload.save_session:
            saved_state = payload.state_path
            manager.save_session(path=saved_state)

        return LoginTriggerResponse(
            success=True,
            message="Meroshare login completed.",
            current_url=page.url,
            state_path=saved_state,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Login trigger failed: {exc}") from exc
    finally:
        try:
            if manager:
                manager.close()
        finally:
            login_lock.release()
