from botocore.exceptions import ClientError
from mypy_boto3_dynamodb.service_resource import Table


class DynamoDBMixin(object):
    table: Table

    def __init__(self, table_name):
        self.table = table_name

    def get(self, key):
        return self.table.get_item(Key=key).get('Item')

    def put(self, attributes):
        extra_args = {}
        try:
            return self.table.put_item(Item=attributes, **extra_args)
        except ClientError as exception:
            raise
