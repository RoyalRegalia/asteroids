import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        player_draw = pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        #change self.rotation
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self,dt):
        
        #forward is equal to pygame function Vector (2D), (X,Y).rotate() method of player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #change self.position by forward multiplied by player speed x delta time (fps)
        self.position += forward * PLAYER_SPEED * dt 
