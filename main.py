from utils.flightsService import Flights
from gaProperties.ga import GA
from utils.output import printResult

def main():
    flightsService = Flights()
    ga = GA(flightsService, 0.75)

    locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
    toRome = False

    population = ga.createPopulation(locales, toRome)

    print("Population created, with size of", len(population))

    bestIndividual = ga.bestIndividual(population)

    printResult(flightsService, bestIndividual, toRome)
        


if __name__ == "__main__":
    main()