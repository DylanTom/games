"""
A module providing the class for the logic of the tic tac toe game

Author: Dylan Tom
Date:
"""

class TicTacToeEngine():
	"""
	A class for the tic tac toe engine
	"""
	SIZE = 3

	def __init__(self):
		self.board = []

	def _create_board(self):
		for row in range(TicTacToeEngine.SIZE):
			row = []
			for col in range(TicTacToeEngine.SIZE):
				row.append('-')
			self.board.append(row)

	def _is_board_filled(self):
		for row in range(TicTacToeEngine.SIZE):
			for col in range(TicTacToeEngine.SIZE):
				if self.board[row][col] == '-':
					return False
		
		return True

	# Check whether the board is filled
	# Check whether player has won or not
	# Select the first turn of the player
	# While loop, breaks when game is over
		# Ask the user to select a row and column
		# Update the spot 
		# If current player won game, print a winning message
		# Check whether board is filled