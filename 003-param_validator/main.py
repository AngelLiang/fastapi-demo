from typing import Annotated

from fastapi import FastAPI
from fastapi import Query
from fastapi import Path
import uvicorn

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/query")
async def read_items_query(q: str | None = Query(default = None, max_length = 50)):
    """
    使用Query()作为函数参数的默认值，将参数max_length设置为50
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title = "The ID of the item to get", ge = 0, le = 1000)],
    q: str = None,
    size: Annotated[float, Query(gt = 0, lt = 10.5)] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
