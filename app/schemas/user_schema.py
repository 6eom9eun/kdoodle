from pydantic import BaseModel, EmailStr

class UserRegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str