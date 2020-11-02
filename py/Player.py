import copy
import math
import pygame
from Bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, location, window):
        #Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)    
        
        self.window = window
        self.sprite = "Sprites\\Player.png"

        #Load the image
        self.origionalImage = pygame.image.load(self.sprite).convert()
        self.image = self.origionalImage
        self.image.set_colorkey((69, 0, 69))

        #set up rectangle locations        
        self.location = location
        self.angle = 0
        self.lastShotTime = 0

        self.rect = self.image.get_rect()
        self.rect.center = self.location
    
    def MoveUp(self, main):
        self.location += self.CalculateMovement()
        self.ConfirmMove()
        main.playerTurret.setLocation(self.location)
    def MoveDown(self, main):
        difference = self.CalculateMovement()
        self.location += pygame.math.Vector2(-difference[0], -difference[1])
        self.ConfirmMove()
        main.playerTurret.setLocation(self.location)
    def RotateLeft(self):
        self.angle -= 5
        self.image, self.rect = self.Rotate(self.origionalImage, self.rect, self.angle) 
        self.ConfirmRotate()
    def RotateRight(self):
        self.angle += 5
        self.image, self.rect = self.Rotate(self.origionalImage, self.rect, self.angle) 
        self.ConfirmRotate()

    def ConfirmMove(self):
        if self.location[0] > 1280:
            self.location[0] = 1280
        
        elif self.location[0] < 0:
            self.location[0] = 0
        
        if self.location[1] > 720:
            self.location[1] = 720
        
        elif self.location[1] < 0:
            self.location[1] = 0
        
        self.rect.center = self.location
    def ConfirmRotate(self):
        if self.angle < 0:
            self.angle += 360
        if self.angle > 359:
            self.angle -= 360

    @staticmethod
    def Rotate(image, rect, angle):
        """Rotate an image arround central point"""
        rotatedImage = pygame.transform.rotate(image, -angle)
        rotatedRect = rotatedImage.get_rect(center=rect.center)
        return rotatedImage, rotatedRect
    
    def Shoot(self, main):
        if pygame.time.get_ticks() - self.lastShotTime > 1000:
            self.lastShotTime = pygame.time.get_ticks()
            bullet = Bullet(copy.deepcopy(self.location), pygame.mouse.get_pos(), self.window)
            main.bulletSpritesList.add(bullet)
            main.allSpritesList.add(bullet)

    def CalculateMovement(self):
        direction = math.radians(self.angle)
        x = math.cos(direction)
        y = math.sin(direction)
        return pygame.math.Vector2(x*5, y*5)

class PlayerTurret(pygame.sprite.Sprite):
    def __init__(self, location, window):
        #Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)    
        
        self.window = window
        self.sprite = "Sprites\\PlayerTurret.png"

        self.location = location
        self.angle = 0

        #Load the image
        self.origionalImage = pygame.image.load(self.sprite).convert()
        self.image = self.origionalImage
        
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.image.set_colorkey((69, 0, 69))

        #set up rectangle locations
        self.rect = self.image.get_rect()
        self.rect.center = self.location
    
    def UpdateRotation(self, mousePos):
        self.angle = self.CalculateAngle(mousePos)
        self.image, self.rect = self.Rotate(self.origionalImage, self.rect, self.angle)

    def CalculateAngle(self, mousePos):
        xDiff = self.location[0] - mousePos[0]
        yDiff = self.location[1] - mousePos[1]

        hyp = math.sqrt((xDiff*xDiff)+(yDiff*yDiff))
        angle = math.acos(xDiff/hyp)

        angle = math.degrees(angle)
        angle -= 180

        if yDiff < 0:
            angle = -angle

        return angle

    @staticmethod
    def Rotate(image, rect, angle):
        """Rotate an image arround central point"""
        rotatedImage = pygame.transform.rotate(image, -angle)
        rotatedImage.set_colorkey((69, 0, 69))
        rotatedRect = rotatedImage.get_rect(center=rect.center)
        return rotatedImage, rotatedRect

    def setLocation(self, location):
        self.location = location
        self.rect.center = location
