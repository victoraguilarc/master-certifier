from dataclasses import dataclass


@dataclass
class Coordinate(object):
    id: str
    axis_x: int
    axis_y: int
    key: str
    template: str

    @property
    def to_dict(self) -> dict:
        return {
            'axis_x': self.axis_x,
            'axis_y': self.axis_y,
            'key': self.key,
            'template': self.template,
        }

    @classmethod
    def from_dict(cls, isntance_data) -> 'Coordinate':
        return cls(
            axis_x=isntance_data['axis_x'],
            axis_y=isntance_data['axis_y'],
            key=isntance_data['key'],
            template=isntance_data['template'],
        )


@dataclass
class Input(object):
    key: str
    value: str

    @property
    def to_dict(self) -> dict:
        return {
            'key': self.key,
            'value': self.value,
        }

    @classmethod
    def from_dict(cls, isntance_data) -> 'Input':
        return cls(
            key=isntance_data['key'],
            value=isntance_data['value'],
        )


@dataclass
class Replacement(object):
    input: Input
    coordinate: Coordinate

    @property
    def to_dict(self) -> dict:
        return {
            'input': self.input.to_dict,
            'coordinate': self.coordinate.to_dict,
        }

    @classmethod
    def from_dict(cls, isntance_data) -> 'Replacement':
        return cls(
            input=Input.from_dict(isntance_data['input']),
            coordinate=Coordinate.from_dict(isntance_data['coordinate']),
        )

