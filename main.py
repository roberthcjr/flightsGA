from utils.flightsService import Flights
from gaProperties.ga import GA
from utils.output import printResult

def main():
    flightsService = Flights()
    locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
    toRome = False
    ga = GA(flightsService, 0.75, locales, toRome)

    print("Population created, with size of", len(ga.population))

    bestIndividual = ga.bestIndividual()

    printResult(flightsService, bestIndividual)
        


if __name__ == "__main__":
    main()