"""
"""

from constants import *
from population import initial_population


SIZE_PPL = 10
DIM = 10


if __name__ == "__main__":
    ppl = initial_population(BIN, SIZE_PPL, DIM)
    print(ppl)

    ppl = initial_population(INT, SIZE_PPL, DIM)
    print(ppl)

    ppl = initial_population(REAL, SIZE_PPL, DIM)
    print(ppl)

    ppl = initial_population(INT_PERM, SIZE_PPL, DIM)
    print(ppl)