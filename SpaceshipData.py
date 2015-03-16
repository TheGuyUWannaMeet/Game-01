import pygame
import random

import time
from spaceship import Spaceship
from baddie import *
pygame.font.init()

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.goodiegroup = pygame.sprite.Group()
        self.baddiegroup = pygame.sprite.Group()
        self.allgrouop = self.goodiegroup, self.baddiegroup
        GoodBase.groups = self.goodiegroup
        BadBase.groups = self.baddiegroup

        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("Courier New",15)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/3

        self.PlayerBaseHP= 1000
        self.OpponentBaseHP= 1000
        self.PlayerXP = 0
        self.OpponentXP=0
        self.PlayerAge = 1
        self.OpponentAge = 1
        self.gold = 300

        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,255,255))
        self.spaceship_speed = 5
        self.bullets = []
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (255,255,255)

        self.baddies = []
        self.goodies = []
        self.Gspeed = -3
        self.Bspeed = 3

        self.baseE_width = 40
        self.baseE_height = 40
        self.baseEcolor = (255,0,0)
        self.baseE_hp = 50
        self.baseE_speed = 3

        self.hmsecond = 0
        self.msecond=0
        self.second =0
        self.minuet = 0

        self.timer = 0
        self.timer2 = 0

        self.turret = False
        self.turretn = []
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_LEFT in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_RIGHT in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_DOWN in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)


        if pygame.K_g in newkeys:
            self.addGoodBase()

        if pygame.K_h in newkeys:
            self.addBadBase()

        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))


        self.mouse_pos = mouse_position
        self.buttons = buttons
        self.newbuttons = newbuttons
        #if random.randint(1,self.frame_rate/8) ==1:

        if self.hmsecond==5: #or  self.msecond == 35:
            self.addBadBase()
            print "go"
            #self.addGoodBase()

        if self.hmsecond < 30:
            self.hmsecond +=.5
        if self.hmsecond >= 30:
            self.hmsecond = 0

        if self.msecond < 30:
            self.msecond+=1

        if self.msecond >= 30:
            self.msecond = 0
            self.second += 1

        if self.second >= 60:
            self.second = 0
            self.minuet += 1

        if self.timer <= 0:
            self.timer = 1
        self.timer -=1

        if self.timer2 <= 0:
            self.timer2 = 1
        self.timer2 -=1


        if self.turret == True:
            #for n in self.turretn:

            if self.msecond ==5 or self.msecond == 10 or self.msecond == 15 or self.msecond == 20:
                self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))



        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)
            x,y,w,h = baddie.getDimensions()
            if x <= 50:
                if self.msecond == 1:
                    self.PlayerBaseHP-= baddie.Atk()

        for goodie in self.goodies:
            goodie.tick(self.width,0,self.height)

            x,y,w,h = goodie.getDimensions()
            if x >= 500:
                if self.msecond == 1:
                    self.OpponentBaseHP -= goodie.Atk()
            if pygame.K_w in newkeys:
                goodie.setMove(False)
            if pygame.K_s in newkeys:
                goodie.setMove(True)


        for goodie in self.goodies:
            if not goodie.alive:
                self.OpponentXP +=100
                continue


            for baddie in self.baddies:
                if not baddie.alive:
                    self.Gspeed = -3
                    self.gold += 25
                    self.PlayerXP += 100
                    continue


                x,y,w,h = baddie.getDimensions()
                goodie.checkHitE(x,y,w,h)
                if goodie.isHit()== True:
                    goodie.getHurt(baddie.Atk())
                    baddie.getHurt(goodie.Atk())
                    baddie.setSpeed(0)
                    goodie.setSpeed(0)

                else:
                    baddie.setSpeed(3)
                    goodie.setSpeed(-3)

            for baddie in self.baddies:
                if not baddie.alive:
                    self.Gspeed = -3
                    continue

            for goodie in self.goodies:
                if not goodie.alive:
                    self.Bspeed = 3
                    continue
                if goodie.isHit()== False:
                    self.Bspeed = 3









        if self.OpponentBaseHP <= 0 or self.PlayerBaseHP <= 0:
            pygame.quit()



        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    self.gold += 25
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHitBaddie(x,y,w,h)
                if bullet.getHit():

                    bullet.setAlive(False)
                    baddie.definateHurt(10)



        live_bullets = []
        live_baddies = []
        live_goodies = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
        for goodie in self.goodies:
            if goodie.alive:
                live_goodies.append(goodie)
      
        self.bullets = live_bullets
        self.baddies = live_baddies
        self.goodies = live_goodies
            
        return

    def addBadBase(self):
        new_baddie = BadBase( self.baseE_width, self.baseE_height, self.width, (self.height-self.baseE_height), self.baseEcolor, self.Bspeed, self.baseE_hp,10)
        self.baddies.append( new_baddie )
                   
        return

    def addGoodBase(self):
        new_goodie = GoodBase( self.baseE_width,
                               self.baseE_height,
                               0,
                               (self.height-self.baseE_height),
                               (0,255,0),
                               self.Gspeed,
                               self.baseE_hp,
                               10 )
        self.goodies.append( new_goodie )

        return

    def addGoodOrc(self):
        new_goodie = GoodOrc( self.baseE_width, self.baseE_height+10, 0, (self.height-self.baseE_height), (0,155,0),self.Gspeed,self.baseE_hp*2.5,20 )
        self.goodies.append( new_goodie )

    def buyTurret(self):
        if self.gold >= 300:
            self.turret = True
            self.turretn.append(1)
            self.gold -= 300

    def buyGBase(self):
        if self.gold >= 100:
            self.addGoodBase()
            self.gold -= 100

    def buyGOrc(self):
        if self.gold >= 250:
            self.addGoodOrc()
            self.gold -= 250


    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )

        rect = pygame.Rect(0,0,self.width,self.height/6)
        surface.fill((155,100,0),rect )

        rect = pygame.Rect(0,200,50,200)
        pygame.draw.rect(surface, (150,150,50),rect)
        rect = pygame.Rect(550,200,50,200)
        pygame.draw.rect(surface, (150,150,50),rect)

        mx,my= self.mouse_pos

        #Goblin button
        x,y,w,h = (40,20,40,40)
        color = (255,255,255)
        if mx >= x and my >= y:
            if mx <= x+w and my <= y+h:
                color =(200,200,200)
                txt = self.font3.render("Goblins: 100g", 100, (255,255,255))
                surface.blit(txt, (250,75))
                if 1 in self.newbuttons:
                    if self.timer == 0:
                        color=(144,144,144)
                        self.buyGBase()
                        self.timer =30
        rect=pygame.Rect(x,y,w,h)
        pygame.draw.rect(surface,color,rect)

        #Orc Button
        x,y,w,h = (100,20,40,40)
        color = (255,255,255)
        if mx >= x and my >= y:
            if mx <= x+w and my <= y+h:
                color =(200,200,200)
                txt = self.font3.render("Orc: 250g", 100, (255,255,255))
                surface.blit(txt, (250,75))
                if 1 in self.newbuttons:
                    if self.timer2 == 0:
                        color=(144,144,144)
                        self.buyGOrc()
                        self.timer2 =30
        rect=pygame.Rect(x,y,w,h)
        pygame.draw.rect(surface,color,rect)

        #Turret Button
        x,y,w,h = (160,20,40,40)
        color = (255,255,255)
        if mx >= x and my >= y:
            if mx <= x+w and my <= y+h:
                color =(200,200,200)
                txt = self.font3.render("Turret: 300g", 100, (255,255,255))
                surface.blit(txt, (250,75))
                if 1 in self.newbuttons:

                    color=(144,144,144)
                    self.buyTurret()

        rect=pygame.Rect(x,y,w,h)
        pygame.draw.rect(surface,color,rect)


        if self.turret == True:

            x,y,w,h = (20, 180, 40, 40)
            rect=pygame.Rect(x,y,w,h)
            pygame.draw.rect(surface,color,rect)



        rect = pygame.Rect(0,0,25,205)
        pygame.draw.rect(surface, (50,50,50),rect)
        rect = pygame.Rect(0,0,20,self.PlayerBaseHP/5)
        pygame.draw.rect(surface, (50,50,50),rect)
        pygame.draw.rect(surface, (255,0,0),rect)

        gold = self.font2.render("Gold  ", 100, (155,155,0))
        surface.blit(gold, (28, 75))
        goldn = self.font2.render(str(self.gold), 100, (155,155,0))
        surface.blit(goldn, (80, 75))


        pygame.draw.rect(surface, (50,50,50),rect, 4)

        rect = pygame.Rect(self.width-20,0,20,200)

        pygame.draw.rect(surface, (50,50,50),rect)
        rect = pygame.Rect(self.width-20,0,20,self.OpponentBaseHP/5)

        surface.fill((255,0,0),rect )
        pygame.draw.rect(surface, (50,50,50),rect, 4)

        rect = pygame.Rect(20,65,self.PlayerXP/5,10)
        surface.fill((150,0,250),rect )
        pygame.draw.rect(surface, (50,50,50),rect, 4)
        if self.gold >=100:
            if self.timer >0:
                rect = pygame.Rect(40,20,self.timer,40)
                pygame.draw.rect(surface, (50,50,50),rect)
        #if self.gold >= 200:
        if self.timer2 >0:
            rect = pygame.Rect(100,20,self.timer2,40)
            pygame.draw.rect(surface, (50,50,50),rect)


        #self.spaceship.draw(surface)
        clock = pygame.time.Clock()
        FPS = 30
        milliseconds = clock.tick(FPS)
        seconds = milliseconds / 1000.0
        #self.baddiegroup.draw(surface)
        #self.goodiegroup.draw(surface)

        for baddie in self.baddies:
            baddie.draw(surface)
            x,y,w,h = baddie.getDimensions()
            rect = pygame.Rect( x,y-20,baddie.GetHP(),5)
            pygame.draw.rect(surface, (255,0,0), rect)
        for goodie in self.goodies:
            goodie.draw(surface)
            x,y,w,h = goodie.getDimensions()
            rect = pygame.Rect( x,y-20,goodie.GetHP(),5)
            pygame.draw.rect(surface, (255,0,0), rect)
        for bullet in self.bullets:
            bullet.draw(surface)
        return


    
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
