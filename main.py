from utils.flightsService import Flights
from gaProperties.ga import GA
from utils.output import printResult

def main():
    flightsService = Flights()
    locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
    toRome = True
    ga = GA(flightService=flightsService, locales=locales, toRome=toRome, kRatio=0.75, crossOverRatio=0.8, mutationRatio=0.05, elitism=4)

    print("Population created, with size of", len(ga.population))

    bestIndividuals = ga.bestIndividuals
    print("Melhor Indivíduo inicial tem custo:", bestIndividuals[0].getTotalCost(), "e fitness", bestIndividuals[0].fitness())
    for i in range(100):
        print("Geração", i)
        print("Melhor fitness: ", ga.bestIndividuals[0].fitness())
        ga.newPopulation()
        print("Finalizada")

    bestIndividual = ga.bestIndividuals[0]
    print("Melhor Indivíduo final tem custo:", bestIndividual.getTotalCost(), "e fitness", bestIndividual.fitness())
    printResult(flightsService, bestIndividual)
        


if __name__ == "__main__":
    main()