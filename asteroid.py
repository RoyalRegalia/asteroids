import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split_on_kill(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #randomize    
        random_angle = random.uniform(20,50)

        new_vect_one = self.velocity.rotate(random_angle)
        new_vect_two = self.velocity.rotate(-random_angle)

        old_radius = self.radius #probably not necessary unless you want to use this old radius somewhere else
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_one.velocity = new_vect_one * 1.2
        
        new_asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_two.velocity = new_vect_two * 1.2