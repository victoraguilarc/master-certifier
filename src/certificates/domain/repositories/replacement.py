from abc import abstractmethod, ABC
from typing import List, Optional
from src.certificates.domain.models.replacement import Replacement
from src.certificates.domain.models.replacement_collection import ReplacementCollection


class ReplacementRepository(ABC):
    @abstractmethod
    def filter_by_template(self, template_id: str) -> List[Replacement]:
        raise NotImplementedError

    @abstractmethod
    def get_collection(self, template_id: str) -> Optional[ReplacementCollection]:
        raise NotImplementedError
