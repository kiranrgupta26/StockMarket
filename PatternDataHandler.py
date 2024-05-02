from PatternAnalyzer import PatternAnalyzer


class PatternDataHandler:
    pattern_analyzer = PatternAnalyzer()
    allPatternData = []
    def analyzeAllPattern(self,trend,stockdata):
        if trend==0:
            data = self.pattern_analyzer.isPiercingLine(stockdata)
            self.allPatternData.append(data)
            # print("Piercing Line ",data)
            # data = self.pattern_analyzer.isInvertedHammer(stockdata)
            # print("Inverted Hammer ",data)
            data = self.pattern_analyzer.isHaramiCrossBullish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isHaramiBullish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isEngulfingBullish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isMorningStar(stockdata)
            self.allPatternData.append(data)

            #Continuation Patter
            data = self.pattern_analyzer.isDownsideTasukiGap(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isSideBySideWhiteLinesBearish(stockdata)
            self.allPatternData.append(data)

        #trend 1 means upward
        elif trend==1:
            data = self.pattern_analyzer.isDarkCloudCover(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isHaramiCrossBearish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isHaramiBearish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isEngulfingBearish(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isEveningStar(stockdata)
            self.allPatternData.append(data)

            #Continuation Pattern
            data = self.pattern_analyzer.isUpsideTasukiGap(stockdata)
            self.allPatternData.append(data)

            data = self.pattern_analyzer.isSideBySideWhiteLinesBullish(stockdata)
            self.allPatternData.append(data)

        return self.allPatternData
