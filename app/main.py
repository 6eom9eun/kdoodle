from contextlib import asynccontextmanager
from app.api.v1.routers import api_router
from fastapi import FastAPI

async def start():
    print("service is started.")
    
def shutdown():
    print("service is stopped.")    

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작점
    await start()
    
    yield
    
    # 종료점
    shutdown()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# v1 API 라우터
app.include_router(api_router, prefix="/api/v1")