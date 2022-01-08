"""
A module displaying the game board for tic tac toe

Author: Dylan Tom
Date:
"""

import pygame as g
from pygame.draw import circle
import engine

# Game Attributes
WIDTH = HEIGHT = 600
DIMENSION = 3
SQUARE_SIZE = WIDTH // DIMENSION
MAX_FPS = 60
IMAGES = {}

g.display.set_caption('TicTacToe')

PLAYER_ONE = False	
PLAYER_TWO = False

def main():
	"""
	Main script handling updating and displaying game state
	"""
	g.init()
	screen = g.display.set_mode((WIDTH,HEIGHT))
	clock = g.time.Clock()
	screen.fill((255,255,255))
	gs = engine.TicTacToeEngine()

	running = True
	while running:
		for e in g.event.get():
			if e.type == g.QUIT:
				running = False
		
		draw_game_state(screen, gs)
		clock.tick(MAX_FPS)
		g.display.flip()

def draw_game_state(screen, gs):
	draw_board(screen)
	draw_shapes(screen, gs.board)

def draw_board(screen):
	"""
	Draws a standard tic tac toe board 

	WARNING: Pygame uses column major order. Note the order of "i" and "j" 
	in the code. 

	Parameter screen: the screen to draw on
	Precondition: screen is a valid pygame attribute 
	"""
	for i in range(DIMENSION):
		for j in range(DIMENSION):
			g.draw.rect(screen, g.Color("white"), \
				g.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	# Drawing border lines
	g.draw.line(screen, g.Color("black"), (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), width = 2)
	g.draw.line(screen, g.Color("black"), (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), width = 2)
	g.draw.line(screen, g.Color("black"),(0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), width = 2)
	g.draw.line(screen, g.Color("black"), (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), width = 2)

def draw_shapes(screen, board):
	for i in range(DIMENSION):
		for j in range(DIMENSION):
			if board[j][i] == 'O':
				# need to fix
				g.draw.circle(screen, g.Color("black"), (((j+1) * SQUARE_SIZE)//2, ((i) * SQUARE_SIZE)//2), 0.5 * SQUARE_SIZE, 10)
			elif board[j][i] == 'X':
				pass


if __name__ == '__main__':
	main()