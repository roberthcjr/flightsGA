import csv

from matplotlib import pyplot as plt
from utils.translator import fullNameLocales, toHours

def printDepartureAndArriveToRome(flightsService, key, value):
    print("Saindo de", fullNameLocales[key], "indo até Roma com saída em:")
    print(flightsService.getFlightDeparture(key, value))
    print("E chegada em:")
    print(flightsService.getFlightArrival(key, value))

def printDepartureAndArriveFromRome(flightsService, key, value):
    print("Saindo de Roma indo até", fullNameLocales[key], "com saída em:")
    print(flightsService.getFlightDeparture(key, value))
    print("E chegada em:")
    print(flightsService.getFlightArrival(key, value))

def printResult(flightsService, bestIndividual):
    print("\nMelhor custo: R$", bestIndividual.getTotalCost())
    print("Com máximo tempo de espera de:", toHours(bestIndividual.maxWaitingTime()))
    print("\nCom voos:")
    for key, value in bestIndividual.localesIndexes.items():
        if bestIndividual.toRome:
            printDepartureAndArriveToRome(flightsService, key, value)
        else:
            printDepartureAndArriveFromRome(flightsService, key, value)

def writeCSV(results):
      with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for result in results:
            spamwriter.writerow(results)

def plotGraph(results, isPoint=False):
    if not isPoint:
        for key in results.keys():
            x = list(range(1, len(results[key])+1))
            plt.plot(x, [value.fitness() for value in results[key]], label = key)
    else:
        values = list(results.values())
        print(values[0])
        print(values[1])
        plt.figure(figsize=(10, 6))
        plt.scatter(values[1], values[0], marker='o', color='r', label='Pontos')
        plt.xlim(0, 500)
        plt.ylim(0, 4000)
        plt.grid(True)
    plt.legend()
    plt.show()
