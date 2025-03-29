
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import util
app=FastAPI()
@app.get("/hello")
async def hello():
    return "hello there!"

@app.post("/classify_image")

async def classify_image():
    form_data = await Request.form()
    image_data = form_data['image_data']
    image_data=Request.form['image_data']
    response = JSONResponse(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin','*')
    return response
   

if __name__=="__main__":
    print("FastAPI running..")
    util.load_artifacts()
    uvicorn.run(app,host="0.0.0.0",port=8080)