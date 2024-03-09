from dataclasses import dataclass


@dataclass
class ReplacementContext(object):
    page: int
    axis_x: float
    axis_y: float
    name: str


@dataclass
class Replacement(ReplacementContext):
    id: str
    template_id: str

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'page': self.page,
            'axis_x': self.axis_x,
            'axis_y': self.axis_y,
            'name': self.name,
            'template_id': self.template_id,
        }

    @classmethod
    def from_dict(cls, instance_data) -> 'Replacement':
        return cls(
            id=instance_data['id'],
            page=instance_data['page'],
            axis_x=float(instance_data['axis_x']),
            axis_y=float(instance_data['axis_y']),
            name=instance_data['name'],
            template_id=instance_data['template_id'],
        )



