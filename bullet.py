import pygame

class Bullet():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.y_vel = 0
        self.x      = x
        self.y = y
        self.y      = self.y+self.y_vel

        self.speed  = 10
        self.color  = color
        self.alive  = True
        self.hit    = False
        return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def moveBullet(self):
        self.x += self.speed
        self.y_vel += 1
        self.y += self.y_vel

        return

    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
        
