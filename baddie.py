import pygame
import random
import time

class BadBase(pygame.sprite.Sprite):

    def __init__(self,width,height,x,y,color, speed, hp,attk):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.attack = attk
        self.speed  = speed
        self.hp = hp
        self.atk = 1
        self.color  = color
        self.alive  = True
        self.move = True
        self.hit = False
        return

    def tick(self,back_wall,upper_wall,lower_wall):
        if self.move:
            self.new_x = self.x - self.speed
            self.new_y = self.y + random.randint(-1,1)
        if self.new_x < back_wall+45:
            self.setMove(False)
        else:
            self.x = self.new_x
        if self.new_y < upper_wall:
            self.new_y = upper_wall
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
        self.y = self.new_y
        if self.hp <= 0:
            self.setAlive(False)
        return self.alive

    def setMove(self,ismoving):
        self.move = ismoving

    def setSpeed(self,speed):
        self.speed = speed


    def getAlive(self):
        return self.alive

    def GetHP(self):
        return self.hp

    def SetHP(self, hp):
        self.hp = hp

    def Atk(self):
        return self.attack

    def getHurt(self, enatk):
        if random.randint(1, 15) == 1:
            self.SetHP(self.GetHP()-enatk)

    def definateHurt(self, enatk):
        self.SetHP(self.GetHP()-enatk)


    def posX(self):
        return self.x

    def posY(self):
        return self.y

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def checkHitE(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def isHit(self):
        return self.hit

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

class GoodBase(pygame.sprite.Sprite):

    def __init__(self,width,height,x,y,color,speed,hp,attk):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.attack = attk
        self.hp = hp
        self.speed  = speed
        self.atk = 1
        self.color  = color
        self.alive  = True
        self.move = True
        self.hit = False
        return

    def tick(self,back_wall,upper_wall,lower_wall):

        if self.move:
            self.new_x = self.x - self.speed
            self.new_y = self.y + random.uniform(-1,1)
        #if self.new_x > back_wall:
         #   self.setAlive(False)

        if self.new_x >= back_wall-self.width-45:
            self.setMove(False)
        else:
            self.x = self.new_x
        if self.new_y < upper_wall:
            self.new_y = upper_wall
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
        self.y = self.new_y

        if self.hp <= 0:
            self.setAlive(False)

        return self.alive



    def setMove(self,ismoving):
        self.move = ismoving

    def GetHP(self):
        return self.hp

    def Atk(self):
        return self.attack

    def getHurt(self, enatk):
        if random.randint(1, 15) == 1:
            self.SetHP(self.GetHP()-enatk)

    def definateHurt(self, enatk):
        self.SetHP(self.GetHP()-enatk)


    def setSpeed(self,speed):
        self.speed = speed


    def SetHP(self, hp):
        self.hp = hp

    def posX(self):
        return self.x

    def posY(self):
        return self.y

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def isHit(self):
        return self.hit

    def checkHitE(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def setAlive(self,alive):
        self.alive = alive

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return




class GoodOrc(GoodBase):
    def __init__(self,width,height,x,y,color,speed,hp,attk):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.attack = attk
        self.hp = hp
        self.speed  = speed
        self.atk = 1
        self.color  = color
        self.alive  = True
        self.move = True
        self.hit = False
        return
        
