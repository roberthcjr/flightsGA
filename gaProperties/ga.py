import copy
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
        self.population = [Individual(flightsService=self.flightService, locales=locales, toRome=toRome) for _ in range(size)]
        self.population.sort(key=lambda individuo: individuo.fitness())
    
    def getBestIndividual(self):
        return self.population[0]
    
    def getMediumIndividual(self):
        return self.population[49]
    
    def getWorstIndividual(self):
        return self.population[99]

    def createPool(self):
        competidors = self.population[self.elitism:]
        pool = []
        random.shuffle(competidors)
        print(len(competidors))
        for index in range(0, len(competidors), 2):
            competidor1 = competidors[index]
            competidor2 = competidors[index+1]
            pool.append(self.tournament(competidor1, competidor2))
        return pool
    
    def crossOver(self, individualA:Individual, individualB:Individual):
        crossOverPosition = random.randint(0, random.randint(1,len(individualA.localesIndexes)))
        return {**splitDictBackward(individualB.localesIndexes, crossOverPosition), **splitDictFoward(individualA.localesIndexes, crossOverPosition)}
    
    def makeCrossOver(self, pool):
        newBorns = []
        crossOverPool = pool[:]
        random.shuffle(crossOverPool)
        for index in range(0, len(crossOverPool), 2):
            father = crossOverPool[index]
            mother = crossOverPool[index+1]
            if(random.uniform(0,1) < self.crossOverRatio):
                toRome = father.toRome
                flightsService = father.flightsService
                newBorns.append(Individual(l=self.crossOver(father, mother), toRome=toRome, flightsService=flightsService))
        return newBorns
    
    def mutate(self, individual:Individual):
        locales = list(individual.localesIndexes.keys())
        randLocale = locales[random.randint(0, len(locales)-1)]
        mutatedIndividual = copy.deepcopy(individual)
        randIndex = None
        if(self.toRome):
            randIndex = random.randint(0, self.flightService.maxDFSize(randLocale, "from") - 1)
        else:
            randIndex = random.randint(0, self.flightService.maxDFSize(randLocale, "to") - 1)
        mutatedIndividual.localesIndexes[randLocale] = randIndex
        return mutatedIndividual
    
    def makeMutation(self, pool):
        mutationPool = pool[:]
        mutated = []
        random.shuffle(mutationPool)
        for individual in mutationPool:
            if(random.uniform(0,1) < self.mutationRatio):
                mutated.append(self.mutate(individual))

        return mutated

    def newPopulation(self):
        pool = self.createPool()

        mutated = self.makeMutation(pool)

        crossOver = self.makeCrossOver(pool)

        elite = copy.deepcopy(self.population)[:self.elitism]

        newElitePotential = elite + crossOver + mutated

        newElite = sorted(newElitePotential, key=lambda individuo: individuo.fitness())[:self.elitism]

        self.population = (newElite + self.population)[:self.size]

    def tournament(self, competidor1, competidor2):
        winner = None
        loser = None

        if competidor1.fitness() < competidor2.fitness():
            winner = competidor1
            loser = competidor2
        else:
            winner = competidor2
            loser = competidor1
        
        if random.uniform(0, 1) < self.kRatio:
            return winner
        return loser
