import logging
import uuid
import json
import typing

import azure.functions as func


def main(request: func.HttpRequest, msg: func.Out[typing.List[str]]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")
    languages = req_body.get("languages")
    
    dataList = []

    for lang in languages:
        dataList.append(json.dumps({
            "rowKey": str(uuid.uuid4()), "subtitle": subtitle,"languageCode": lang
        }))

    msg.set(dataList)

    return func.HttpResponse(f"New Message Queue entries created: {dataList}", status_code=200)