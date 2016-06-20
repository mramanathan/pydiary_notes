#!/usr/bin/env python

#  -*- coding:utf-8 -*-

import sys
import matrix
import character
from character import Direction
from character import MainSymbol

rows, columns = 23, 40
defaultchar = ' '

game_matrix = matrix.Matrix(rows, columns, defaultchar)
main_symbol = MainSymbol('*')

def main():

    # print "Main symbol used is ", main_symbol.symbol
    game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

    while True:

        game_matrix.print_matrix()
        direction = raw_input("Where to go today ? (WASD) ")

        if direction == 'q':
            sys.exit()
        elif direction in (Direction.NORTH, Direction.EAST, Direction.WEST, Direction.SOUTH):
            # game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.trace)
            main_symbol.move(direction)
            game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

    return ''

if __name__ == '__main__':
    main()