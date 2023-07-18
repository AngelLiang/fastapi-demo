from typing import Union

from fastapi import Body, FastAPI
# 注意，Field 是直接从 pydantic 导入的，而不是像其他的（Query，Path，Body 等）都从 fastapi 导入。
from pydantic import BaseModel, Field

import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero", default=1)
    tax: Union[float, None] = None


@app.put("/items/{itemId}")
async def update_item(itemId: int, item: Item = Body(embed = True)):
    results = {"itemId": itemId, "item": item}
    print(results)
    return results

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
