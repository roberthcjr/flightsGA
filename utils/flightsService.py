from utils.translator import readTxt, toMinutes

class Flights:
    def __init__(self):
        self.fullDf = readTxt('database/flights.txt', ["from", "to", "departure", "arrival", "price"])
        
        self.fullDf["arrivalInMin"] = toMinutes(self.fullDf, "arrival")
        self.fullDf["departureInMin"] = toMinutes(self.fullDf, "departure")

    def getFlightCost(self, locale, index, column):
        return self.fullDf[self.fullDf[column] == locale].iloc[index]["price"]
    
    def getFlightArrivalInMin(self, locale, index):
        return self.fullDf[self.fullDf["from"] == locale].iloc[index]["arrivalInMin"]
    
    def getFlightDepartureInMin(self, locale, index):
        return self.fullDf[self.fullDf["to"] == locale].iloc[index]["departureInMin"]
    
    def getFlightDeparture(self, locale, index):
        return self.fullDf[self.fullDf["from"] == locale].iloc[index]["departure"]
    
    def getFlightArrival(self, locale, index):
        return self.fullDf[self.fullDf["from"] == locale].iloc[index]["arrival"]
    
    def maxDFSize(self, locale, column):
        return len(self.fullDf[self.fullDf[column] == locale])



    