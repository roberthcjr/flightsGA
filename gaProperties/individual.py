import random

# TODO: need some repairs, this class doesn't work right now
class Individual:
    def __init (self, flightIndexes):
        self.flightIndexes = flightIndexes

    def __init__ (self, flightsService, locales, toRome):
        self.flightsService = flightsService
        self.localesIndexes = {}
        for locale in locales:
            randIndex = None
            if toRome:
                randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "from") - 1)
            else:
                randIndex = random.randint(0, self.flightsService.maxDFSize(locale, "to") - 1)

            self.localesIndexes[locale] = randIndex
    
    def maxWaitingTime(self):
        return max(self.flightsTime) - min(self.flightsTime)
    
    def fitness(self):
        return self.cost + self.maxWaitingTime() * 10
    