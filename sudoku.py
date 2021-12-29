"""
A module providing a class for solving sudoku.

Author: Dylan Tom
Date: December 29, 2021
"""

import time

# Test boards
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

class Sudoku:
	"""
	A class for sudoku.

	Attribute SIZE: the size of the sudoku board
	Invariant: SIZE is an int

	Attribute BOX_SIZE: size of a box, a subset of the sudoku board
	Invariant: BOX_SIZE is an int less than SIZE
	"""

	SIZE = 9
	BOX_SIZE = 3

	def __init__(self, board):
		"""
		Initializes the sudoku board.

		Parameter board: the sudoku grid to solve, must be valid
		Precondition: board is a 2D table of size, Sudoku.SIZE
		"""
		self.board = board


	def run(self):
		"""
		Runs the sudoku solver.
		"""
		print("Input board is...")
		self._display_board()
		start = time.perf_counter()
		self._solve()
		print(f'Solved in {time.perf_counter() - start} seconds')
		print("Solved board is...")
		self._display_board()


	def _display_board(self):
		"""
		Displays the board in an easy to read format.
		"""
		for row in range(Sudoku.SIZE):
			line = ""
			if row % Sudoku.BOX_SIZE == 0 and row != 0:
				print("----------------------")
			for col in range(Sudoku.SIZE):
				if col % Sudoku.BOX_SIZE == 0 and col != 0:
					line += "| "
				line += str(self.board[row][col]) + " "
			print(line)
		print()


	def _solve(self):
		"""
		Returns True if the board is solved or False if the board is not.

		The main function to solve the sudoku board. 
		- Finds the next empty square.
		- Makes a guess from 1 to 9, inclusive. 
		- Verifies that the guess is valid.  
		- Fills the appropriate square with that number.
		- Recursive call to solve the rest of the puzzle.
		- Backtracks if the recursive call fails.
		"""
		r, c = self._next_empty_square()

		if r is None:
			return True
		
		for guess in range(1,10):
			if self._is_valid(guess,r,c):
				self.board[r][c] = guess
				if self._solve():
					return True
			self.board[r][c] = 0
		
		return False	


	def _next_empty_square(self):
		"""
		Returns a pair r, c of a square that is empty or None if there are
		no more empty squares.

		Helper method to solve().
		"""
		for r in range(Sudoku.SIZE):
			for c in range(Sudoku.SIZE):
				if self.board[r][c] == 0:
					return r, c
		
		return None, None

	def _is_valid(self, guess, row, col):
		"""
		Returns True if guess is a legal guess

		Helper method to solve(). Verifies that the guess does not appear in 
		the row, column, or its own 3 x 3 grid. 

		Parameter guess: A random guess to fill the square at row, col
		Precondition: guess is an int between 1 and 9, inclusively

		Parameter row: The row of the empty square
		Precondition: row is an int between 1 and 9, inclusively

		Parameter col: The column of the empty square
		Precondition: col is an int between 1 and 9, inclusively
		"""
		# Verifies that the row is valid
		if guess in self.board[row]:
			return False

		# Verifies that the column is valid
		col_tracker = [self.board[r][col] for r in range(Sudoku.SIZE)]
		if guess in col_tracker:
			return False
		
		# Verifies that the 3 x 3 grid is valid
		row_begin = (row // Sudoku.BOX_SIZE) * Sudoku.BOX_SIZE
		col_begin = (col // Sudoku.BOX_SIZE) * Sudoku.BOX_SIZE

		for i in range(Sudoku.BOX_SIZE):
			for j in range(Sudoku.BOX_SIZE):
				if self.board[i + row_begin][j + col_begin] == guess:
					return False

		return True
	

