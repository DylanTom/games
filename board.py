"""
A class for the sudoku board.
"""

class Board(object):
	SIZE = 9
	BOX_SIZE = 3

	EASY = [
		[0,0,0,0,0,4,9,0,0],
		[5,4,0,7,0,6,0,0,0],
		[8,0,3,1,0,0,0,7,0],
		[2,6,8,0,1,7,0,5,4],
		[0,0,0,0,5,8,6,0,0],
		[4,1,0,0,3,2,8,9,7],
		[0,0,0,0,0,1,0,4,3],
		[6,0,4,0,0,0,1,0,9],
		[0,3,0,8,0,0,0,0,0]
	]

	HARD = [
		[8,0,0,0,0,0,0,0,0],
		[0,0,3,6,0,0,0,0,0],
		[0,7,0,0,9,0,2,0,0],
		[0,5,0,0,0,7,0,0,0],
		[0,0,0,0,4,5,7,0,0],
		[0,0,0,1,0,0,0,3,0],
		[0,0,1,0,0,0,0,6,8],
		[0,0,8,5,0,0,0,1,0],
		[0,9,0,0,0,0,4,0,0]
	]

	def __init__(self, board):
		self.board = board

	def displayBoard(self):
		print("Input Board is")
		print()
		for row in range(Board.SIZE):
			line = ""
			if row % Board.BOX_SIZE == 0 and row != 0:
				print("----------------------")
			for col in range(Board.SIZE):
				if col % Board.BOX_SIZE == 0 and col != 0:
					line += "| "
				line += str(self.board[row][col]) + " "
			print(line)