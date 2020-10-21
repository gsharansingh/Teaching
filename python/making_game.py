import pygame

# Intialize the pygame
pygame.init()

# window size
w_width = 800
w_height = 600

# create the screen
screen = pygame.display.set_mode((w_width, w_height))

# Redrawing the window
def re_draw_window():
    screen.fill((255, 0, 0))
    p.move()
    p.draw(screen)
    pygame.display.update()

class Player():
    def __init__(self, x=0, y=0, width=100, height=100, color=(0, 0, 0)):
        '''
        A rectangular moved around using keys

        `x`: default 'x-axis' postion of rectangle
        `y`: default 'y-axis' postion of rectangle
        `width`: width of rectangle
        `height`: height of rectangle
        `color`: color of rectangle
        '''

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.displace = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.displace

        if keys[pygame.K_RIGHT]:
            self.x += self.displace

        if keys[pygame.K_UP]:
            self.y -= self.displace

        if keys[pygame.K_DOWN]:
            self.y += self.displace
        
        # Updating the rectangle's position
        self.rect = (self.x, self.y, self.width, self.height)


running = True
p = Player(300, 300, 100, 100, (255, 255, 255))

while running:

    for event in pygame.event.get():
        re_draw_window()
        if event.type == pygame.QUIT:
            running = False