from dataclasses import dataclass
from typing import Optional

from src.certificates.domain.exceptions import CertificateNotFoundError
from src.certificates.domain.models.certificate import Certificate
from src.certificates.domain.repositories.certificate import CertificateRepository


@dataclass
class CertificateDetailer(object):
    certificate_id: str
    certificate_repository: CertificateRepository

    def execute(self) -> Optional[Certificate]:
        certificate = self.certificate_repository.find_by_id(self.certificate_id)
        if not certificate:
            raise CertificateNotFoundError
        return certificate
