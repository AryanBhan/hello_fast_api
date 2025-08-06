from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/owner")
def read_owner():
    return {"message": "This API Belong to Master Aryan.....😀"}

@app.get("/github")
def redirect_to_github():
    return RedirectResponse(url="https://github.com/AryanBhan/hello_fast_api")

@app.get("/linkedin")
def redirect_to_linkedin():
    return RedirectResponse(url="https://www.linkedin.com/in/aryanbhan/")