# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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
    asteroids = pygame.sprite.Group()
    
    # Set the Player class containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #kinda same as the line below:
    #updatable.add(player_object)
    #drawable.add(player_object)
    
    # Create a Player instance (it will automatically add itself to the groups)
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    #asteroid_object = Asteroid((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), ASTEROID_MIN_RADIUS)
    #AsteroidField object in the initialization code.
    AstroidField_object = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for quit event
                sys.exit("player quit")
        
        #use group instead of individual objects
        #example:
        #player_object.update(dt)
        #update posisition
        updatable.update(dt)

        screen.fill("black")  # fill screen with black
        
        #use group instead of individual objects
        #example:
        #player_object.draw(screen)
        for draw in drawable:
            draw.draw(screen)
        
        #check for collisions
        for astroid in asteroids:
            if astroid.has_collided(player_object):
                sys.exit("Game Over!")

        pygame.display.flip()   # update the display
        dt = clock_object.tick(60) # limit the frame rate to 60 FPS pause the game loop until 1/60th of a second has passed
        dt = dt / 1000 # convert from milliseconds to seconds
    #pygame.quit()



if __name__ == "__main__":
    main()
