import logging
import json
import azure.functions as func


def main(msg: func.QueueMessage, messageJSON, messageSub: func.Out[str] ) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    
    msgBody = json.loads(msg.get_body().decode('utf-8'))
    messageJSONLoad = json.loads(messageJSON)

    messageSub.set(json.dumps({
            "rowKey": msgBody['rowKey'], "subtitle": messageJSONLoad['subtitle'].upper(), "languageCode": msgBody['languageCode']
        }))
