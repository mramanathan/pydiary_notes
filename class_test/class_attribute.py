#!/usr/bin/env python

class myTest(object):
    '''
    Simple blueprint for class, myTest with sample code
    showing howto modify attributes using __class__
    '''
    
    test_x = 17
    
intVals = myTest()

print "Attributes of intVals class : "
print intVals.test_x

newInts = myTest()

print "Attributes of newInts class : "
print newInts.test_x

## via object, intVals, now change the attribute test_x defined in myTest
intVals.__dict__["test_x"] = "Orange"
print "modified attribute of test_x is, ", intVals.test_x
## now change the attribute test_x defined in myTest but directly
## why this isn't working ???
''' myTest.__class__.__dict__["test_x"] = "Orange"
print newInts.test_x '''

myVals = myTest()
print myVals.test_x