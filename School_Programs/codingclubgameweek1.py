import pygame


pygame.init()
win_width = 400
win_height = 400
bg = (10, 100, 200)
win = pygame.display.set_mode((win_width, win_height))
win.fill(bg)
run = True
clock = pygame.time.Clock()
FPS= 35


class Player:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.colour = (225, 0, 0)




	def draw(self):
		self.move()
		pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 2)



	def move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.y -= self.vel
		
		elif keys[pygame.K_DOWN]:
			self.y += self.vel

		elif keys[pygame.K_LEFT]:
			self.x -= self.vel

		elif keys[pygame.K_RIGHT]:
			self.x += self.vel


player = Player(100, 100, 80, 20)

while run:
	clock.tick(FPS)
	win.fill(bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			run = False
			quit()

	player.draw()
	pygame.display.update()