from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/items/{itemId}")
async def read_item(itemId):
    return {"itemId": itemId}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
