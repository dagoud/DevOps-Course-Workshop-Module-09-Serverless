import logging
import json
import azure.functions as func


def main(msg: func.QueueMessage, messageJSON) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    
    message = json.loads(messageJSON)
    print(f"Table row: {messageJSON}")
    # return func.HttpResponse(f"Table row: {messageJSON}")
