#!/usr/bin/env python

# -*- coding:utf-8 -*-

import unittest
from rental import Rental

class RentalTest(unittest.TestCase):
    
    def test_empty(self):
        h = Rental()
        assert h.cost() == 0.0
        
    def test_one_house(self):
        h = Rental()
        h.house("Bangalore", 1146, 6000, 2)
        # we are blind to the actual cost computed via h.cost() method
        assert h.cost() == 144000.0

    def test_two_houses(self):
        h = Rental()
        h.house("Bangalore", 1146, 6000, 2)
        h.house("Bangalore", 937, 20000, 2)
        # This kind of 'assert' will help us know what the actual computed cost was
        self.assertEqual(h.cost(), 624000.0)
        
    def test_all_houses(self):
        h = Rental()
        h.house("Bangalore", 1146, 6000, 2)
        h.house("Bangalore", 1311, 9000, 1)
        h.house("Bangalore", 1519, 5000, 1)
        h.house("Bangalore", 936, 17000, 2)
        h.house("Bangalore", 937, 20000, 2)
        self.assertEqual(h.cost(), 1200000.0)


"""
rental code tested without unitest

h = Rental()

print("Cost of house not rented should be 0.0: %s" % h.cost())
assert h.cost() == 0.0
h.house("Bangalore", 1146, 6000, 2)
print("Rental cost of 1146@Bangalore rented at 6000 for 2 years: %s" % h.cost())
assert h.cost() == 144000.0
h.house("Bangalore", 937, 2000, 2)
print("Rental cost of 937@Bangalore rented at 2000 for 2 years: %s" % h.cost())
assert h.cost() == 192000.0
"""