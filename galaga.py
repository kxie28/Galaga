import pygame
import sys
from random import shuffle, randrange, choice

pygame.init()
clock = pygame.time.Clock()
ship_img = pygame.image.load('ship.png')
enemy_1_img = pygame.image.load('enemy1_1.png')


#           R    G    B
WHITE 	= (255, 255, 255)
GREEN 	= (78, 255, 87)
YELLOW 	= (241, 255, 0)
BLUE 	= (80, 255, 239)
PURPLE 	= (203, 0, 255)
RED 	= (237, 28, 36)

display_height = 600
display_width = 800
ship_width = 55
ship_height = 65

gameDisplay 		= pygame.display.set_mode((display_width,display_height))
'''FONT = "fonts/space_invaders.ttf"
IMG_NAMES 	= ["ship", "ship", "mystery", "enemy1_1", "enemy1_2", "enemy2_1", "enemy2_2",
				"enemy3_1", "enemy3_2", "explosionblue", "explosiongreen", "explosionpurple", "laser", "enemylaser"]
IMAGES 		= {name: image.load("images/{}.png".format(name)).convert_alpha()
				for name in IMG_NAMES}'''

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = pygame.image.load('background.png')
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

def enemy_1():
	gameDisplay.blit(enemy_1_img, (x,y))
			
def ship(x,y):
	gameDisplay.blit(ship_img, (x,y))

def game_loop():
	exited = False
	x_change = 0
	y_change = 0
	x = (display_width * 0.45)
	y = (display_height * 0.88)
	while not exited:
		
		#Set the background
		BackGround = Background('background.png', [0,0])
		gameDisplay.fill([255,255,255])
		gameDisplay.blit(BackGround.image, BackGround.rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exited = True
			
			#Setting up movements
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				elif event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = +5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					x_change = 0
					y_change = 0	
		if x > display_width - ship_width or x < 0:
			x_change = 0
		if y > display_height - ship_height or y < 0:
			y_change = 0		
		x += x_change
		y += y_change
	
		
		ship(x,y)
		print(event)
		
		
		
		pygame.display.update()
		clock.tick(60)
	
game_loop()
	

