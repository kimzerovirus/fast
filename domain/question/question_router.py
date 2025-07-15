from fastapi import APIRouter
from database import SessionLocal
from models import Question

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list")
async def list_questions():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _question_list