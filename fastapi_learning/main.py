from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def say_hi():
  return {"So we are in Github"}