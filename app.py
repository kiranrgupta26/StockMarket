import flask
import uvicorn
from flask import request
from fastapi import FastAPI
from models import StockInput

from DataHandler import DataHandler
from StockData import StockData

app = flask.Flask(__name__)
#app =  FastAPI()

@app.route('/')
def hello():
    msg = "Docker Works"
    return msg

#App routing
@app.post('/pattern/stock')
def getstockpattern():
#async def getstockpattern(inp:StockInput):
    # ticker = inp.ticker
    # api_key = "c102ba52a69f4c859f231c77c9ddb198"
    # timespan = inp.time

    data = request.get_json()
    ticker = data["ticker"]
    api_key = "c102ba52a69f4c859f231c77c9ddb198"
    timespan = data["time"]

    data_handler = DataHandler()
    results = data_handler.get_stock_prices(ticker, api_key,timespan)
    print("Flask Appications")
    return results

if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)
    #uvicorn.run(app,host = "0.0.0.0",port=5000)



