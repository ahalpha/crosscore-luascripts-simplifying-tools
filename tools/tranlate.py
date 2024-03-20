import json
import requests
from src.configs import *

def tranlate(source, direction):
    if configs_general.enable_tranlate:
        url = "http://api.interpreter.caiyunai.com/v1/translator"

        # WARNING, this token is a test token for new developers,
        # and it should be replaced by your token
        token = configs_general.tranlate_token

        payload = {
            "source": source,
            "trans_type": direction,
            "request_id": "demo",
            "detect": True,
        }

        headers = {
            "content-type": "application/json",
            "x-authorization": "token " + token,
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        return json.loads(response.text)["target"]
    
    return source