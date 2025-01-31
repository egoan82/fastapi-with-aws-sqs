from fastapi import APIRouter
from routes.api.messages import router as messages_router

router = APIRouter()
router.include_router(messages_router, prefix="/messages", tags=["messages"])