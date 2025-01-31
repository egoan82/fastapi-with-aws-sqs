import logging
import sys

hostname = "fastapi-aws-sqs"

log_format = (
    f"[%(levelname)s][{hostname}][%(filename)s:%(lineno)d][%(funcName)s] %(message)s"
)

logging.basicConfig(
    format=log_format,
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)