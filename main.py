import random

import pygame

from board import Board
from snake import Snake

from constants.dimensions import WIDTH, HEIGHT
from constants.colors import *

pygame.init()

# consts

FPS = 240
win = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
	clock = pygame.time.Clock()

	score = 0
	snake = Snake()

	board = Board()
	board.generate_board(snake.positions)


	move_event = pygame.USEREVENT + 1

	pygame.time.set_timer(move_event, 60)

	right = pygame.K_RIGHT, pygame.K_d
	left = pygame.K_LEFT, pygame.K_a
	up = pygame.K_UP, pygame.K_w
	down = pygame.K_DOWN, pygame.K_s

	to_move_dir = "right"
	dir_changed = False

	while True:
		clock.tick(FPS)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				quit()
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_SPACE:
					board.generate_board()
				if e.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if dir_changed == False:
					dir_changed = True
					if e.key in right:
						to_move_dir = "right"
					if e.key in left:
						to_move_dir = "left"
					if e.key in up:
						to_move_dir = "up"
					if e.key in down:
						to_move_dir = "down"

			if e.type == move_event:
				snake.change_direction(to_move_dir)
				dir_changed = False
				snake.move(board.answer_pos)
				if snake.head == board.answer_pos:
					board.generate_board(snake.positions)
					score += 1
				if snake.check_collisions():
					print(score)
					return

		win.fill(BLACK)
		board.draw(win)

		snake.draw(win)
		pygame.display.update()


if __name__ == '__main__':
	main()