import uuid

import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from src.certificates.application.detailer import CertificateDetailer
from src.certificates.application.generator import CertificateGenerator
from src.certificates.application.presenters import CertificatePresenter
from src.certificates.infrastructure.repositories.dynamo_certificate import DynamoCertificateRepository
from src.certificates.infrastructure.repositories.dynamo_replacement import DynamoReplacementRepository
from src.certificates.infrastructure.repositories.dynamo_template import DynamoTemplateRepository
from src.common.environment import TEMPLATE_TABLE, REPLACEMENT_TABLE, CERTIFICATE_TABLE, CERTIFICATE_BUCKET
from src.common.infrastructure.s3_bucket import S3Bucket
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


class CertificateRequest(BaseModel):
    template_id: str
    group: str
    context: dict


@app.post(path="/certificate", description="Generate a certificate")
def certificate(request: CertificateRequest):
    dynamo_db = boto3.resource('dynamodb')
    s3_bucket = boto3.resource('s3')

    certificate_id = str(uuid.uuid4())

    use_case = CertificateGenerator(
        certificate_id=certificate_id,
        template_id=request.template_id,
        group=request.group,
        context=request.context,
        template_repository=DynamoTemplateRepository(table=dynamo_db.Table(TEMPLATE_TABLE)),
        replacement_repository=DynamoReplacementRepository(table=dynamo_db.Table(REPLACEMENT_TABLE)),
        certificate_repository=DynamoCertificateRepository(table=dynamo_db.Table(CERTIFICATE_TABLE)),
        certificate_bucket=S3Bucket(bucket=s3_bucket.Bucket(CERTIFICATE_BUCKET)),
    )
    instance = use_case.execute()

    return CertificatePresenter(instance).to_dict


@app.get(path="/certificate/{certificate_id}", description="Get a certificate")
def certificate(certificate_id: str):
    dynamo_db = boto3.resource('dynamodb')

    repository = DynamoCertificateRepository(table=dynamo_db.Table(CERTIFICATE_TABLE))

    instance = CertificateDetailer(
        certificate_id=certificate_id,
        certificate_repository=repository,
    ).execute()

    return CertificatePresenter(instance).to_dict


app.include_router(hc_router)
