import uvicorn
from fastapi import FastAPI
from user import user_router
from goods import goods_router

app = FastAPI()


app.include_router(goods_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app="test:app",host="0.0.0.0",port=8000,reload=True)