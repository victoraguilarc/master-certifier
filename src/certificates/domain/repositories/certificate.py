from abc import abstractmethod, ABC
from typing import List, Optional

from src.certificates.domain.models.certificate import Certificate


class CertificateRepository(ABC):
    @abstractmethod
    def find_by_id(self, instance_id: str) -> Optional[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def filter_by_category(self, category: str) -> List[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def filter_by_group(self, group: str) -> List[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def persist(self, instance: Certificate):
        raise NotImplementedError
