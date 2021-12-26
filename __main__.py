"""
The primary application script
"""

from sudoku import *

def sudoku():
	board = []
	for i in range(Sudoku.SIZE):
		row = []
		for j in range(Sudoku.SIZE):
			row.append(int(input(f'What is in ({i+1},{j+1})? ')))
		board.append(row)
	Sudoku(board).run()

if __name__ == '__main__':
	print('What game do you want to play?')
	game = input('Enter \'s\' for sudoku ')
	if game == 's':
		sudoku()