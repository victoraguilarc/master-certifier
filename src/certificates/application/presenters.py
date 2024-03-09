from dataclasses import dataclass

from src.certificates.domain.models.certificate import Certificate
from src.common.environment import CLOUDFRONT_BASE_URL


@dataclass
class CertificatePresenter(object):
    instance: Certificate

    @property
    def to_dict(self):
        return {
            'id': self.instance.id,
            'template_id': self.instance.template_id,
            'group': self.instance.group,
            'file_path': f'{CLOUDFRONT_BASE_URL}/{self.instance.file_path}',
        }
