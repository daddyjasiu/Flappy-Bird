import pygame, sys

def draw_floor():

	screen.blit(floor_surface, (floor_x_pos, 900))
	screen.blit(floor_surface, (floor_x_pos + width, 900))


pygame.init()

width = 576
height = 1024
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Game Variables

gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('S:/repo/Flappy-Bird/main/assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('S:/repo/Flappy-Bird/main/assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('S:/repo/Flappy-Bird/main/assets/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 512))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_movement = 0
				bird_movement -= 12


	screen.blit(bg_surface, (0, 0))

	bird_movement += gravity
	bird_rect.centery += bird_movement
	screen.blit(bird_surface, bird_rect)

	floor_x_pos -= 1
	draw_floor()

	if floor_x_pos <= -576:
		floor_x_pos = 0

	pygame.display.update()
	clock.tick(120)