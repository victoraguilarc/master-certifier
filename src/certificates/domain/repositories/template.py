from abc import abstractmethod, ABC
from typing import Optional
from src.certificates.domain.models.template import Template


class TemplateRepository(ABC):
    @abstractmethod
    def find_template(self, id: str) -> Optional[Template]:
        raise NotImplementedError
