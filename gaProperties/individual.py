import random

class Individual:
    def __init__ (self, flightsService, locales, toRome):
        self.flightsService = flightsService
        self.locales = locales
        self.flightsTime = []
        self.cost = 0
        self.indexes = {}
        for locale in self.locales:
            if toRome:
                randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "from") - 1)
                self.flightsTime.append(self.flightsService.getFlightArrivalInMin(locale, randIndex))
                self.cost += self.flightsService.getFlightCost(locale, randIndex, "from")
            else:
                randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "to") - 1)
                self.flightsTime.append(self.flightsService.getFlightDepartureInMin(locale, randIndex))
                self.cost += self.flightsService.getFlightCost(locale, randIndex, "to")

            self.indexes[locale] = randIndex
    
    def maxWaitingTime(self):
        return max(self.flightsTime) - min(self.flightsTime)
    