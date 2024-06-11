class GA:
    def fitness(self, individual):
        return individual.cost + individual.maxWaitingTime() * 10
    
    def bestIndividual(self, population):
        best = population[0]
        for individual in population:
            if self.fitness(individual) < self.fitness(best):
                best = individual
        return best