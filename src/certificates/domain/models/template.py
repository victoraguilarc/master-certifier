from dataclasses import dataclass


@dataclass
class Template(object):
    id: str
    file_path: str

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'file_path': self.file_path,
        }

    @classmethod
    def from_dict(cls, instance_data: dict) -> 'Template':
        return cls(
            id=instance_data['id'],
            file_path=instance_data.get('file_path'),
        )
