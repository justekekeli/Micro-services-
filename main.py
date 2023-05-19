from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to Moli: Your names dictonnary"

@app.post("/explain")
def explain_name():
    return "Explain the name kekeli"

@app.post("/translate")
def translate_name():
    return "Translate kekeli in French"

if __name__ == '__main__':
    uvicorn.run(app, port=8080)