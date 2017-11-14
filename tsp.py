'''TSP problem in python3 with DEAP'''
# meta block
__author__ = "Steven Porretta"
__version__ = "0.0.1"
__maintainer__ = "Steven Porretta"
__email__ = "stevenporretta@scs.carleton.ca"
__status__ = "Development"

import array
import random
import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# Import my TSP stuff
from distance import *
from parser import *

# Create a new TSP
eil51 = Parser("eil51.tsp")
citylist = eil51.city_coords
# print(len(citylist))
# citylist = zip(citylist.get(1)[:-1], citylist.get(1)[1:])
# for u, v in citylist:
#     print(u)
#     print(v)
tours = TSPDistance(eil51.city_tour_init, eil51.city_coords)
distance_map = tours.distance_map
IND_SIZE = int(eil51.dimension)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i',
               fitness=creator.FitnessMin)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i',
               fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

# Structure initializers
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalTSP(individual):
    distance = distance_map[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distance += distance_map[gene1][gene2]
    return distance,


toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)


def main():
    random.seed(169)

    pop = toolbox.population(n=100000)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg_dist", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min_dist", numpy.min)
    stats.register("max_dist", numpy.max)

    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 1000, stats=stats,
                        halloffame=hof)
    print('')
    return pop, stats, hof


if __name__ == "__main__":
    main()
