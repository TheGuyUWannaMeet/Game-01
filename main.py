import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.font.init()
    c = SpaceshipAdventure(600, 400, 30)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

