import random

class Individual:
    def __init__ (self, flightsService):
        self.flightsService = flightsService
        self.locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
        self.arrivals = []
        self.cost = 0
        for locale in self.locales:
            randIndex = random.randint(0, self.flightsService.maxDFSize(locale) - 1)
            self.arrivals.append(self.flightsService.getFlightArrival(locale, randIndex))
            self.cost += self.flightsService.getFlightCost(locale, randIndex)
    
    def maxWaitingTime(self):
        return max(self.arrivals) - min(self.arrivals)
    