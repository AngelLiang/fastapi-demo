from typing import Union

# 1、导入 Depends
from fastapi import Depends, FastAPI
import uvicorn

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    # 2、创建依赖项
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    # 3、声明依赖项需要使用 Depends 和一个新的参数：
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
