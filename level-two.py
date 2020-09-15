import pygame



SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED= (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHTPURPLE= (153, 0, 153)

image=pygame.image.load(r'C:\Users\Dell\Desktop\se\spaceshipnew.png')
alien=pygame.image.load(r'C:\Users\Dell\Desktop\se\devilone.jpg')
blue=pygame.image.load(r'C:\Users\Dell\Desktop\se\blueflame.jpg')

#font = pygame.font.SysFont("comicsansms", 72)
 
#text = font.render("Hello, World", True, (0, 128, 0))



class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False
    background_image=pygame.image.load(r"C:\Users\Dell\Desktop\se\wa.jpg")
    image=pygame.image.load(r'C:\Users\Dell\Desktop\se\spaceship_resize.png')
    


    def __init__(self, width, height):

        game_over=False
        
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2 -38, height - 100)
        generator = Generator(self)
        rocket = None
    
        while not done:
            if len(self.aliens) == 0:
                self.screen.fill(WHITE)
                self.displayText("VICTORY  ACHIEVED :)")
                #self.displayMessage1("PLAY AGAIN:Y ")
                self.displayMessage2("QUIt :C ")
                
                game_over=True
                for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_c:
                          pygame.quit()
                     

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                hero.x -= 2 if hero.x > 20 else 0  
            elif pressed[pygame.K_RIGHT]:  
                hero.x += 2 if hero.x < width - 20 else 0  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x+50, hero.y))

            background_image=pygame.image.load(r'C:\Users\Dell\Desktop\se\wa.jpg')
            pygame.display.flip()
            self.clock.tick(60)
            #self.screen.fill((0, 0, 0)
            self.screen.blit(background_image,[0,0])

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if ((alien.y > height-30)or((alien.y+30>=hero.y+2)and(alien.x>=hero.x and alien.x<=hero.x+100))):
                    self.screen.fill(WHITE)
                    self.lost = True
                    self.displayText("YOU DIED:(")
                    #self.displayMessage1("PLAY AGAIN:Y ")
                    self.displayMessage2("QUIt :C ")
                    game_over=True
                    
                    for event in pygame.event.get():
                      if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                          return Game(self.width,self.height)
                        if event.key == pygame.K_c:
                          pygame.quit()
                      

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: hero.draw()

                

    
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('comicsansms', 50)
        textsurface = font.render(text, False, GREEN)
        self.screen.blit(textsurface, (50, 50))
    def displayMessage1(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('comicsansms', 50)
        textsurface = font.render(text, False, RED)
        self.screen.blit(textsurface, (400, 150))
        
    def displayMessage2(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('comicsansms', 50)
        textsurface = font.render(text, False, RED)
        self.screen.blit(textsurface, (400, 200))


class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    def draw(self):
        #pygame.draw.rect(self.game.screen,  
                         #LIGHTBLUE,  
                         #pygame.Rect(self.x, self.y, self.size, self.size))
        self.game.screen.blit(alien,(self.x,self.y))
        self.y += 0.24

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)


class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.image=image

    #image=pygame.image.load(r'C:\Users\Dell\Desktop\se\spaceship.png')


    def draw(self):
        self.game.screen.blit(image,(self.x,self.y))
        #pygame.draw.rect(self.game.screen,
         #                (210, 250, 251),
          #               pygame.Rect(self.x, self.y, 8, 5))


class Generator:
    def __init__(self, game):
        margin = 30 
        width = 50  
        for x in range(margin+20, game.width - margin, width-10):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

        # game.aliens.append(Alien(game, 280, 50))


class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        pygame.mixer.music.load('gunshoot.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def draw(self):
        #pygame.draw.rect(self.game.screen,  
         #                RED,  
          #               pygame.Rect(self.x, self.y, 3, 5))
        self.game.screen.blit(blue,(self.x,self.y))
        self.y -= 1  


if __name__ == '__main__':
    game = Game(800,600)

