import pygame
import random
import math

class Snowfall:

    def __init__(self):
        pygame.init()
        self.snowflakes = []

        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))

    def start(self):
        while self.running:
            self.screen.fill((0, 0, 0))  
            self.background = pygame.image.load("back.jpg")
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.snowflakes.append(
                Snowflake(random.randrange(-40, 1320), random.randrange(-50, -10), 4, (150, 150, 150), 2.3,self.screen, self.snowflakes))

            self.snowflakes.append(
                Snowflake(random.randrange(-40, 1320), random.randrange(-50, -10), 3, (255, 255, 255), 2, self.screen,self.snowflakes))

            for snowflake in self.snowflakes:
                snowflake.calculate()
                snowflake.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

class Snowflake:
    def __init__(self, x, y, size, color, speed, screen, snowflakes):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color
        self.screen = screen  #
        self.snowflakes = snowflakes
        self.toggle = False
        self.switch = random.randrange(0, 250)

    def draw(self):
        if self.y > 720:
            self.snowflakes.remove(self)  
        else:
            pygame.draw.circle(self.screen, self.color, (round(self.x), round(self.y)), self.size)

    def calculate(self):
        if self.y == self.switch:
            self.toggle = not self.toggle
            self.switch = self.y + random.randrange(0, 250)

        if self.toggle:
            self.x = self.x + (math.cos(self.y / 180) * 0.2)
        else:
            self.x = self.x - (math.sin(self.y / 180) * 0.2)

        self.y = self.y + self.speed

snowfall = Snowfall()
snowfall.start()
