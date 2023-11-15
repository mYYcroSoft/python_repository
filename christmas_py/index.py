import pygame
import random
import math


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

x = 100
y = 0



class Snowflake:
    def __init__(self, x,y, size, color, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color
        self.toggle = False 
        self.switch = random.randrange(0,250)

    def draw(self):
        if self.y > 720:
            del self
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def calculate(self):
        if self.y == self.switch:
            self.toggle = not self.toggle
            self.switch = self.y + random.randrange(0,250)
        
        if self.toggle:
            self.x = self.x + (math.cos(self.y/ 180) * 0.2) 
        else:
            self.x = self.x - (math.sin(self.y/ 180) * 0.2)     
        
        self.y = self.y + self.speed

snowfalkes = [

]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    snowfalkes.append(Snowflake(random.randrange(-40,1320), random.randrange(-50,-10), 4, (150, 150, 150), 2.3))

    snowfalkes.append(Snowflake(random.randrange(-40,1320), random.randrange(-50,-10), 3, (255, 255, 255), 2))

    
    #pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)
    for snowflake in snowfalkes:
        snowflake.calculate()
        snowflake.draw()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
