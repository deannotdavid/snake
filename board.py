import random

import pygame

from constants.dimensions import *
from constants.colors import *

class Square:
	def __init__(self, row: int, column: int) -> None:
		self.width = SQUARE_LEN

		self.row = row
		self.column = column
		self.color = RED

		self.get_rect()

	def get_rect(self) -> None:
		self.rect = pygame.Rect(self.row*self.width, self.column*self.width, self.width, self.width)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.rect(screen, self.color, self.rect)

class Board:
	def __init__(self) -> None:
		pass

	def generate_board(self, snake: list[tuple[int, int]]) -> None:
		self.answer = Square(random.randint(1, BOARD_WIDTH-2), random.randint(1, BOARD_HEIGHT-2))
		while (self.answer.row, self.answer.column) in snake:
			print("Oops")
			self.answer = Square(random.randint(0, BOARD_WIDTH-1), random.randint(0, BOARD_HEIGHT-1))

		self.answer_pos = self.answer.row, self.answer.column

	def draw(self, screen: pygame.Surface) -> None:

		self.answer.draw(screen)
		return
		for row in self.board:
			for square in row:
				square.draw(screen)
