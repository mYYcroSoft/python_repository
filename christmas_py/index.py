import pygame
from pygame import mixer 
import random
import math

class music:
    def __init__(self) -> None:
        mixer.init()    
        mixer.music.load("music.mp3")    
        mixer.music.set_volume(0.7) 
        mixer.music.play() 

  

class Snowfall:

    def __init__(self):
        pygame.init()
        self.snowflakes = []

        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.song = music()
        self.random_char = chr(random.randint(65, 90))
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.gift_image = pygame.image.load("gift.png")
        self.gift_rect = self.gift_image.get_rect()
        self.gift_rect.topleft = (random.randrange(0, 300), random.randrange(0, 300))

        
     
 
    def game(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("A")
                    if self.gift_rect.collidepoint(event.pos):
                        self.gift_rect.topleft = (random.randrange(0, 800), random.randrange(0, 800))
                        self.score += 1
          
        
    def start(self):    
        while self.running:
            self.game()
            self.screen.fill((0, 0, 0))  
            self.background = pygame.image.load("back2.jpg")
            self.background = pygame.transform.scale(self.background, (1280, 720))

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

            self.screen.blit(self.gift_image, self.gift_rect.topleft)
            pygame.transform.scale(self.gift_image, (50, 50))
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

if __name__ == "__main__":
    snowfall = Snowfall()
    snowfall.start()
