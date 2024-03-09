from typing import List, Optional

from boto3.dynamodb.conditions import Key

from src.certificates.domain.models.replacement import Replacement
from src.certificates.domain.models.template import Template
from src.certificates.domain.repositories.replacement import ReplacementRepository
from src.certificates.domain.repositories.template import TemplateRepository
from src.common.infrastructure.dynamo_db import DynamoDBMixin


class DynamoTemplateRepository(DynamoDBMixin, TemplateRepository):

    def find_template(self, id: str) -> Optional[Template]:
        query_result = self.table.query(
            KeyConditionExpression=Key('id').eq(id),
        )
        matches = query_result.get('Items', [])
        if not matches:
            return None
        return Template.from_dict(matches[0])



