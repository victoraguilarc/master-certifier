from dataclasses import dataclass
from typing import List, Dict

from src.certificates.domain.models.replacement import ReplacementContext, Replacement


@dataclass
class ReplacementItem(ReplacementContext):
    value: str

    @property
    def to_dict(self) -> dict:
        return {
            'page': self.page,
            'axis_x': self.axis_x,
            'axis_y': self.axis_y,
            'name': self.name,
            'value': self.value,
        }

    @classmethod
    def from_dict(cls, instance_data) -> 'ReplacementItem':
        return cls(
            page=instance_data['page'],
            axis_x=instance_data['axis_x'],
            axis_y=instance_data['axis_y'],
            name=instance_data['name'],
            value=instance_data['value'],
        )


@dataclass
class ReplacementCollection(object):
    pages: Dict[int, List[Replacement]]

    def get_page_items(self, page: int) -> List[Replacement]:
        return self.pages.get(page, [])


