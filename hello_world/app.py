import json
import requests

def lambda_handler(event, context):
    print(event)

    try:
        ip = requests.get("https://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "v2 hello world from Python function",
            "location": ip.text.replace("\n", "")
        }),
    }
