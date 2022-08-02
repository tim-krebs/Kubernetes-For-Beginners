from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": f"From: {os.os.environ.get('ENV', 'DEFAULT_ENV')}"}
