# this allows us to use code from the open-source pygame library
import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # Initialize the game
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
    shots = pygame.sprite.Group()
    # Assign class containers to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    #kinda same as the line below:
    #updatable.add(player_object)
    #drawable.add(player_object)
    
    # Create a Player instance (it will automatically add itself to the groups)
    #Spawn player
    player_object = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    #AsteroidField object in the initialization code.
    #Spawn asteroids
    AstroidField_object = AsteroidField()

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for quit event
                sys.exit("player quit")
        
        #use group instead of individual objects
        #example:
        #player_object.update(dt)
        #update posisitions
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
            for shot in shots:
                if astroid.has_collided(shot):
                    astroid.split()
                    shot.kill()

        pygame.display.flip()   # update the display
        dt = clock_object.tick(60) # limit the frame rate to 60 FPS pause the game loop until 1/60th of a second has passed
        dt = dt / 1000 # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
