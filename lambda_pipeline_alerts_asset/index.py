import json
import logging
import os
from botocore.vendored import requests  # use import requests for local test


# Read environment variables
SLACK_WEB_HOOK_URL = os.environ['SLACK_WEB_HOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    # Read message posted on SNS Topic
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + str(message))

# Construct a slack message
    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "%s" % message
    }

# Post message on SLACK_WEB_HOOK_URL
    req = requests.post(SLACK_WEB_HOOK_URL, json.dumps(slack_message))

    if req.status_code == 200:
        logger.info(f'Post to slack was successful /nHttpCode: {req.status_code}')
    else:
        logger.error(f'Post to Slack failed /nHttpCode: {req.status_code}')
