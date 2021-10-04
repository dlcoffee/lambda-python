import json


def handler(event, context):
    body = {
        "message": "hello for api",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
