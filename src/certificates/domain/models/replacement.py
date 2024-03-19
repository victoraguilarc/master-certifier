from dataclasses import dataclass

from src.common.domain.base_enum import BaseEnum


@dataclass
class ReplacementContext(object):
    page: int
    axis_x: float
    axis_y: float
    name: str


class ReplacementCategory(BaseEnum):
    TEXT = 'text'
    IMAGE = 'image'


@dataclass
class Replacement(ReplacementContext):
    id: str
    template_id: str
    category: ReplacementCategory
    metadata: dict

    @property
    def is_text(self) -> bool:
        return self.category == ReplacementCategory.TEXT

    @property
    def is_image(self) -> bool:
        return self.category == ReplacementCategory.IMAGE

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'page': self.page,
            'axis_x': self.axis_x,
            'axis_y': self.axis_y,
            'name': self.name,
            'category': str(self.category),
            'template_id': self.template_id,
            'metadata': self.metadata,
        }

    @classmethod
    def from_dict(cls, instance_data) -> 'Replacement':
        return cls(
            id=instance_data['id'],
            page=instance_data['page'],
            axis_x=float(instance_data['axis_x']),
            axis_y=float(instance_data['axis_y']),
            name=instance_data['name'],
            category=ReplacementCategory.from_value(instance_data['category']),
            template_id=instance_data['template_id'],
            metadata=instance_data.get('metadata', {}),
        )


