from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from simulator import execute

app = FastAPI()
templates = Jinja2Templates(directory="templates")

run_simulator = execute

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Read the default code from a file
    with open("default_code.s", "r") as file:
        default_code = file.read()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "default_code": default_code,
            "result": None,
            "execution_info": None,
            "memory_info": None,
        }
    )

@app.post("/execute", response_class=HTMLResponse)
async def execute_code(request: Request, code: str = Form(...)):
    result, execution_info, memory_info = run_simulator(code.split('\n'))
    print(result, execution_info, memory_info)

    return templates.TemplateResponse(
        "output.html",
        {
            "request": request,
            "result": result,
            "execution_info": execution_info,
            "memory_info": memory_info,
        }
    )

