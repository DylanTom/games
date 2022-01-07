"""
A module displaying the game board for tic tac toe

Author: Dylan Tom
Date:
"""

import pygame as g
from pygame import draw
import engine

# Game Attributes
WIDTH = HEIGHT = 512
DIMENSION = 3
SQUARE_SIZE = 50
MAX_FPS = 60
IMAGES = {}

g.init()
g.display.set_caption('TicTacToe')
screen = g.display.set_mode((WIDTH,HEIGHT))

PLAYER_ONE = False
PLAYER_TWO = False

def load_images():
	images = ["O.png", "X.png"]
	for image in images:
		IMAGES[image] = g.transform.scale(g.image.load(image))

def main():
	pass
	# draw_game_state(screen, gameState, validMoves, selected)

def draw_board():
	for row in range(DIMENSION):
		for col in range(DIMENSION):
			g.draw.rect(screen, g.Color("white"), \
				g.Rect(row * SQUARE_SIZE, col * SQUARE_SIZE))

def draw_game_state(screen, gameState, validMoves, selected):
	draw_board(screen)

if __name__ == 'main':
	main()