import math
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, location, mousePos, window):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)    
        
        self.window = window
        self.sprite = "Sprites\\Bullet.png"

        # Load the image
        self.image = pygame.image.load(self.sprite).convert()
        
        #set up rectangle locations
        self.location = location
        self.movement = self.CalculateMovement(mousePos)

        self.rect = self.image.get_rect()
        self.rect.center = self.location

    def Move(self):
        if self.location[0] < 0:
            self.kill()
        elif self.location[0] > 1280:
            self.kill()
        
        if self.location[1] < 0:
            self.kill()
        elif self.location[1] > 720:
            self.kill()
        
        self.location += self.movement
        self.rect.center = self.location
    
    def CalculateMovement(self, mousePos):
        xDiff = self.location[0] - mousePos[0]
        yDiff = self.location[1] - mousePos[1]

        origionalXDiff = xDiff
        origionalYDiff = yDiff

        if xDiff < 0:
            xDiff = -xDiff
        if yDiff < 0:
            yDiff = -yDiff


        hyp = math.sqrt((xDiff*xDiff)+(yDiff*yDiff))

        angle = math.asin(xDiff/hyp)
        x = math.sin(angle)
        y = math.cos(angle)

        
        if origionalXDiff > 0 and origionalYDiff < 0: #Bottom Left Quadrant
            if x > 0:
                x = -x
            if y < 0:
                y = -y
        elif origionalXDiff > 0 and origionalYDiff > 0: #Top Left Quadrant
            if x > 0:
                x = -x
            if y > 0:
                y = -y
        elif origionalXDiff < 0 and origionalYDiff > 0: #Upper Right Quadrant
            if x < 0:
                x = -x
            if y > 0:
                y = -y
        elif origionalXDiff < 0 and origionalYDiff < 0: #Bottom Right Quadrant
            if x < 0:
                x = -x
            if y < 0:
                y = -y 

        return pygame.math.Vector2(x*8, y*8)
