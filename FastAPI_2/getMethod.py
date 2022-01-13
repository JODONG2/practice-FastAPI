from fastapi import FastAPI
import uvicorn 
from typing import Optional 

app = FastAPI()

career = [{"CV": "my career"}, {"NLP":"your career"}, {"MLOps":"our career" }]

@app.get("/career")
def get_career(first:int = 0, limit:int = 1):
    return career[first:first+limit]

@app.get("/users/{user_id}")
def get_user2(user_id:str, option:Optional[str]= None):
    if option:
        return {user_id:option}
    return {user_id:user_id+" and option is None"}

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id":user_id}

@app.get("/")
def root():
    return {"message":"Hello World"}

if __name__ =='__main__':
    uvicorn.run("getMethod:app", host='0.0.0.0', port = 8000, reload=True)
