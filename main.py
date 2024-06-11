from utils.flightsService import Flights
from gaProperties.individual import Individual
from gaProperties.ga import GA

def main():
    flightsService = Flights()
    ga = GA()
    population = []
    for i in range(100):
        population.append(Individual(flightsService))

    print("Population created, with size of", len(population))

    for individual in population:
        print(individual.cost)

    print("Best individual has a cost of", ga.bestIndividual(population).cost, "and a max waiting time of", ga.bestIndividual(population).maxWaitingTime())

if __name__ == "__main__":
    main()