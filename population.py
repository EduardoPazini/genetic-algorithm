"""
"""

from constants import *
from single import Single
from random import randint

def random_single(structure_type, dimension):
    chromosome = []
    if structure_type == BIN:
        while dimension > 0:
            chromosome.append(randint(0, 1))
            dimension -= 1
    elif structure_type == INT_PERM:
        aux = [i for i in range(dimension)]
        l = len(aux)
        while l > 0:
            ind = randint(0, l-1)
            chromosome.append(aux[ind])
            aux.pop(ind)
            l -= 1
    elif structure_type == INT:
        pass
    elif structure_type == REAL:
        pass
    return Single(chromosome)

def initial_population(structure_type, size, dimension):
    return [random_single(structure_type, dimension) for _ in range(size)]
