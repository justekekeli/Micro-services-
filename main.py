from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv
load_dotenv()

class Meaning(BaseModel):
    name: str

class Translation(BaseModel):
    name: str
    language : str

api_key = os.getenv('OPENAI')
openai.api_key = api_key


def name_option(name,language=None):
    if language :
        prompt = f'Give me a name that have the same meaning as {name} in {language}'
        max_tokens = 15
    else:
        prompt = f'Give me the meaning of the name {name}'
        max_tokens = 50
    explanation = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0
    )
    return explanation['choices'][0]['text']


app = FastAPI()


@app.get("/")
async def root():
    return "Welcome to Moli: Your names dictonnary"

@app.post("/explain")
async def explain_name(name:Meaning):
    payload = {'result':name_option(name.name)}
    return JSONResponse(content=jsonable_encoder(payload))

@app.post("/translate")
async def translate_name(obj:Translation):
    payload = {'result':name_option(obj.name,obj.language)}
    return JSONResponse(content=jsonable_encoder(payload))

if __name__ == '__main__':
    uvicorn.run(app, port=8080)