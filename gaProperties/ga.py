from gaProperties.individual import Individual

class GA:

    def __init__(self, flightService):
        self.flightService = flightService

    def fitness(self, individual):
        return individual.cost + individual.maxWaitingTime() * 10
    
    def bestIndividual(self, population):
        best = population[0]
        for individual in population:
            if self.fitness(individual) < self.fitness(best):
                best = individual
        return best
    
    def createPopulation(self, locales, toRome, size=100):    
        if not callable(Individual):
            raise ValueError("`Individual` deve ser uma classe ou uma função que cria instâncias.")
        
        if not locales:
            raise ValueError("O parâmetro `locales` não deve estar vazio.")
        
        return [Individual(self.flightService, locales, toRome) for _ in range(size)]