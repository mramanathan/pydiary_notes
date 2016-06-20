#!/usr/bin/env python

# -*- coding:utf-8 -*-

import re

""" 
Short example for usage of regex ?P ;
See this thread for more explanation on 'named regular expression':
http://stackoverflow.com/questions/10059673/named-regular-expression-group-pgroup-nameregexp-what-does-p-stand-for
"""

leader = "Mohandas Karamchand Gandhi"

m = re.match(r"(?P<first_name>\w+) (?P<middle_name>\w+) (?P<last_name>\w+)", leader)

print "==" * 10
print("Mahatma's first name : %s" %(m.group('first_name')))
print("Mahatma's second name : %s" %(m.group('middle_name')))
print("Mahatma's last name : %s" %(m.group('last_name')))
print "==" * 10