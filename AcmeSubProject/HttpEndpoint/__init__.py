import logging
import uuid
import json
import typing

import azure.functions as func


def main(request: func.HttpRequest, msg: func.Out[typing.List[str]], message: func.Out[str]) -> func.HttpResponse:
 
    req_body = request.get_json()
    subtitle = req_body.get("subtitle")
    languages = req_body.get("languages")
    rowKey = str(uuid.uuid4())
    
    table = json.dumps({
        "rowKey": rowKey, "subtitle": subtitle,
    })
    
    queueList = []

    for lang in languages:
        queueList.append(json.dumps({
            "rowKey": rowKey, "languageCode": lang
        }))

    message.set(table)
    msg.set(queueList)

    return func.HttpResponse(f"New Subtitles added to table: {table}. New Language Message Queue entries created: {queueList}", status_code=200)