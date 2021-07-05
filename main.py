from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return 'heyy'

