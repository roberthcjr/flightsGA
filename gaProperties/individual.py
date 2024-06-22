import random
from utils.flightsService import Flights

class Individual:
    def __init__ (self, flightsService:Flights=None, locales=None, toRome=None, l=None):
        if l == None:
            self.flightsService = flightsService
            self.toRome = toRome
            self.localesIndexes = {}
            for locale in locales:
                randIndex = None
                if toRome:
                    randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "from") - 1)
                else:
                    randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "to") - 1)

                self.localesIndexes[locale] = randIndex
        else:
            self.localesIndexes = l
            self.toRome = toRome
            self.flightsService=flightsService

    def getFlightsTime(self):
        flights = []
        for locale, index in self.localesIndexes.items():
            if self.toRome:
                flights.append(self.flightsService.getFlightArrivalInMin(locale, index))
            else:
                flights.append(self.flightsService.getFlightDepartureInMin(locale, index))

        return flights
    
    def getTotalCost(self):
        totalCosts = 0
        for locale, index in self.localesIndexes.items():
            if self.toRome:
                totalCosts += self.flightsService.getFlightCost(locale, index, "from")
            else:
                totalCosts += self.flightsService.getFlightCost(locale, index, "to")

        return totalCosts
    
    def maxWaitingTime(self):
        flights = self.getFlightsTime()
        return max(flights) - min(flights)
    
    def fitness(self):
        return self.getTotalCost() + self.maxWaitingTime() * 10
    