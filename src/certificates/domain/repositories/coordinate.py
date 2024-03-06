from abc import abstractmethod, ABC
from typing import List
from src.certificates.domain.models.coordinate import Coordinate


class CoordinateRepository(ABC):
    @abstractmethod
    def filter_by_template(self, template: str) -> List[Coordinate]:
        raise NotImplementedError
