import json


def handler(event, context):
    todos = [
        {'id': 1, 'name': 'first todo', 'status': 'open'},
        {'id': 2, 'name': 'second  todo', 'status': 'done'},
    ]

    body = {
        "data": todos,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
