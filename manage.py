import os

import uvicorn

from automation_api.core.env import env_bool

if __name__ == "__main__":
    host = os.getenv("SERVER_HOST", "0.0.0.0")
    port = int(os.getenv("SERVER_PORT", "8000"))
    reload_enabled = env_bool("SERVER_RELOAD", False)
    uvicorn.run("automation_api.main:app", host=host, port=port, reload=reload_enabled)
