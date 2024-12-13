import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        circle_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, circle_width)

    def update(self, dt):
        #Move in a straight line at a constant speed, per frame 
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            #Generate a random angle between 20 and 50 degress
            random_angle = random.uniform(20,50)

            #Define new velocity/direction based on opposite of random angle (to go opposite direction)

            split_velocity_pos = self.velocity.rotate(random_angle)
            split_velocity_neg = self.velocity.rotate(-random_angle)


            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = split_velocity_pos * 1.2
            new_asteroid_2.velocity = split_velocity_neg * 1.2

            


            