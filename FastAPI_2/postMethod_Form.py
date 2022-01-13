from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
import uvicorn 
from typing import Optional 
from fastapi.templating import Jinja2Templates
app = FastAPI()
template = Jinja2Templates(directory='./')

@app.get('/login/')
def get_login_form(request: Request):
    return template.TemplateResponse('login_form.html', context= {'request':request})

@app.post("/login/")
def login(username:str = Form(...), password:str = Form(...)):
    return {"username":username}

if __name__=='__main__': 
    uvicorn.run("postMethod_Form:app", host = "0.0.0.0", port = 8000, reload=True)