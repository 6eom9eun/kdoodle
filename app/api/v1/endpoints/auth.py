from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.auth_service import AuthService
from app.schemas.user_schema import UserRegisterRequest

router = APIRouter()

@router.post("/register")
async def register(req: UserRegisterRequest, db: AsyncSession = Depends(get_db)):
    user = await AuthService.register_user(db, req.email, req.username, req.password)
    if not user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    return {"message": "회원가입 성공", "user_id": user.id}