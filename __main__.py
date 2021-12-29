"""
The primary application script
"""

from sudoku import *
import sys


def sudoku():
	board = []
	for i in range(Sudoku.SIZE):
		row = []
		for j in range(Sudoku.SIZE):
			row.append(int(input(f'What is in ({i+1},{j+1})? ')))
		board.append(row)
	Sudoku(board).run()


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == 'EASY':
			Sudoku(EASY).run()
		elif sys.argv[1] == 'HARD':
			Sudoku(HARD).run()
	else:
		print('What game do you want to play?')
		print('Enter \'s\' for sudoku ')
		print()
		game = input()
		if game == 's':
			print('Beginning sudoku, enter a valid board:')
			sudoku()