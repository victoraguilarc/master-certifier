from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.certificates.domain.models.coordinate import Replacement
from src.routers.health_check_api import router as hc_router
from src.config import PROJECT_NAME, API_VERSION

# Declare the application
app = FastAPI(title=PROJECT_NAME, debug=False, version=API_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/health", description="Health check")
def health_check():
    return {"status": "OK"}


@app.post(path="/certificate", description="Generate a certificate")
def certificate(template_name: str, replacements: List[Replacement]):
    return {"status": "OK"}


app.include_router(hc_router)
