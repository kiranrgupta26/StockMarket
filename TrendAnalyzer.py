class TrendAnalyzer:
    def get_trend(self,stockdata):
        # Trend of previous two day
        currdata = stockdata[1]
        prevdata = stockdata[2]
        trend = 0
        if currdata.close < currdata.open and prevdata.close < prevdata.open:
            trend = 0
        elif currdata.open < currdata.close and prevdata.open < prevdata.close:
            trend = 1
        return trend