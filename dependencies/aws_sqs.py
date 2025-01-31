import json
import time

import boto3

from core.config import settings
from utils.logger import logger


def send_sqs_message(message: dict):
    sqs = boto3.client(
        "sqs",
        aws_access_key_id=settings.aws_key_id,
        aws_secret_access_key=settings.aws_secret_key,
        region_name=settings.aws_region,
        endpoint_url=settings.localstack_url,
    )

    parser_message = json.dumps(message)
    response = sqs.send_message(
        QueueUrl=settings.sqs_queue_url,
        MessageBody=parser_message,
        MessageGroupId="messageGroup1",
        MessageDeduplicationId="1",
    )
    logger.info(f"Message sent: {response.get('MessageId')}")
    return response.get("MessageId")


def listen_sqs():
    sqs = boto3.client(
        "sqs",
        aws_access_key_id=settings.aws_key_id,
        aws_secret_access_key=settings.aws_secret_key,
        region_name=settings.aws_region,
        endpoint_url=settings.localstack_url,
    )
    while True:
        logger.info("Listening to SQS")
        response = sqs.receive_message(
            QueueUrl=settings.sqs_queue_url,
            AttributeNames=["All"],
            MaxNumberOfMessages=1,
            MessageAttributeNames=["All"],
            VisibilityTimeout=10,
            WaitTimeSeconds=10,
        )
        if "Messages" in response:
            for message in response["Messages"]:
                logger.info(message)
                sqs.delete_message(
                    QueueUrl=settings.sqs_queue_url, ReceiptHandle=message["ReceiptHandle"]
                )
        else:
            time.sleep(5)
