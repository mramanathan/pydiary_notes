#!/usr/bin/env python

# -*- coding: utf-8 -*-

from Tkinter import *

""" Get CR # via the text widget and print back on the console. """

def showOutput():
	print(" Check build, review verdicts and state for this CR:%s" % (crid.get()))

master = Tk()

Label(master, text="Enter CR #").grid(row=0)

crid = Entry(master)

crid.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='Show', command=showOutput).grid(row=2, column=1, sticky=W, pady=4)

mainloop()
