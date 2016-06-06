#!/usr/bin/env python

class Rectangle(object):
    '''
    Simple blueprint to calculate any object of Rectangle 
    shape but the attributes are passed from the object.
    '''
    
    def calcArea(self):
        return self.length * self.width
    
factory = Rectangle()
print factory.__doc__

factory.length, factory.width = 28,13
print "Area of the factory floor : %d" %(factory.calcArea())