from fastapi import APIRouter
from schemas.messages import MessageRequest
from dependencies.aws_sqs import send_sqs_message

router = APIRouter()


@router.post(
    "/send_message",
    status_code=201,
    response_model=None,
    tags=["messages"],
    description="Send a message to a queue",
)
async def send_message(
        message: MessageRequest,
):
    message_id = send_sqs_message(message.model_dump())
    return {"message_id": message_id}