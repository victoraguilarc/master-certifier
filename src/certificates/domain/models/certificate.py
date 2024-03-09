from dataclasses import dataclass
from typing import Optional


@dataclass
class Certificate(object):
    id: str
    template_id: str
    group: str
    file_path: Optional[str] = None

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'template_id': self.template_id,
            'group': self.group,
            'file_path': self.file_path,
        }

    @classmethod
    def from_dict(cls, instance_data: dict) -> 'Certificate':
        return cls(
            id=instance_data['id'],
            template_id=instance_data['template_id'],
            group=instance_data['group'],
            file_path=instance_data.get('file_path'),
        )
