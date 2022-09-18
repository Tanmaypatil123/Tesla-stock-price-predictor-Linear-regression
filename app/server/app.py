from typing import Union

from fastapi import FastAPI,Form,templating,Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle


templates = Jinja2Templates(directory="templates")
regmodel=pickle.load(open('regmodel.pkl','rb'))

app = FastAPI()


@app.route('/')
def home(request:Request):
    context = {'request': request,"price":""}
    return templates.TemplateResponse('index.html',context)

@app.post("/predict/")
def predict_price(request:Request,Open:float = Form(),High:float = Form(),Low:float = Form(),Volumn:float = Form()):
    pred = regmodel.predict([[Open,High,Low,Volumn]])[0]
    print([Open,High,Low,Volumn])
    context = {'request': request,"price":pred}
    return templates.TemplateResponse("index.html",context=context)

