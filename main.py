import pygame
import sys


from asteroidfield import AsteroidField
from constants import *
from player import *
from asteroid import Asteroid
from circleshape import *
from shot import Shot

def main():
    
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #FPS setup/handling 
    # dt => Delta Time

    python_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #Game Loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for members in updatable:
            members.update(dt)

        for obj in asteroids:
            if obj.collision_check(player): 
                print("Game over!")
                sys.exit()

        for obj in asteroids:
            for bullet in shots:
                if obj.collision_check(bullet):
                    obj.split()
                    bullet.kill()

        for members in drawable:
            members.draw(screen)
        

        pygame.display.flip()

        #Pauses gameloop for 1/60 of a second
        #.tick() returns time since it was last called - the delta time in ms
        dt = python_clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()