import pygame

pygame.joystick.init() #check for joysticks
joysitkcs = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())] #get all joysticks
print(joysitkcs)

class Player(object):
    def __init__(self):
        self.player = pygame.rect.Rect((300,400,50,50))
        self.color = "white"
        
    def move(self, x_speed,y_speed):
        self.player.move_ip((x_speed,y_speed))
    def changecolor(self, color):
        self.color = color
    def draw(self, game_screen):
        pygame.draw.rect(game_screen,self.color,self.player)

pygame.init()

player = Player()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            break
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            #print(pygame.joystick.Joystick(0).get_button)
