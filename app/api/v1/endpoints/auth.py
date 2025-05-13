from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
async def login():
    return {"message": "Login endpoint"}

@router.get("/register")
async def register():
    return {"message": "Register endpoint"}

@router.get("/logout")
async def logout():
    return {"message": "Logout endpoint"}