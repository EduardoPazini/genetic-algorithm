"""
"""

class Single:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    def __repr__(self):
        return "\n%s" % (self.chromosome)
        
    def __str__(self):
        return "<Test single:%s" % (self.chromosome)
