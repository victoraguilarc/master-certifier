from collections import defaultdict
from typing import List, Optional

from boto3.dynamodb.conditions import Key

from src.certificates.domain.models.replacement import Replacement
from src.certificates.domain.models.replacement_item import ReplacementCollection
from src.certificates.domain.models.template import Template
from src.certificates.domain.repositories.replacement import ReplacementRepository
from src.common.infrastructure.dynamo_db import DynamoDBMixin


class DynamoReplacementRepository(DynamoDBMixin, ReplacementRepository):
    def get_collection(self, template_id: str) -> Optional[ReplacementCollection]:
        replacements = self.filter_by_template(template_id)
        if not replacements:
            return None
        pages = defaultdict(list)
        for replacement in replacements:
            pages[replacement.page].append(replacement)
        return ReplacementCollection(pages=pages)

    def find_template(self, template_id: str) -> Optional[Template]:
        raise NotImplementedError

    def filter_by_template(self, template_id: str) -> List[Replacement]:
        query_result = self.table.query(
            IndexName='template_id',
            KeyConditionExpression=Key('template_id').eq(template_id),
        )
        matches = query_result.get('Items', [])
        return [Replacement.from_dict(match) for match in matches]


