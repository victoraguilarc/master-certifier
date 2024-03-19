from dataclasses import dataclass
from typing import List, Dict

from src.certificates.domain.models.replacement import ReplacementContext, Replacement


@dataclass
class ReplacementCollection(object):
    pages: Dict[int, List[Replacement]]

    def get_page_items(self, page: int) -> List[Replacement]:
        return self.pages.get(page, [])


