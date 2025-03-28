import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
# import util
app=FastAPI()
@app.get("/hello")

async def hello():
    return "hello there!"

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)