#!/usr/bin/env python

# -*- coding:utf-8 -*-

class Matrix():

    def __init__(self, rows, columns, defaultchar = '@'):

        self.rows = rows
        self.columns = columns

        self.grid = [ [defaultchar] * columns for _ in xrange(rows)]

    def print_matrix(self):

        for row in self.grid:
            print ''.join(row)

    def update_character_in_matrix(self, row_number, column_number, new_character):

        if 0 <= row_number <= self.rows:
            if 0 <= column_number <= self.columns:
                self.grid[row_number][column_number] == new_character
                return
        raise IndexError(" Index error. Indexes out of bounds / range   ")