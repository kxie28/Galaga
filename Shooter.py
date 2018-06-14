import pygame
import random


width = 800
height = 600
FPS = 30

pygame.init()
display_screen = pygame.display.set_mode( (width,height) )
pygame.display.set_caption("test game")
clock = pygame.time.Clock() #set to keep FPS at what we need it at

ship_img = pygame.image.load('ship.png')
meteors_img = pygame.image.load('meteors.png')
lasers_img = pygame.image.load('laser.png')
x = (width * 0.45)
y = (height * 0.88)

#           R    G    B
WHITE 	= (255, 255, 255)
GREEN 	= (78, 255, 87)
YELLOW 	= (241, 255, 0)
BLUE 	= (80, 255, 239)
PURPLE 	= (203, 0, 255)
RED 	= (237, 28, 36)
BLACK 	= (0,	0, 	 0)

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = pygame.image.load('background.png')
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.rect.center = (width/2, height/2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #mself.image = pygame.Surface((50, 50))
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0    
            
    def shoot(self):
		laser = Laser(self.rect.centerx, self.rect.top)
		all_sprites.add(laser)
		lasers.add(laser)

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((30,40))
		self.image = meteors_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(width - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1,8) #random enemies come from the top
		self.speedx = random.randrange(-3, 3) #random enemies can also come from the sides
		
	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width +20:
			self.rect.x = random.randrange(width - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)

class Laser(pygame.sprite.Sprite):
	def __init__(self, x ,y):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10,20))
		self.image = lasers_img
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10
	
	def update(self):
		self.rect.y += self.speedy
		#bullet ends when it's off the screen
		if self.rect.bottom < 0:
			self.kill()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
lasers = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
	dots = Enemy()
	all_sprites.add(dots)
	enemies.add(dots)

def crashed():
	message_display("You Crashed")
	

def game_loop():
	game_running = True
	while game_running:
		#FPS
		clock.tick(FPS)
		#inputs
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()
		
		
		
		
		#Update the screen
		all_sprites.update()
		
		#handle bullets hitting enemies
		collides = pygame.sprite.groupcollide(enemies, lasers, True, True)
		for collide in collides:
			dots = Enemy()
			all_sprites.add(dots)
			enemies.add(dots)
		
		#handle collisions
		collide = pygame.sprite.spritecollide(player, enemies, False)
		if collide:
			game_running = False
		
		#Set the background
		BackGround = Background('background.png', [0,0])
		display_screen.fill([255,255,255])
		display_screen.blit(BackGround.image, BackGround.rect)
		all_sprites.draw(display_screen)
		pygame.display.flip()

game_loop()

