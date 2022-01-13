import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class fullstack(BaseModel):
    name: str
    Description: Optional[str] = None 
    skill: str
    score: Optional[float] = None

class ML(BaseModel):
    name:str
    skill:str
    score:Optional[float] = None 

@app.post("/fullstack/")
def create_stack(stack: fullstack): 
    return stack 

@app.post("/job/", response_model= ML)

def create_job(web: fullstack):
    return web
    
if __name__ == '__main__': 
    uvicorn.run('postMethod:app', host = "0.0.0.0", port = 8000, reload=True)
