from circleshape import CircleShape
import pygame

from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen):
        circle_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, circle_width)

    def update(self, dt):
        #Move in a straight line at a constant speed, per frame 
        self.position += (self.velocity * dt)