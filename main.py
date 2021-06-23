"""
"""

from constants import *
from population import initial_population


SIZE_PPL = 20
DIM = 7


if __name__ == "__main__":
    ppl = initial_population(BIN, SIZE_PPL, DIM)
    #ppl = initial_population(INT_PERM, SIZE_PPL, DIM)
    print(ppl)
