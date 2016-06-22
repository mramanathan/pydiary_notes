
# coding: utf-8

# ####### 27/May/2016: 
# ##### ===========
# ** zip, izip play ground

""" What's this thing about zip and izip ?

zip is better or izip ?

"""

nations = ['Brazil', 'Russia', 'India', 'China']
capitals = ['Brasilia', 'Moscow', 'New Delhi', 'Beijing']

### zipper . . .
print "==" * 10,
print "print and zip using a for loop"
for country, center in zip(nations, capitals):
    print "Capital of %s is %s" %(country, center)
print "==" * 10

# repeat of the above for loop in a single print
print "==" * 10,
print "print and zip in a single line of python code"
print(list(zip(*(nations, capitals))))
print "==" * 10
    
## izipper . . . 
for this, that in izip(nations, capitals):
    print "Capital of %s is %s" %(this, that)