from pydantic import BaseModel

class MessageRequest(BaseModel):
    title: str
    message: str