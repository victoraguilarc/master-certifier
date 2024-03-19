from dataclasses import dataclass

from src.common.domain.base_enum import BaseEnum


class TextAlignment(BaseEnum):
    LEFT = 'LEFT'
    CENTER = 'CENTER'
    RIGHT = 'RIGHT'
    JUSTIFY = 'JUSTIFY'


@dataclass
class TextMetadata(object):
    alignment: TextAlignment = TextAlignment.CENTER
    font_size: float = 12
    font_family: str = 'Arial'

    @property
    def is_text_center(self) -> bool:
        return self.alignment == TextAlignment.CENTER

    @property
    def is_text_left(self) -> bool:
        return self.alignment == TextAlignment.LEFT

    @property
    def is_text_right(self) -> bool:
        return self.alignment == TextAlignment.RIGHT

    @property
    def to_dict(self) -> dict:
        return {
            'alignment': str(self.alignment),
            'font_size': self.font_size,
            'font_family': self.font_family,
        }

    @classmethod
    def from_dict(cls, instance_data: dict) -> 'TextMetadata':
        return cls(
            alignment=(
                TextAlignment.from_value(instance_data['alignment'])
                if instance_data.get('alignment')
                else TextAlignment.CENTER
            ),
            font_size=(
                float(instance_data['font_size'])
                if instance_data.get('font_size')
                else 12
            ),
            font_family=(
                instance_data.get('font_family')
                if instance_data.get('font_family')
                else 'Arial'
            ),
        )



