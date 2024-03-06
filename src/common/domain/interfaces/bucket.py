from abc import ABC, abstractmethod
from typing import Optional


class Bucket(ABC):

    @abstractmethod
    def get(self, file_name: str):
        raise NotImplementedError

    @abstractmethod
    def upload(
        self,
        file_name: str,
        file_content: bytes,
        content_type: Optional[str] = None,
    ):
        raise NotImplementedError

    @abstractmethod
    def delete(self, file_name: str):
        raise NotImplementedError

    @abstractmethod
    def get_url(self, file_name: str) -> str:
        raise NotImplementedError


