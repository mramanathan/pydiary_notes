#!/usr/bin/env python

class myTest(object):
    '''
    Simple blueprint for class, myTest
    '''
    
    test_x = 17
    
intVals = myTest()

print "Attributes of intVals class : "
print intVals.test_x

# attribute created outside the class definition
# it's accessible to only intVals object
# uncomment newInts.test_y to run the program and check this
intVals.test_y= 29

print intVals.test_y

newInts = myTest()

print "Attributes of newInts class : "
print newInts.test_x
#print newInts.test_y