import uuid

import boto3

from src.certificates.application.generator import CertificateGenerator
from src.certificates.infrastructure.repositories.dynamo_certificate import DynamoCertificateRepository
from src.certificates.infrastructure.repositories.dynamo_replacement import DynamoReplacementRepository
from src.certificates.infrastructure.repositories.dynamo_template import DynamoTemplateRepository
from src.common.environment import TEMPLATE_TABLE, REPLACEMENT_TABLE, CERTIFICATE_TABLE, CERTIFICATE_BUCKET
from src.common.infrastructure.s3_bucket import S3Bucket

template_repository = DynamoTemplateRepository(
    table=boto3.resource('dynamodb').Table(TEMPLATE_TABLE),
)
replacement_repository = DynamoReplacementRepository(
    table=boto3.resource('dynamodb').Table(REPLACEMENT_TABLE),
)
certificate_repository = DynamoCertificateRepository(
    table=boto3.resource('dynamodb').Table(CERTIFICATE_TABLE),
)
certificate_bucket = S3Bucket(
    bucket=boto3.resource('s3').Bucket(CERTIFICATE_BUCKET),
)

use_case = CertificateGenerator(
    template_id="cargas",
    group="cargas",
    context={
        "full_name": "Victor Aguilar",
    },
    certificate_id=str(uuid.uuid4()),
    template_repository=template_repository,
    replacement_repository=replacement_repository,
    certificate_repository=certificate_repository,
    certificate_bucket=certificate_bucket,
)

use_case.execute()