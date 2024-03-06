from dataclasses import dataclass
from typing import Optional


@dataclass
class Certificate(object):
    id: str
    category: str
    group: str
    file_url: Optional[str] = None

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'category': self.category,
            'group': self.group,
            'file_url': self.file_url,
        }

    @classmethod
    def from_dict(cls, instance_data: dict) -> 'Certificate':
        return cls(
            id=instance_data['id'],
            category=instance_data['category'],
            group=instance_data['group'],
            file_url=instance_data.get('file_url'),
        )
