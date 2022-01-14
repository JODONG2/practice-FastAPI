from fastapi import FastAPI, APIRouter 
import uvicorn 

user_router = APIRouter(prefix="/users") 
order_router = APIRouter(prefix="/orders") 

@user_router.get("/", tags=["users"])
def create_user():
    return [{"name": "JODONG2"}]

@user_router.get("/me", tags=["users"])
def get_my_id():
    return {"name": "fakeID"}

@order_router.get("/" , tags=["orders"]) 
def get_order_list():
    return [{"skill": "AI"}, {"skill":"ComputerVision"}, {"skill:MLOps"},{"skill:BE"}] 

app= FastAPI() 

@app.get("/", tags=["root"])
def root():
    return {"HI":"THERE :)"}

if __name__ == '__main__': 
    app.include_router(user_router)
    app.include_router(order_router)
    uvicorn.run("apiRouter:app", host = "0.0.0.0", port = 8000)