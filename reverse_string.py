# _*_ coding: utf-8 _*_

#!/usr/bin/env python

def revStr(mystr):
	''' Reverses the input string and the case too '''
	''' KeYs shall become SyEk '''
	''' Zalando Interview '''

	newstr = []

	print("String to reverse : {}".format(mystr))

	for i in mystr:
		if i.isupper():
			newstr.append(i.lower())
		else:
			newstr.append(i.upper())

	
	print("String to reverse : {}".format(newstr))
	print("Reversed string : {}".format("".join(newstr)[::-1]))

	return None



def main():

	input_str = "codERpAd iS HoT"

	revStr(input_str)



if __name__ == "__main__":
	main()
