from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .schemas import Message, Product
from .table_manager import save_product

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount('/static', StaticFiles(directory=BASE_DIR / 'static'), name='static')

templates = Jinja2Templates(directory=BASE_DIR / 'static/templates')


@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.post('/products', response_model=Message)
def increment_table(data: Product):
    file_path = Path(BASE_DIR / 'data/tabela.xlsx')

    save_product(file_path, data)

    return {'message': 'ok'}
