from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    async def register_user(db: AsyncSession, email: str, username: str, password: str):
        result = await db.execute(select(User).where(User.email == email))
        if result.scalars().first():
            return None
        hashed_password = AuthService.hash_password(password)
        user = User(email=email, username=username, hashed_password=hashed_password)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user