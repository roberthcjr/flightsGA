import random
from gaProperties.individual import Individual
from utils.splitter import splitDictBackward, splitDictFoward

class GA:

    def __init__(self, flightService, kRatio, crossOverRatio, mutationRatio, elitism, locales, toRome, size=100):
        self.flightService = flightService
        self.kRatio = kRatio
        self.crossOverRatio = crossOverRatio
        self.mutationRatio = mutationRatio
        self.toRome = toRome
        self.size = size
        self.elitism = elitism
        self.population = [Individual(self.flightService, locales, toRome) for _ in range(size)]
        self.population.sort(key=lambda individuo: individuo.fitness())
        self.bestIndividuals = self.population[:self.elitism]
    
    def tournament(self, competidor1, competidor2):
        winner = None
        loser = None

        if competidor1.fitness() > competidor2.fitness():
            winner = competidor1
            loser = competidor2
        else:
            winner = competidor2
            loser = competidor1
        
        if random.uniform(0, 1) < self.kRatio:
            return winner
        return loser
