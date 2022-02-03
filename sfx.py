import os

import pygame

pygame.mixer.init()

def update_sfx(*sfx_dir: str) -> dict:
	sfx = {}
	for file in os.listdir(os.path.join("data", *sfx_dir)):
		if file.endswith(".wav"):
			sfx_name = file.removesuffix(".wav")
			sfx[sfx_name] = pygame.mixer.Sound(os.path.join("data", *sfx_dir, file))
	return sfx

sfx = update_sfx("sfx")