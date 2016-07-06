#!/usr/bin/env python

# -*- coding: utf-8 -*-

class Rental(object):
    
    def __init__(self):
        """ alhouses is a list of lists... 
        [[city, name, rent, years] ...]"""
        self.allhouses = []
        
    def house(self, city, doornum, rent, years):
        # In 'city', stayed at 'doornum' for 'years' period paying monthly rent, 'rent'
        self.allhouses.append([city, doornum, rent, years])
        
    def cost(self):
        totalrent = 0.0
        for city, doornum, rent, years in self.allhouses:
            if years >= 1:
                period = years * 12
                totalrent += rent * period
            else:
                totalrent += rent * years
        return totalrent

