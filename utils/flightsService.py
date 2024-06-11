import pandas as pd

class Flights:
    def __init__(self):
        self.fullDf = pd.read_csv('database/flights.txt',
                             names=["from", "to", "departure", "arrival", "price"])
        
        self.fullDf["arrival"] = pd.to_datetime(self.fullDf["arrival"]).dt.hour * 60 + pd.to_datetime(self.fullDf["arrival"]).dt.minute

    def getFlightCost(self, locale, index):
        return self.fullDf[self.fullDf["from"] == locale].iloc[index]["price"]
    
    def getFlightArrival(self, locale, index):
        return self.fullDf[self.fullDf["from"] == locale].iloc[index]["arrival"]
    
    def maxDFSize(self, locale):
        return len(self.fullDf[self.fullDf["from"] == locale])



    