from dataclasses import dataclass
from typing import List

from src.certificates.domain.models.certificate import Certificate
from src.certificates.domain.models.coordinate import Replacement
from src.certificates.domain.repositories.certificate import CertificateRepository
from src.certificates.domain.repositories.coordinate import CoordinateRepository
from src.common.domain.interfaces.bucket import Bucket


@dataclass
class CertificateGenerator(object):
    template: str
    replacements: List[Replacement]
    coordinate_repository: CoordinateRepository
    certificate_repository: CertificateRepository
    certificate_bucket: Bucket

    def execute(self) -> Certificate:
        # Get coordinates by template
        # Validate if each coordinate has a value.
        # Get document template
        # Replace the coordinates in the template with the values.
        # Build and store the certificate in S3 and dynamodb
        # Return the certificate
        pass
