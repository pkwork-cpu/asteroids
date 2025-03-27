# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    clock_object = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set the Player class containers
    Player.containers = (updatable, drawable)
    #kinda same as the line below:
    #updatable.add(player_object)
    #drawable.add(player_object)
    
    # Create a Player instance (it will automatically add itself to the groups)
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    print(len(drawable))
    print(type(drawable.sprites()))
    
    while running:
        for event in pygame.event.get():
            # check for quit event
            if event.type == pygame.QUIT:
                running = False
        
        


        screen.fill((0, 0, 0))  # fill screen with black
        
        
        
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        #player_object.update(dt)
        #player_object.draw(screen)


        pygame.display.flip()   # update the display
        dt = clock_object.tick(60) # limit the frame rate to 60 FPS pause the game loop until 1/60th of a second has passed
        dt = dt / 1000 # convert from milliseconds to seconds
    print("Exiting Asteroids!")
    pygame.quit()



if __name__ == "__main__":
    main()
