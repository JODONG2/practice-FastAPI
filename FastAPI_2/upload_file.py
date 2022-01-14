from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from typing import Optional , List
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app=FastAPI()

@app.post('/files/')
def create_files(files:List[bytes] = File(...)):
    return {'file_size': len(file) for file in files}

@app.post('/uploadfiles')

def create_upload_files(files:List[UploadFile] = File(...)):
    return {'file_name': file.filename for file in files}

@app.get('/')
def main():
    content = """
<body>

<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>

<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>

</body>
    """
    return HTMLResponse(content=content)

if __name__ =='__main__':
    uvicorn.run('upload_file:app', host = "0.0.0.0", port=8000 , reload = True)