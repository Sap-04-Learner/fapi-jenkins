from fastapi import FastAPI

app = FastAPI()

@app.get('/name/{name}')
def home(name: str = "Guest"):
    return {
            'message': f'Welcome {name}! To this page',
            'description': 'You have connected to Jenkins Properly!'
        } 

@app.get('/')
def home():
    return {'message': 'hello world'}

