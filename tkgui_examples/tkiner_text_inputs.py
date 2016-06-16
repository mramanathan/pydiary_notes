#!/usr/bin/env python

# -*- coding: utf-8 -*-

from Tkinter import *

""" Collect names from the text-boxes and display them. """

def showOutput():
	print(" First Name:%s\n Last Name:%s" % (e1.get(), e2.get()))

master = Tk()

Label(master, text="First Name").grid(row=0)
Label(master, text="Second Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=showOutput).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
