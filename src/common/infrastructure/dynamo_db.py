from dataclasses import dataclass

from botocore.exceptions import ClientError
from mypy_boto3_dynamodb.service_resource import Table


@dataclass
class DynamoDBMixin(object):
    table: Table

    def get(self, key):
        return self.table.get_item(Key=key).get('Item')

    def put(self, attributes):
        extra_args = {}
        try:
            return self.table.put_item(Item=attributes, **extra_args)
        except ClientError as exception:
            raise
