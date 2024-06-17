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
    
    def newPopulation(self, locales, toRome):
        newPopulation = []
        father = self.tournament()
        mother = self.tournament()
        while mother == father:
            father = self.tournament()

    def tournament(self, population):
        competitor1 = population[random.randint(0, len(population) - 1)]
        competitor2 = population[random.randint(0, len(population) - 1)]

        while competitor1 == competitor2:
            competitor2 = population[random.randint(0, population.len() - 1)]

        bestCompetitor = None
        worstCompetitor = None

        if competitor1.fitness() > competitor2.fitness():
            bestCompetitor = competitor1
            worstCompetitor = competitor2
        else:
            bestCompetitor = competitor2
            worstCompetitor = competitor1
        
        if random.uniform(0, 1) < self.kRatio:
            return bestCompetitor
        return worstCompetitor
