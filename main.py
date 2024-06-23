import copy
from utils.flightsService import Flights
from gaProperties.ga import GA
from utils.output import printResult, csv, plotGraph

def runMultipleGas(quantity, toRome, kRatio, crossOverRatio, mutationRatio, genQuantity):
    bestResultsGACosts = []
    bestResultsGAWaiting = []
    for i in range(quantity):
        print("GA:", i+1)
        results = runGa(toRome, kRatio, crossOverRatio, mutationRatio, genQuantity)
        bestResult = sorted(results["bestResults"], key=lambda individuo: individuo.fitness())[0]
        bestResultsGACosts.append(bestResult.getTotalCost())
        bestResultsGAWaiting.append(bestResult.maxWaitingTime())
    return {
        "bestResultsGACosts": bestResultsGACosts,
        "bestResultsGAWaiting": bestResultsGAWaiting
    }
    
def runGa(toRome, kRatio, crossOverRatio, mutationRatio, genQuantity):
    flightsService = Flights()
    locales = ["LIS", "MAD", "CDG", "DUB", "BRU", "LHR"]
    ga = GA(flightService=flightsService, locales=locales, toRome=toRome, kRatio=kRatio, crossOverRatio=crossOverRatio, mutationRatio=mutationRatio, elitism=4)

    bestIndividual = ga.getBestIndividual()
    print("Melhor Indivíduo inicial tem custo:", bestIndividual.getTotalCost(), "e fitness", bestIndividual.fitness())

    bestResults = []
    mediumResults = []
    worstResults = []

    for i in range(genQuantity):
        print("Geração", i+1)
        print("Melhor fitness: ", ga.getBestIndividual().fitness())
        bestResults.append(copy.deepcopy(ga.getBestIndividual()))
        mediumResults.append(copy.deepcopy(ga.getMediumIndividual()))
        worstResults.append(copy.deepcopy(ga.getWorstIndividual()))
        ga.newPopulation()
        print("Finalizada")

    bestIndividual = ga.getBestIndividual()
    print("Melhor Indivíduo final tem custo:", bestIndividual.getTotalCost(), "e fitness", bestIndividual.fitness())
    printResult(flightsService, bestIndividual)

    return {
        "bestResults": bestResults,
        "mediumResults": mediumResults,
        "worstResults": worstResults
    }


def main():
    toRome = False
    kRatio = 0.65
    crossOverRatio = 0.8
    mutationRatio = 0.25
    genQuantity = 200
    results = runGa(toRome=toRome, kRatio=kRatio, crossOverRatio=crossOverRatio, mutationRatio=mutationRatio, genQuantity=genQuantity)
    plotGraph(results=results)
    # results = runMultipleGas(quantity=30, toRome=toRome, kRatio=kRatio, crossOverRatio=crossOverRatio, mutationRatio=mutationRatio, genQuantity=genQuantity)
    # plotGraph(results=results, isPoint=True)
if __name__ == "__main__":
    main()