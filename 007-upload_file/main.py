"""
使用文件上传，需要先安装python-multipart

    pip install python-multipart

"""
from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
