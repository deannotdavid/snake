import pygame

from constants.dimensions import SQUARE_LEN, BOARD_WIDTH, BOARD_HEIGHT
from constants.colors import GREEN

class Snake:
	def __init__(self):
		self.direction = "right"
		self.positions = [(i, 5) for i in range(1,5)]
		self.get_rects()

	def move(self, apple_pos: tuple[int, int]=None) -> bool:
		if self.direction == "right":
			movement = [1, 0]
		if self.direction == "left":
			movement = [-1, 0]
		if self.direction == "up":
			movement = [0, -1]
		if self.direction == "down":
			movement = [0, 1]

		movement_x = movement[0]
		movement_y = movement[1]

		self.head = self.positions[-1]
		self.positions.append((self.head[0]+movement_x, self.head[-1]+movement_y))
		apple_collision = self.apple_collision(apple_pos)
		if not apple_collision:
			del self.positions[0]
		self.get_rects()
		return apple_collision

	def check_collisions(self):
		return self.snake_collision() or self.edge_collision()

	def snake_collision(self) -> bool:
		return self.positions.count(self.head) > 1

	def apple_collision(self, apple_pos: tuple[int, int]) -> bool:
		return self.head == apple_pos

	def edge_collision(self) -> bool:
		lr_collision = self.head[0] < 0 or self.head[0] > BOARD_WIDTH-1
		ud_collision = self.head[1] < 0 or self.head[1] > BOARD_HEIGHT-1
		edge_collision = lr_collision or ud_collision
		return edge_collision

	def get_rects(self):
		self.rects = [pygame.Rect(pos[0]*SQUARE_LEN, pos[1]*SQUARE_LEN,
			SQUARE_LEN, SQUARE_LEN) for pos in self.positions]

	def draw(self, screen: pygame.Surface):
		for square in self.rects:
			pygame.draw.rect(screen, GREEN, square)

	def change_direction(self, direction: str) -> str:
		if self.direction == direction: return

		directions = self.direction, direction
		opposite = ("right" in directions and "left" in directions) or ("up" in directions and "down" in directions)

		if opposite: return

		self.direction = direction

class LoopSnake(Snake):
	def check_collisions(self):
		if self.snake_collision():
			return True # collision has happened

		new_pos = None
		if self.head[0] < 0:
			new_pos = BOARD_WIDTH - 1, self.head[1]
		elif self.head[0] > BOARD_WIDTH-1:
			new_pos = 0, self.head[1]
		elif self.head[1] < 0:
			new_pos = self.head[0], BOARD_HEIGHT-1
		elif self.head[1] > BOARD_HEIGHT - 1:
			new_pos = self.head[0], 0

		if new_pos:
			self.positions.append(new_pos)
			del self.positions[0]