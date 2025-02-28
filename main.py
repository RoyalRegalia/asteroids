import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfields import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #Assign into variable (Meaning: "new object")
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #After changing a static field like containers, make sure to create all Player objects after the change.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) #2 Assign into a variable
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        
        #(old syntax) 
        #player.update(dt) #3 place before rendering for a smoother experience (no lag)
        #(new syntax using groups)
        updatable.update(dt)
        
        screen.fill((0,0,0))

        #(old syntax) 
        #player.draw(screen) #2 or this won't work, #3 This should be done after calculations
        #(new syntax)
        for things in drawable:
            things.draw(screen)
        
        pygame.display.flip()
        
        #limit framerate to 60
        dt = clock.tick(60) / 1000

        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()

