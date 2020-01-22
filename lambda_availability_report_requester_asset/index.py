import os
import json
import boto3
import logging
from config import endpoints

logger = logging.getLogger()


def lambda_handler(event, context):
    logger.info(f"Event: {str(event)}")

    client = boto3.client('lambda')

    for item in endpoints:
        logger.info(f"Payload to call lambda: {str(item)}")

        payload = json.dumps(item)
        try:
            response = client.invoke(
                FunctionName='lambda_availability_checker',
                InvocationType='Event',
                LogType='Tail',
                ClientContext='lambda_availability_requester',
                Payload=payload
            )
            logger.info(f"Request to lambda successfully.\nAppName: {item['appName']}")
        except Exception as e:
            logger.error(f"Error requesting to lambda.\nError: {e}")
