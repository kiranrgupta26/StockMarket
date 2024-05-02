import requests

from PatternAnalyzer import PatternAnalyzer
from PatternDataHandler import PatternDataHandler
from StockData import StockData
from TrendAnalyzer import TrendAnalyzer


class DataHandler:
    ticker = "MSFT"
    api_key = "c102ba52a69f4c859f231c77c9ddb198"

    def get_json_data(self):
        data = {
            'meta': {'symbol': 'MSFT', 'interval': '1day', 'currency': 'USD', 'exchange_timezone': 'America/New_York',
                     'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'type': 'Common Stock'}, 'values': [
                {'datetime': '2024-03-28', 'open': '420.95999', 'high': '421.87000', 'low': '419.12000',
                 'close': '420.72000',
                 'volume': '21871161'},
                {'datetime': '2024-03-27', 'open': '424.44000', 'high': '424.45001', 'low': '419.01001',
                 'close': '421.42999',
                 'volume': '16704978'},
                {'datetime': '2024-03-26', 'open': '425.60999', 'high': '425.98999', 'low': '421.35001',
                 'close': '421.64999',
                 'volume': '16725647'},
                {'datetime': '2024-03-25', 'open': '425.23999', 'high': '427.41000', 'low': '421.60999',
                 'close': '422.85999',
                 'volume': '18060450'},
                {'datetime': '2024-03-22', 'open': '429.70001', 'high': '429.85999', 'low': '426.07001',
                 'close': '428.73999',
                 'volume': '17648473'},
                {'datetime': '2024-03-21', 'open': '429.82999', 'high': '430.82001', 'low': '427.16000',
                 'close': '429.37000',
                 'volume': '21296222'},
                {'datetime': '2024-03-20', 'open': '422.00000', 'high': '425.95999', 'low': '420.66000',
                 'close': '425.23001',
                 'volume': '17860100'},
                {'datetime': '2024-03-19', 'open': '417.82999', 'high': '421.67001', 'low': '415.54999',
                 'close': '421.41000',
                 'volume': '19837900'},
                {'datetime': '2024-03-18', 'open': '414.25000', 'high': '420.73001', 'low': '413.78000',
                 'close': '417.32001',
                 'volume': '20106000'},
                {'datetime': '2024-03-15', 'open': '419.29001', 'high': '422.60001', 'low': '412.79001',
                 'close': '416.42001',
                 'volume': '45049800'},
                {'datetime': '2024-03-14', 'open': '420.23999', 'high': '427.82001', 'low': '417.98999',
                 'close': '425.22000',
                 'volume': '34157300'},
                {'datetime': '2024-03-13', 'open': '418.10001', 'high': '418.17999', 'low': '411.45001',
                 'close': '415.10001',
                 'volume': '17115900'},
                {'datetime': '2024-03-12', 'open': '407.62000', 'high': '415.57001', 'low': '406.79001',
                 'close': '415.28000',
                 'volume': '22457000'},
                {'datetime': '2024-03-11', 'open': '403.76001', 'high': '405.67999', 'low': '401.26001',
                 'close': '404.51999',
                 'volume': '16120800'},
                {'datetime': '2024-03-08', 'open': '407.95999', 'high': '410.42001', 'low': '404.32999',
                 'close': '406.22000',
                 'volume': '17971700'},
                {'datetime': '2024-03-07', 'open': '406.12000', 'high': '409.78000', 'low': '402.23999',
                 'close': '409.14001',
                 'volume': '18718500'},
                {'datetime': '2024-03-06', 'open': '402.97000', 'high': '405.16000', 'low': '398.39001',
                 'close': '402.09000',
                 'volume': '22344100'},
                {'datetime': '2024-03-05', 'open': '413.95999', 'high': '414.25000', 'low': '400.64001',
                 'close': '402.64999',
                 'volume': '26919200'},
                {'datetime': '2024-03-04', 'open': '413.44000', 'high': '417.35001', 'low': '412.32001',
                 'close': '414.92001',
                 'volume': '17596000'},
                {'datetime': '2024-03-01', 'open': '411.26999', 'high': '415.87000', 'low': '410.88000',
                 'close': '415.50000',
                 'volume': '17800300'},
                {'datetime': '2024-02-29', 'open': '408.64001', 'high': '414.20001', 'low': '405.92001',
                 'close': '413.64001',
                 'volume': '31947300'},
                {'datetime': '2024-02-28', 'open': '408.17999', 'high': '409.29999', 'low': '405.32001',
                 'close': '407.72000',
                 'volume': '13183100'},
                {'datetime': '2024-02-27', 'open': '407.98999', 'high': '408.32001', 'low': '403.85001',
                 'close': '407.48001',
                 'volume': '14835800'},
                {'datetime': '2024-02-26', 'open': '411.45999', 'high': '412.16000', 'low': '407.35999',
                 'close': '407.54001',
                 'volume': '16193500'},
                {'datetime': '2024-02-23', 'open': '415.67001', 'high': '415.85999', 'low': '408.97000',
                 'close': '410.34000',
                 'volume': '16295900'},
                {'datetime': '2024-02-22', 'open': '410.19000', 'high': '412.82999', 'low': '408.57001',
                 'close': '411.64999',
                 'volume': '27009900'},
                {'datetime': '2024-02-21', 'open': '400.17001', 'high': '402.29001', 'low': '397.22000',
                 'close': '402.17999',
                 'volume': '18631100'},
                {'datetime': '2024-02-20', 'open': '403.23999', 'high': '404.48999', 'low': '398.01001',
                 'close': '402.79001',
                 'volume': '24307900'},
                {'datetime': '2024-02-16', 'open': '407.95999', 'high': '408.29001', 'low': '403.44000',
                 'close': '404.06000',
                 'volume': '22281100'},
                {'datetime': '2024-02-15', 'open': '408.14001', 'high': '409.13000', 'low': '404.29001',
                 'close': '406.56000',
                 'volume': '21825500'}], 'status': 'ok'}
        return data

    def get_stock_prices(self,ticker, apiKey,timespan):
        # url = f"https://api.twelvedata.com/time_series?symbol={ticker}&interval={timespan}&apikey={apiKey}"
        # response = requests.get(url).json()
        # print(response)
        response = self.get_json_data()
        stockdata = self.get_stock_data(response)

        trend_analyzer = TrendAnalyzer()
        trend = trend_analyzer.get_trend(stockdata)

        pattern_data_handler = PatternDataHandler()
        allpatterndata = pattern_data_handler.analyzeAllPattern(trend,stockdata)

        return allpatterndata

    def get_stock_data(self,response):
        response = response["values"]
        stockdata = []
        for i in range(len(response)):
            data = StockData(float(response[i]["low"]), float(response[i]["open"]), float(response[i]["close"]), float(response[i]["high"]),
                             response[i]["datetime"])
            stockdata.append(data)

        return stockdata