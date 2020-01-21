import json
import uuid
import datetime
import requests
from lambda_availabilitty_report_checker_asset.lambda_resources.logger import Logger


class HealthChecker:

    @classmethod
    def caller(cls, url, app_name: str, environment: str, is_maintenance: bool):

        cls.url = url
        cls.app_name = app_name
        cls.environment = environment
        cls.is_maintenance = is_maintenance
        response = {}

        # make request
        try:
            Logger.LogMsg(msg=f'Sending request to {cls.url}')
            r = requests.get(cls.url)
        except Exception as e:
            Logger.LogMsg(msg=f'Error requesting to {cls.url}: {e}')
        else:
            req_time = r.elapsed.total_seconds()
            req_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            check_id = uuid.uuid4()
            response['id'] = str(check_id)
            response['createdAt'] = req_date
            response['appName'] = cls.app_name
            response['environment'] = cls.environment
            response['isMaintenance'] = cls.is_maintenance
            response['duration'] = req_time

            # process request
            if r.status_code == 200:
                response['httpStatus'] = 200
                response['success'] = True
            else:
                response['httpStatus'] = r.status_code
                response['success'] = False

            json_response = json.dumps(response)

            return json_response
