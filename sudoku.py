"""
A class for sudoku.
"""

class Sudoku:
	"""
	
	"""
	# Class Attributes
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
		"""
		Initializes the sudoku board

		Parameter board: the sudoku grid to solve
		Precondition: board is a 2D table of size, Sudoku.SIZE
		"""
		self.board = board

	def run(self):
		"""
		Main script to run the sudoku solver
		"""
		print("Input board is...")
		self._display_board()
		self._solve()
		print("Solved board is...")
		self.display_board()

	def _display_board(self):
		print()
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
		The main function to solve the sudoku board
		"""
		r, c = self._next_empty_square()

		if r == -1:
			return True
		
		for guess in range(1,10):
			if self._is_valid(guess,r,c):
				self.board[r][c] == guess
				# Recursive call to solve the rest of the puzzle
				if self._solve():
					return True
			# Backtrack
			self.board[r][c] = 0
		
		return False	


	def _next_empty_square(self):
		"""
		Returns a pair r, c of a square that is empty

		Helper method to solve()
		"""
		for r in range(Sudoku.SIZE):
			for c in range(Sudoku.SIZE):
				if self.board[r][c] == 0:
					return r, c
		
		return -1, -1

	def _is_valid(self, guess, row, col):
		"""
		Returns True if guess is a legal guess
		"""
		# Verifies the row is valid
		if guess in self.board[row]:
			return False

		# Verifies the column is valid
		col_tracker = [self.board[r][col] for r in range(Sudoku.SIZE)]
		if guess in col_tracker:
			return False
		
		# Verifies each 3 x 3 grid is valid
		row_begin = (row // Sudoku.BOX_SIZE) * Sudoku.BOX_SIZE
		col_begin = (col // Sudoku.BOX_SIZE) * Sudoku.BOX_SIZE

		for i in range(Sudoku.BOX_SIZE):
			for j in range(Sudoku.BOX_SIZE):
				if self.board[i + row_begin][j + col_begin] == guess:
					return False

		return True
	

