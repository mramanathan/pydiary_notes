#!/usr/bin/env python

class House(object):
    
    family_name = "Rams"
    total_number_of_houses = 0
    
    def __init__(self, city, nature, amount):
        self.house_location = city
        self.house_type     = nature
        self.house_rent     = amount
        
        House.total_number_of_houses += 1
        
amb_flat = House("Chennai", "own", 0)
mog_flat = House("Chennai", "own", 0)
blr_1146 = House("Bangalore", "rent", 6500)
blr_1374 = House("Bangalore", "rent", 10000)
blr_1249 = House("Bangalore", "rent", 5000)
blr_936 = House("Bangalore", "rent", 16000)
blr_937 = House("Bangalore", "rent", 20000)
blr_1143 = House("Bangalore", "own", 0)

print "%s family has stayed in %d houses across different cities." %(House.family_name,  House.total_number_of_houses)