# import dependencies
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# create app instance
app = FastAPI()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/advice.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("advice.html", {"request": request})

@app.get("/params.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("params.html", {"request": request})



app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)