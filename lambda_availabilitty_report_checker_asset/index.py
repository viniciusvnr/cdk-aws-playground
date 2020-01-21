import os
import json
from decimal import Decimal
from lambda_availabilitty_report_checker_asset.lambda_resources.checker.HealthChecker import HealthChecker
from lambda_availabilitty_report_checker_asset.lambda_resources.repository.DynamoDb import DynamoDb
from lambda_availabilitty_report_checker_asset.lambda_resources.logger import Logger


def lambda_handler(event, context):
    """
    event to be sent to lambda:
    {
        "url": "https://xxx/health",
        "appName": "application-name",
        "environment": "staging",
        "isMaintenance": false
    }
    """

    Logger.LogMsg(msg=f"Event: {str(event)}", level='INFO')

    access_key = os.environ.get('DB_ACCESS_KEY')
    secret_key = os.environ.get('DB_SECRET_KEY')
    dynamo_db_table = 'AvailabilityCheck'

    db_client = DynamoDb(
        access_key_id=access_key,
        secret_access_key=secret_key
        #endpoint='http://localhost:8000/' for local test.
    )

    # Request
    input_request = json.loads(event)
    try:
        resp = HealthChecker.caller(
            app_name=input_request['appName'],
            environment=input_request['environment'],
            is_maintenance=input_request['isMaintenance'],
            url=input_request['url']
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
#     "url": "https://www.google.com",
#     "appName": "application-api",
#     "environment": "staging",
#     "isMaintenance": False
# })
#
# test = lambda_handler(lambda_event, 'test')
# print(test)
