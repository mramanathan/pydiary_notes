#!/usr/bin/env python

class House(object):
    
    family_name = "Rams"
    total_number_of_houses = 0
    
    def __init__(self, city, nature, amount = 0, years = 0):
        self.house_location = city
        self.house_type     = nature
        self.month_rent     = amount
        self.stay_period    = years
        
        House.total_number_of_houses += 1
        
    def calcRent(self):
        if self.stay_period >= 1:
            return self.month_rent * (12 * self.stay_period)
        else:
            return self.month_rent * self.stay_period
        
    def ownStay(self):
        if self.stay_period >= 1:
            return self.stay_period * 12
        else:
            return self.stay_period
    
amb_flat = House("Chennai", "own", 5)
mog_flat = House("Chennai", "own", 4)
blr_1146 = House("Bangalore", "rent", 6500, 2)
print "Total rent paid : %d" %(blr_1146.calcRent())
blr_1374 = House("Bangalore", "rent", 10000, 1)
print "Total rent paid : %d" %(blr_1374.calcRent())
blr_1249 = House("Bangalore", "rent", 5000, 1)
print "Total rent paid : %d" %(blr_1249.calcRent())
blr_936 = House("Bangalore", "rent", 16000, 2)
print "Total rent paid : %d" %(blr_936.calcRent())
blr_937 = House("Bangalore", "rent", 20000, 1)
print "Total rent paid : %d" %(blr_937.calcRent())
blr_1143 = House("Bangalore", "own", 1)

print "%s family has stayed in %d houses across different cities." %(House.family_name,  House.total_number_of_houses)
print "Sum of rent paid in all the rental houses : %d" %(blr_1146.calcRent() + blr_1374.calcRent() + blr_1249.calcRent() + blr_936.calcRent() + blr_937.calcRent()) 
print "%s family has stayed in their own house for %d months in all." %(House.family_name, amb_flat.ownStay() + mog_flat.ownStay() + blr_1143.ownStay())