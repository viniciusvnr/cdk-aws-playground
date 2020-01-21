import os
import json
import boto3
from botocore.vendored import requests  # use import requests for local test

code_pipeline = boto3.client('codepipeline')


def put_job_success(job, message):
    print('Putting job success')
    print(message)
    code_pipeline.put_job_success_result(jobId=job)


def put_job_failure(job, message):
    print('Putting job failure')
    print(message)
    code_pipeline.put_job_failure_result(jobId=job, failureDetails={'message': message, 'type': 'JobFailed'})


def get_job_name(job):
    print('Getting Code Pipeline name')


def lambda_handler(event, context):

    print('Function Executing')
    print("Event Passed to Handler: " + json.dumps(event))

    # load parameters from code pipeline event
    user_parameters = event["CodePipeline.job"]['data']['actionConfiguration']['configuration']['UserParameters']
    decoded_parameters = json.loads(user_parameters)

    # set function variables
    new_relic_app_id = decoded_parameters['FunctionVars']['APP_ID']
    new_relic_api_key = decoded_parameters['FunctionVars']['API_KEY']
    git_repo = decoded_parameters['FunctionVars']['GIT_REPO']
    app_name = decoded_parameters['FunctionVars']['APP_NAME']
    base_uri = f'https://api.newrelic.com/v2/applications/{new_relic_app_id}/deployments.json'
    change_log = event["CodePipeline.job"]['data']['inputArtifacts'][0]['revision']
    revision = f'Commit: {change_log[:7]}'
    description = f'{app_name} deployment'
    job_id = event['CodePipeline.job']['id']

    body = {
        "deployment": {
            "revision": revision,
            "changelog": f'https://github.com/flintapp/{git_repo}/commit/{change_log}',
            "description": description,
        }
    }
    headers = {
        "X-Api-Key": new_relic_api_key,
        "Content-Type": 'application/json'
    }
    r = requests.post(base_uri, data=json.dumps(body), headers=headers)

    if r.status_code == 201:
        put_job_success(job_id, f"New relic deployment post was Successful. http-code: {r.status_code}")
    else:
        put_job_failure(job_id, f"Fail to post to new relic api. Status Code {r.status_code}")
