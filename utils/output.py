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

def printResult(flightsService, bestIndividual, toRome):
    print("\nMelhor custo: R$", bestIndividual.cost)
    print("Com máximo tempo de espera de:", toHours(bestIndividual.maxWaitingTime()))
    print("\nCom voos:")
    for key, value in bestIndividual.indexes.items():
        if toRome:
            printDepartureAndArriveToRome(flightsService, key, value)
        else:
            printDepartureAndArriveFromRome(flightsService, key, value)
