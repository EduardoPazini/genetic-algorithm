"""
"""

class Single:
    """
    @staticmethod
    def fitness(chromosome):
        return 0
    """

    def __init__(self, chromosome, calculateFitness=True):
        self.chromosome = chromosome
        """
        if calculateFitness:
            self.fitness = Single.fitness(chromosome)
        #self.randomFitness = self.fitness
        """

    def __repr__(self):
        return "\n%s" % (self.chromosome)
        
    def __str__(self):
        return "<Test a:%s b:%s>" % (self.a, self.b)
