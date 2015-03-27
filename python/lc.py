################################################################################
# 
# Linear Counting algorithm fun
#
# References:
# - https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures
#   -web-analytics-data-mining/
# - Whang,K.-Y., Vander-Zanden, B., and Taylor, H. A Linear-Time Probablistic
#   Counting Algorithm for Database Applications
#
################################################################################

import math
import sys

class LinearCounter:
    """ Linear Counting algorithm methods """

    # BitSet variable
    # BitSet mask variable 
    m = 0
    bitset = []
    dataset = []

    def __init__(self, mask):
        self.m = mask
        self.bitset = [0]*self.m

    def add(self, value): 
        # Apply hash function to value and add to BitSet
        pos = self.hash(value)
        self.bitset[pos] = 1

    def hash(self, value):
        # Compute ascii value % m
        asciisum = 0
        for i in range(0, len(value)):
            asciisum += ord(value[i])
        return asciisum % self.m

    def process(self, data):
        # Compute bitset for given dataset
        self.dataset = data
        for element in data:
            self.add(element)

    def cardinality(self):
        # Compute expected and actual cardinality from bitset and dataset
        expected = len(set(self.dataset))
        frac = self.bitset.count(0)/float(self.m)
        actual = -1.0 * self.m * math.log(frac) 
        return expected, actual


if __name__=='__main__':
    mask = int(sys.argv[1]) 
    # Example dataset from paper
    data = ["Harry", "Joe", "Bill", "Harry", "Paul", "Arthur", "Karen", 
        "Mike", "Chris", "Cathy", "Norm", "Brian"]
    lc = LinearCounter(mask)
    lc.process(data)
    e, a = lc.cardinality()

    print "Linear counting: m = %d, hash = ascii value computation" % mask
    print "Linear counting cardinality: expected = %s, actual = %s" % (str(e), str(a)) 
 
