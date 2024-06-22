import matplotlib.pyplot
plt = matplotlib.pyplot

from utils.flightsService import Flights
from gaProperties.ga import GA
from utils.output import printResult

def main():
    flightsService = Flights()
    locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
    toRome = True
    ga = GA(flightService=flightsService, locales=locales, toRome=toRome, kRatio=0.75, crossOverRatio=0.8, mutationRatio=0.10, elitism=4)

    print("Population created, with size of", len(ga.population))

    bestIndividuals = ga.getBestIndividuals()
    print("Melhor Indivíduo inicial tem custo:", bestIndividuals[0].getTotalCost(), "e fitness", bestIndividuals[0].fitness())

    genQuantity = 100

    bestResults = []
    mediumResults = []
    worstResults = []
    x = list(range(1, genQuantity+1))

    for i in range(genQuantity):
        print("Geração", i)
        print("Melhor fitness: ", ga.getBestIndividuals()[0].fitness())
        bestResults.append(ga.population[0].fitness())
        mediumResults.append(ga.population[49].fitness())
        worstResults.append(ga.population[99].fitness())
        ga.newPopulation()
        print("Finalizada")

    plt.plot(x, bestResults, label = "Melhor Resultado") 
    plt.plot(x, mediumResults, label = "Médio Resultado") 
    plt.plot(x, worstResults, label = "Pior Resultado") 
    plt.legend() 
    plt.show()

    for i in range(20):
        print(ga.population[i].fitness())

    bestIndividual = ga.getBestIndividuals()[0]
    print("Melhor Indivíduo final tem custo:", bestIndividual.getTotalCost(), "e fitness", bestIndividual.fitness())
    printResult(flightsService, bestIndividual)
        


if __name__ == "__main__":
    main()