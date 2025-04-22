import store
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import RedirectResponse


app = FastAPI()

STATIC_DIR = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
@app.get('/')

def get_list():
    return [1, 2, 3, 4, 5, 6]

@app.get('/contact')

@app.get('/html')
async def read_root():

    return RedirectResponse(url="/static/index.html")   
def get_list():
    return {'name' : 'Platzi'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()