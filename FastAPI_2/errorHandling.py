from fastapi import FastAPI,HTTPException
import uvicorn 

app = FastAPI()

items = {
    1:"JODONG2",
    2:"DoNgineer",
    3:"^-^", 
}

@app.get("/items/{id}")
def get_items(id:int) :
    try:
        item = items[id]
    except KeyError:
        raise HTTPException(status_code=404, detail= f'아이템을 찾을 수 없슴다! {id}')
    return item

if __name__ == '__main__':
    uvicorn.run("errorHandling:app", host = "0.0.0.0", port=8000, reload=True)