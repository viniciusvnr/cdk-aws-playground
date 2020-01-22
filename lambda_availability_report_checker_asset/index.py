import os
import json
from decimal import Decimal
from lambda_resources.checker.HealthChecker import HealthChecker
from lambda_resources.repository.DynamoDb import DynamoDb
from lambda_resources.logger import Logger


def lambda_handler(event, context):
    """
    event to be sent to lambda:
    {
        "url": "https://payments-api-staging.growpay.me/health",
        "appName": "Payments-api",
        "environment": "staging",
        "isMaintenance": false
    }
    """

    Logger.LogMsg(msg=f"Event: {str(event)}", level='INFO')

    dynamo_db_table = 'AvailabilityReports'

    db_client = DynamoDb()

    # Request
    try:
        resp = HealthChecker.caller(
            app_name=event['appName'],
            environment=event['environment'],
            is_maintenance=event['isMaintenance'],
            url=event['url']
        )
        # Insert item in DynamoDb Table
        dynamo_item = json.loads(resp, parse_float=Decimal)
        add_item_to_dynamo_db = db_client.addItem(item=dynamo_item, table=dynamo_db_table)
        req_id = add_item_to_dynamo_db['ResponseMetadata']['RequestId']
        Logger.LogMsg(f'Item added to dynamo table: {dynamo_db_table}. RequestId: {req_id}.')

        return True

    except Exception as e:
        Logger.LogMsg(e, level='ERROR')
        return False

# --- TEST ---
#
# lambda_event = json.dumps({
#     "url": "https://payments-api-staging.growpay.me/health",
#     "appName": "Payments-api",
#     "environment": "staging",
#     "isMaintenance": False
# })
#
# test = lambda_handler(lambda_event, 'test')
# print(test)
