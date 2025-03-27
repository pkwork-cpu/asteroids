# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Exiting Asteroids2!")

        screen.fill((0, 0, 0))  # fill screen with black
        pygame.display.flip()   # update the display
    print("Exiting Asteroids!")
    pygame.quit()
if __name__ == "__main__":
    main()
