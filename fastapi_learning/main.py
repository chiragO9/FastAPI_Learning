from fastapi import FastAPI

app = FastAPI()

# @app.get('/')

# def say_hi():
#   return {"So we are in Github"}

@app.get('/')
def blog():
  return  {'data' : {'Book':'Twilight book'}}

@app.get('/blog/{id}')
def showblog(id):
    return {"This is for showing blog." : id}

@app.get('/blog/{id}/comments')
def comments(id):
   return {'data' : {'1','2'}}

@app.get('/one/{id}')
def change_type(id:int):
   return {'data' :id}