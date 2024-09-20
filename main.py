import pygame, sys
import movements
#import tic_tac_toe

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        # Variable that stores whether we are in a battle or not
        self.battle = None

    def run(self):
        # Add code that stops the player from walking when battling
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                

            self.screen.fill('black')
            x_sprite = pygame.image.load('Graphics/X Sprite.png').convert_alpha()
            #x_sprite = pygame.transform.rotozoom(x_sprite,0,4)
            x_rect = x_sprite.get_rect(center = (500, 500))
            
            self.screen.blit(x_sprite, x_rect)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
    