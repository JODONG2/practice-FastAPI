from fastapi import FastAPI
import uvicorn 

app = FastAPI()

items= {} 

@app.on_event("startup") 
def startup_event(): 
    print("Startup event") 
    items["start"] = {"name":"ㅠ^ㅠ"}
    items["event"] = {"name":"^-^"}

@app.on_event("shutdown") 
def shutdown_event(): 
    print("Shutdown event") 
    with open("log.txt", mode= 'a') as log : 
        log.write("application shutdown") 

@app.get('/items/{item_id}')
def read_item(item_id: str): 
    return items[item_id]

if __name__ == '__main__': 
    uvicorn.run("eventHandler:app", host = "0.0.0.0", port = 8000, reload= True)