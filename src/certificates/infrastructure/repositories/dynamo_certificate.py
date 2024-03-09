from typing import List, Optional

from boto3.dynamodb.conditions import Key

from src.certificates.domain.models.certificate import Certificate
from src.certificates.domain.repositories.certificate import CertificateRepository
from src.common.infrastructure.dynamo_db import DynamoDBMixin


class DynamoCertificateRepository(DynamoDBMixin, CertificateRepository):
    def find_by_id(self, instance_id: str) -> Optional[Certificate]:
        query_result = self.table.query(
            KeyConditionExpression=Key('instance_id').eq(instance_id),
        )
        matches = query_result.get('Items', [])
        if not matches:
            return None
        return Certificate.from_dict(matches[0])

    def filter_by_category(self, category: str) -> List[Certificate]:
        query_result = self.table.query(
            IndexName='category',
            KeyConditionExpression=Key('country').eq(category),
        )
        matches = query_result.get('Items', [])
        return [Certificate.from_dict(match) for match in matches]

    def filter_by_group(self, group: str) -> List[Certificate]:
        query_result = self.table.query(
            IndexName='group',
            KeyConditionExpression=Key('group').eq(group),
        )
        matches = query_result.get('Items', [])
        return [Certificate.from_dict(match) for match in matches]

    def persist(self, instance: Certificate):
        self.table.put_item(Item=instance.to_dict)
