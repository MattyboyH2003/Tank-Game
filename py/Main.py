import pygame
from Player import Player, PlayerTurret

########################################################################################################
#                                              - Setup -                                               #
########################################################################################################

if __name__ == "__main__":
    pygame.init()
    resolution = (1280, 720)
    pygame.display.set_caption("Tank Game")
    window = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
else:
    exit()

########################################################################################################
#                                              - Classes -                                             #
########################################################################################################

class Main: #Main class for storing almost all functions
    def __init__(self):
        self.allSpritesList = pygame.sprite.Group()
        self.bulletSpritesList = pygame.sprite.Group()

        self.player = Player(pygame.math.Vector2(1280/2, 720/2), window)
        self.playerTurret = PlayerTurret(pygame.math.Vector2(1280/2, 720/2), window)
        self.allSpritesList.add(self.player)
        self.allSpritesList.add(self.playerTurret)
        
    def GameLoop(self): #The Main game loop, called when play is clicked
        running = True
        while running:
            self.EventCheck()
            self.playerTurret.UpdateRotation(pygame.mouse.get_pos())

            for bullet in self.bulletSpritesList:
                bullet.Move()

            #Final stuff
            pygame.display.update()
            window.fill((60, 80, 38))
            self.allSpritesList.draw(window)
            clock.tick(30)

    def EventCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.Shoot(self)

        #Checks if the specified keys are pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.MoveUp(self)
        if keys[pygame.K_a]:
            self.player.RotateLeft()
        if keys[pygame.K_s]:
            self.player.MoveDown(self)
        if keys[pygame.K_d]:
            self.player.RotateRight()

########################################################################################################
#                                          - Call Functions -                                          #
########################################################################################################

main = Main()
main.GameLoop()
pygame.quit()
quit()
