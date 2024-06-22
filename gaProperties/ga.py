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
    
    def newPopulation(self, population):
        newPopulation = population[:]
        father:Individual = self.tournament()
        mother:Individual = self.tournament()
        while mother == father:
            father = self.tournament()

        daughter, son = self.getChild(father, mother)

        newPopulation.append([daughter, son])

        self.population = newPopulation.sort(key=lambda individual:individual.fitness())[:len(self.population)]

    def getChild(self, father:Individual, mother:Individual):
        child1 = self.crossOver(father, mother)
        child2 = self.crossOver(mother, father)

        return child1, child2

    def crossOver(self, individualA:Individual, individualB:Individual, genomeLen):
        crossOverPosition = random.randint(0, genomeLen)
        return splitDictFoward(individualA.localesIndexes, crossOverPosition) + splitDictBackward(individualB)
    

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
