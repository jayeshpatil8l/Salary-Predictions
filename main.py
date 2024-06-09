import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import predict, Data

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name = "static")

templates = Jinja2Templates(directory = "templates")


@app.get("/", response_class = HTMLResponse )
async def read_data(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/predict", response_class = HTMLResponse) 
async def display(request : Request, 
        designation:str = Form(...),
        age : int = Form(...),
        exp : int = Form(...),
        ratings : int = Form(...),
        leaves : int = Form(...)):
    
    vars = {"designation": designation, "age": age, "exp":exp, "ratings": ratings, "leaves": leaves}
    prediction = predict(Data(**vars))
   
    return templates.TemplateResponse("results.html", 
        {
        "request": request, 
        "designation": designation, 
        "age":age, 
        "exp":exp,
        "ratings": ratings, 
        "leaves":leaves, 
        "prediction": prediction
        })

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8000)


