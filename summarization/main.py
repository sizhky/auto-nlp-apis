from fastapi import APIRouter
from pydantic import BaseModel
from summarization.infer import infer

router = APIRouter()


class SummarizationRequest(BaseModel):
    text: str


@router.post("/validate/")
async def validate(request: SummarizationRequest):
    return infer(request.text)
