import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
ship_img = pygame.image.load('ship.png')
enemy_1_img = pygame.image.load('enemy1_1.png')
laser = pygame.image.load('laser.png')
lasers = []

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

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = laser
		self.rect = self.image.get_rect(center=pos)
		self.rect.bottom = y
		self.rect.centerx = x
		self.speed = -10
		
	def update(self, dt):
		self.rect.y += self.speedy
		#kill if it moves off the top of the screen
		if self.rect.bottom < 0:
			self.kill()

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
	dt = clock.tick(60) / 1000
	while not exited:
		
		#Set the background
		BackGround = Background('background.png', [0,0])
		gameDisplay.fill([255,255,255])
		gameDisplay.blit(BackGround.image, BackGround.rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exited = True
			
			#Setting up movements
			keys = pygame.key.get_pressed()
			
			#Creating a movement booster
			move = 10 if keys[pygame.K_LSHIFT] else 5 
			
			if keys[pygame.K_LEFT]: #to move left
				x_change = -move
			if x < 0 : x = 0
			
			if keys[pygame.K_RIGHT]: #to move right
				x_change += move
			if x > display_width - 20  : x = 741
			
			if keys[pygame.K_UP]: #to move up
				y_change -= move
			if y < 0: y = 0
			
			if keys[pygame.K_DOWN]: #to move down
				y_change += move
			if y > display_height - 15 : y=533
			
			if event.type == pygame.KEYUP: #stop if no key is pressed
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					x_change = 0
					y_change = 0
					
			if keys[pygame.K_SPACE]: #if space is pressed
				
					
		x += x_change
		y += y_change
	
		
		ship(x,y)
		print(event)
		
		
		
		pygame.display.update()
		clock.tick(60)
	
game_loop()
	

