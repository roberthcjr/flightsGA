import random
from gaProperties.individual import Individual

class GA:

    def __init__(self, flightService, kRatio):
        self.flightService = flightService
        self.kRatio = kRatio
    
    def bestIndividual(self, population):
        best = population[0]
        for individual in population:
            if individual.fitness() < best.fitness():
                best = individual
        return best
    
    def createPopulation(self, locales, toRome, size=100):    
        if not callable(Individual):
            raise ValueError("`Individual` deve ser uma classe ou uma função que cria instâncias.")
        
        if not locales:
            raise ValueError("O parâmetro `locales` não deve estar vazio.")
        
        return [Individual(self.flightService, locales, toRome) for _ in range(size)]