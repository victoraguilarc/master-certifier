from dataclasses import dataclass
from typing import Optional

from mypy_boto3_s3.service_resource import Bucket
from mypy_boto3_s3.type_defs import GetObjectOutputTypeDef

from src.common.domain.interfaces.filebucket import FileBucket


@dataclass
class S3Bucket(FileBucket):
    bucket: Bucket

    def get_file(self, file_name: str) -> bytes:
        return self._read(
            self.bucket.Object(file_name).get()
        )

    def upload(
        self,
        file_name: str,
        file_content: bytes,
        content_type: Optional[str] = None,
    ):
        optional_params = {'ContentType': content_type}
        self.bucket.Object(file_name).put(
            Body=file_content,
            **self._remove_none_values(optional_params),
        )
        self.bucket.Object(file_name).get()
        return file_name

    def delete(self, file_name: str):
        pass

    def get_url(self, file_name: str) -> str:
        pass

    @classmethod
    def _read(cls, reference: GetObjectOutputTypeDef) -> bytes:
        return reference.get('Body').read()

    @classmethod
    def _remove_none_values(cls, data: dict) -> dict:  # noqa: WPS110
        return {key: value for key, value in data.items() if value is not None}  # noqa: WPS110

    #
    # def get(self, file_name):
    #     return self.bucket.Object(self._bucket_url, file_name).get()
    #
    # def upload(self, file_name, file_content, content_type: Optional[str] = None):
    #     optional_params = {'ContentType': content_type}
    #     return self._resource.Object(self._bucket_url, file_name).put(
    #         Body=file_content,
    #         **remove_none_values(optional_params),
    #     )
    #
    # def delete(self, file_name):
    #     return self._resource.Object(self._bucket_url, file_name).delete()
    #
    # def get_url(self, file_name):
    #     return 'https://{bucket_url}.s3.amazonaws.com/{file_name}'.format(
    #         bucket_url=self._bucket_url,
    #         file_name=file_name,
    #     )
    #
    # def read(self, file_name):
    #     return self.get(file_name)['Body'].read()
