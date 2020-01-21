import boto3
from lambda_availabilitty_report_checker_asset.lambda_resources.logger import Logger


class DynamoDb:

    def __init__(self, access_key_id, secret_access_key, endpoint=None):
        self.dynamo_db = boto3.resource(
            'dynamodb', aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            endpoint_url=endpoint)

    def addItem(self, table, item):
        self.table = table
        self.item = item

        table_ = self.dynamo_db.Table(self.table)
        response = table_.put_item(Item=self.item)

        return response

    def _createTable(self, table: str, key_schema: list, attr_definitions: list, prov_throughput: dict):
        self.table = table
        self.key_schema = key_schema
        self.attr_definitions = attr_definitions
        self.prov_throughput = prov_throughput

        create_table = self.dynamo_db.create_table(
            TableName=self.table,
            KeySchema=self.key_schema,
            AttributeDefinitions=self.attr_definitions,
            ProvisionedThroughput=self.prov_throughput
        )
        return create_table

# to run dynamo local
# docker run -p 8000:8000 amazon/dynamodb-local
# Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client

# Dynamo Item
# {
# 	"id": "fb6915fb-9f84-4df7-a983-5f1c43666944", <string>
# 	"createdAt": "2020-01-16T15:40:41Z", <string>
# 	"appName": "Application-api", <string>
# 	"environment": "staging", <string>
# 	"httpStatus": 200, <number>
# 	"success": true, <bool>
# 	"isMaintenance": false, <bool>
# 	"duration": 0.559907 <number>
# }

# k_schema = [
#     {
#         'AttributeName': 'id',
#         'KeyType': 'HASH'
#     },
# {
#     'AttributeName': 'createdAt',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'appName',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'environment',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'httpStatus',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'success',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'isMaintenance',
#     'KeyType': 'RANGE'
# },
# {
#     'AttributeName': 'duration',
#     'KeyType': 'RANGE'
# }
# ]

# attr_def = [
#     {
#         'AttributeName': 'id',
#         'AttributeType': 'S'
#     },
# {
#     'AttributeName': 'createdAt',
#     'AttributeType': 'S'
# },
# {
#     'AttributeName': 'appName',
#     'AttributeType': 'S'
# },
# {
#     'AttributeName': 'environment',
#     'AttributeType': 'S'
# },
# {
#     'AttributeName': 'httpStatus',
#     'AttributeType': 'N'
# },
# {
#     'AttributeName': 'success',
#     'AttributeType': 'S'
# },
# {
#     'AttributeName': 'isMaintenance',
#     'AttributeType': 'S'
# },
# {
#     'AttributeName': 'duration',
#     'AttributeType': 'N'
# }
# ]
#
# prov_throughput = {
#     'ReadCapacityUnits': 1,
#     'WriteCapacityUnits': 1
# }
# db_client = DynamoDb()
# create_table = db_client.createTable(
#     table='AvailabilityCheck',
#     key_schema=k_schema,
#     attr_definitions=attr_def,
#     prov_throughput=prov_throughput
# )
#
# print(create_table)
