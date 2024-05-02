class PatternAnalyzer:
    def isPiercingLine(self, stockdata):
        # first check if downtrend before curr date
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        # Then check if today is white body
        if curr_data.open < curr_data.close:
            # open below the low of previous day
            if curr_data.open < prev_data.low:
                # and close above the midpoint of previous day
                if ((prev_data.open + prev_data.close) / 2) <= curr_data.close < prev_data.open:
                    return {"Trend":1,"Pattern":"Piercing Line Bullish Reversal","Description":"Trend Will Go Up"}
        return {"Trend":0,"Pattern":"Piercing Line Bullish Reversal","Description":"Not a Bullish Reversal"}

    def isDarkCloudCover(self, stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        # Second day is the black body
        if curr_data.open > curr_data.close:
            # opens above the high of previous day
            if curr_data.open > prev_data.high:
                # closes below midpoint of prev day
                if ((prev_data.open + prev_data.close) / 2) >= curr_data.close > prev_data.open:
                    return {"Trend":1,"Pattern":"Dark CLoud Cover Bearish Reversal","Description":"Trend Will Go Down"}
        return {"Trend":0,"Pattern":"Dark Cloud Cover Bearish Reversal","Description":"Not a Bearish Reversal"}

    # def isInvertedHammer(self, stockdata):
    #     curr_data = stockdata[0]
    #     prev_data = stockdata[1]
    #
    #     if ((curr_data.high - curr_data.open) >= 2 * (curr_data.open - curr_data.close) and
    #             curr_data.close == curr_data.low and
    #             curr_data.open < (prev_data.open + prev_data.close) / 3):
    #         return 1
    #     return 0

    def isHaramiCrossBullish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        # Check if curr day is Doji
        if (0.97* curr_data.open <=curr_data.close <= 1.05* curr_data.open):
            if curr_data.low >= prev_data.low and curr_data.high <= prev_data.high:
                return {"Trend":1,"Pattern":"Harami Cross","Description":"It is Bullish Reversal"}
        return {"Trend":0,"Pattern":"Harami Cross","Description":"Not a Bullish Reversal"}

    def isHaramiCrossBearish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        # Check if curr day is Doji
        if (0.97* curr_data.open <=curr_data.close <= 1.05* curr_data.open):
            if curr_data.low >= prev_data.low and curr_data.high <= prev_data.high:
                return {"Trend":1,"Pattern":"Harami Cross","Description":"It is Bearish Reversal"}
        return {"Trend":0,"Pattern":"Harami Cross","Description":"Not a Bearish Reversal"}

    def isHaramiBullish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        #check if it is a white body
        if curr_data.close > curr_data.open:
            if curr_data.open > prev_data.close and curr_data.close < prev_data.open:
                return {"Trend":1,"Pattern":"Harami","Description":"It is Bullish Reversal"}

        return {"Trend":0,"Pattern":"Harami","Description":"Not A Bullish Reversal"}

    def isHaramiBearish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        #check if it is a white body
        if curr_data.close < curr_data.open:
            if curr_data.open < prev_data.close and curr_data.close > prev_data.open:
                return {"Trend":1,"Pattern":"Harami","Description":"It is Bearish Reversal"}

        return {"Trend":0,"Pattern":"Harami","Description":"Not A Bearish Reversal"}

    def isEngulfingBullish(self, stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        #Check if it engulf prev day
        if curr_data.open < prev_data.close and curr_data.close> prev_data.open:
            return {"Trend": 1, "Pattern": "Bullish Engulfing", "Description": "It is A Bullish Reversal"}
        return {"Trend": 0, "Pattern": "Engulfing", "Description": "Not A Bullish Reversal"}

    def isEngulfingBearish(self, stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]

        # Check if it engulfs prev day
        if curr_data.open > prev_data.close and curr_data.close < prev_data.open:
            return {"Trend": 1, "Pattern": "Bearish Engulfing", "Description": "It is A Bearish Reversal"}
        return {"Trend": 0, "Pattern": "Engulfing", "Description": "Not A Bearish Reversal"}

    def isMorningStar(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        #prev day gaps lower
        if prev_data.open < prev_prev_data.close:
            #curr day is white body
            if curr_data.open < curr_data.close:
                if curr_data.open > prev_data.open:
                    return {"Trend": 1, "Pattern": "Morning Star", "Description": "It is A Bullish Reversal"}
        return {"Trend": 0, "Pattern": "Morning Star", "Description": "Not a Bullish Reversal"}

    def isEveningStar(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        # prev day gaps
        if prev_data.open > prev_prev_data.close:
            #Third day is black day
            if curr_data.open > curr_data.close:
                if curr_data.open < prev_data.open:
                    return {"Trend": 1, "Pattern": "Evening Star", "Description": "It is A Bearish Reversal"}
        return {"Trend": 0, "Pattern": "Evening Star", "Description": "Not A Bearish Reversal"}

    #Continuation Pattern
    def isUpsideTasukiGap(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        if prev_data.open > prev_prev_data.close:
            #Current day is black day
            if curr_data.close < curr_data.open:
                if prev_data.close > curr_data.open > prev_data.open :
                    if prev_prev_data.close < curr_data.close <prev_data.open:
                        return {"Trend": 1, "Pattern": "Upside Tasuki Gap", "Description": "It is A Bullish Continuation"}
        return {"Trend": 0, "Pattern": "Upside Tasuki Gap", "Description": "Not A Bullish Continuation"}


    def isDownsideTasukiGap(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        if prev_data.open < prev_prev_data.close:
            # Current day is black day
            if curr_data.close > curr_data.open:
                if prev_data.close < curr_data.open < prev_data.open:
                    if prev_prev_data.close > curr_data.close > prev_data.open:
                        return {"Trend": 1, "Pattern": "Downside Tasuki Gap",
                                "Description": "It is A Bearish Continuation"}
        return {"Trend": 0, "Pattern": "Downside Tasuki Gap", "Description": "Not A Bearish Continuation"}

    def isSideBySideWhiteLinesBullish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        if prev_data.open > prev_prev_data.close:
            #2nd and 3rd open at almost same price
            if curr_data.open >= prev_data.open:
                return {"Trend": 1, "Pattern": "Side By Side White Lines",
                        "Description": "It is A Bullish Continuation"}
        return {"Trend": 0, "Pattern": "Side By Side White Lines",
                "Description": "Not A Bullish Continuation"}


    def isSideBySideWhiteLinesBearish(self,stockdata):
        curr_data = stockdata[0]
        prev_data = stockdata[1]
        prev_prev_data = stockdata[2]

        if prev_data.close < prev_prev_data.close:
            #2nd and 3rd are white body
            if curr_data.close < curr_data.open and prev_data.close > prev_data.open:
                # 2nd and 3rd open at almost same price
                if curr_data.open >= prev_data.open:
                    return {"Trend": 1, "Pattern": "Bearish Side By Side White Lines",
                            "Description": "It is A Bearish Continuation"}
        return {"Trend": 0, "Pattern": "Bearish Side By Side White Lines",
                "Description": "Not A Bearish Continuation"}

