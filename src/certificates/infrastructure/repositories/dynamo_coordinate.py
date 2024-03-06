from typing import List, Optional

from boto3.dynamodb.conditions import Key

from src.certificates.domain.models.certificate import Certificate
from src.certificates.domain.models.coordinate import Coordinate
from src.certificates.domain.repositories.certificate import CertificateRepository
from src.certificates.domain.repositories.coordinate import CoordinateRepository
from src.common.infrastructure.dynamo_db import DynamoDBMixin


class DynamoCoordinateRepository(DynamoDBMixin, CoordinateRepository):
    def filter_by_template(self, template: str) -> List[Coordinate]:
        query_result = self.table.query(
            KeyConditionExpression=Key('template').eq(template),
        )
        matches = query_result.get('Items', [])
        return [Coordinate.from_dict(match) for match in matches]
