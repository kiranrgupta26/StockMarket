from fastapi import FastAPI
from pydantic import BaseModel

class StockInput(BaseModel):
    ticker : str
    time : str