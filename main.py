import os
import random

import pygame

import leaderboard as lb
from utils import *
from board import Board
from snake import Snake, LoopSnake

from constants.colors import *
from constants.dimensions import WIDTH, HEIGHT

class Game:
	def __init__(self) -> None:
		# pygame stuff
		self.FPS = 60
		self.win = pygame.display.set_mode((WIDTH, HEIGHT))

		pygame.mouse.set_visible(False)
		
		# controls
		self.right = pygame.K_RIGHT, pygame.K_d
		self.left = pygame.K_LEFT, pygame.K_a
		self.up = pygame.K_UP, pygame.K_w
		self.down = pygame.K_DOWN, pygame.K_s

		# fonts
		nokia_path = os.path.join("data", "fonts", "nokiafc22.ttf")
		arcade_path = os.path.join("data", "fonts", "PressStart2P.ttf")
		self.score_font = pygame.font.Font(nokia_path, 256)
		self.header_font = pygame.font.Font(arcade_path, 56)
		self.body_font = pygame.font.Font(arcade_path, 32)

	def leaderboard(self):
		# gets top 10 scores from the leaderboard database
		top_scores = lb.get_top(10)
		# adds blank spots if top 10 is not full
		while len(top_scores) < 10:
			top_scores.append(('___', 0, random.choice(["LOOP", "WALLS"])))
		print(top_scores)

		# gets the center co-ordinates of self.win
		center_x, center_y = self.win.get_rect().center

		clock = pygame.time.Clock()
		
		# creates surfaces for leaderboard to be drawn inside the leaderboard
		header = "HIGH SCORES"
		header_surf = self.header_font.render(header, False, WHITE)

		leaderboard_lines = list()
		for place, score in enumerate(top_scores):
			place_str = str(place + 1)
			name, points, mode = score
			line = f"{place_str.rjust(2)} {name.center(9)} {str(points).rjust(3, '0')} {mode.rjust(8)}"
			line_surf = self.body_font.render(line, False, WHITE)
			line_center = center_x - (line_surf.get_width()/2)
			y = 97 + (place * 50)
			leaderboard_lines.append((line_surf, line_center, y))

		while True:
			clock.tick(self.FPS)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.win.fill(BLACK)

			# blit header
			self.win.blit(header_surf, (center_x - header_surf.get_width()/2, 20))

			# blit leaderboard
			for surf, x, y in leaderboard_lines:
				self.win.blit(surf, (x, y))

			pygame.display.update()

	def play_game(self):
		score = 0
		snake = LoopSnake()

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
						return score

			self.win.fill(BLACK)
			board.draw(self.win)

			snake.draw(self.win)
			pygame.display.update()

	def game_over(self, score: int) -> None:
		score_surf = self.score_font.render(str(score), False, WHITE)
		score_rect = score_surf.get_rect(center=self.win.get_rect().center)

		clock = pygame.time.Clock()
		self.win.blit(score_surf, score_rect)
		pygame.display.update()


		while True:
			clock.tick(self.FPS)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					quit_program()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_SPACE:
						print("hi")
						return


def main():
	pygame.init()
	g = Game()
	g.leaderboard()
	# while True:
	# 	score = g.play_game()
	# 	g.game_over(score)

if __name__ == '__main__':
	main()