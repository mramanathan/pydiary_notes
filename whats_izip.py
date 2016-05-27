
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
for country, center in zip(nations, capitals):
    print "Capital of %s is %s" %(country, center)
    
## izipper . . . 
for this, that in izip(nations, capitals):
    print "Capital of %s is %s" %(this, that)