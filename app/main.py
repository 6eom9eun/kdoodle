from contextlib import asynccontextmanager
from fastapi import FastAPI

def start():
    print("service is started.")
    
def shutdown():
    print("service is stopped.")    

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작점
    start()
    
    yield
    
    # 종료점
    shutdown()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}