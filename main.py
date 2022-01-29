import os
import random

import pygame

from utils import *
from board import Board
from snake import Snake

from constants.colors import *
from constants.dimensions import WIDTH, HEIGHT

class Game:
	def __init__(self) -> None:
		# pygame stuff
		self.FPS = 60
		self.win = pygame.display.set_mode((WIDTH, HEIGHT))
		
		# controls
		self.right = pygame.K_RIGHT, pygame.K_d
		self.left = pygame.K_LEFT, pygame.K_a
		self.up = pygame.K_UP, pygame.K_w
		self.down = pygame.K_DOWN, pygame.K_s

		# fonts
		font_path = os.path.join("data", "fonts", "nokiafc22.ttf")
		self.score_font = pygame.font.Font(font_path, 256)

	def play_game(self):
		print("new")

		score = 0
		snake = Snake()

		board = Board()
		board.generate_board(snake.positions)

		clock = pygame.time.Clock()


		move_event = pygame.USEREVENT + 1

		pygame.time.set_timer(move_event, 60)


		to_move_dir = "right"
		dir_changed = False

		while True:
			clock.tick(self.FPS)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					quit_program()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_SPACE:
						board.generate_board()
					if e.key == pygame.K_ESCAPE:
						quit_program()
					if dir_changed == False:
						dir_changed = True
						if e.key in self.right:
							to_move_dir = "right"
						if e.key in self.left:
							to_move_dir = "left"
						if e.key in self.up:
							to_move_dir = "up"
						if e.key in self.down:
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
						# score_surf = self.score_font.render(str(score), False,
						# 	WHITE)
						# score_rect = score_surf.get_rect(center=self.win.get_rect().center)
						# self.win.blit(score_surf, score_rect)
						# pygame.display.update()
						# pygame.time.delay(700)
						self.game_over(score)
						return

			self.win.fill(BLACK)
			board.draw(self.win)

			snake.draw(self.win)
			pygame.display.update()

	def game_over(self, score: int) -> None:
		score_surf = self.score_font.render(str(score), False, WHITE)
		score_rect = score_surf.get_rect(center=self.win.get_rect().center)

		clock = pygame.time.Clock()

		while True:
			clock.tick(self.FPS)
			self.win.blit(score_surf, score_rect)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					quit_program()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
						quit_program()
					if e.key == pygame.K_SPACE:
						return
			pygame.display.update()


def main():
	pygame.init()
	g = Game()
	while True:
		g.play_game()


if __name__ == '__main__':
	main()