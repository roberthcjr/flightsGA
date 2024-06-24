import copy
import statistics as sts
import numpy as np
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
    mutationRatio = 0.05
    genQuantity = 200
    results = runGa(toRome=toRome, kRatio=kRatio, crossOverRatio=crossOverRatio, mutationRatio=mutationRatio, genQuantity=genQuantity)
    plotGraph(results=results)
    # results = runMultipleGas(quantity=30, toRome=toRome, kRatio=kRatio, crossOverRatio=crossOverRatio, mutationRatio=mutationRatio, genQuantity=genQuantity)
    # plotGraph(results=results, isPoint=True)
    allResults = []
    bestResults = []
    for key in results.keys():
        if key == "bestResults":
            bestResults += results[key]
        allResults += results[key]
    allFitness = [individuo.fitness() for individuo in allResults]
    bestFitness = [individuo.fitness() for individuo in bestResults]

    print("Variancia(todos): ", np.var(allFitness))
    print("Mediana(todos):", np.median(allFitness))
    print("Média(todos):", np.mean(allFitness))
    print("Moda(todos):", sts.mode(allFitness))
    print("Desvio padrão(todos):", np.std(allFitness))

    print("\nVariancia(melhor): ", np.var(bestFitness))
    print("Mediana(melhor):", np.median(bestFitness))
    print("Média(melhor):", np.mean(bestFitness))
    print("Moda(melhor):", sts.mode(bestFitness))
    print("Desvio padrão(melhor):", np.std(bestFitness))
if __name__ == "__main__":
    main()