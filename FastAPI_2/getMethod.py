from fastapi import FastAPI
import uvicorn 


app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id":user_id}

@app.get("/")
def root():
    return {"message":"Hello World"}

if __name__ =='__main__':
    uvicorn.run("getMethod:app", host='0.0.0.0', port = 8000, reload=True)
