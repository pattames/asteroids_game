import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt  # Moves in a straight line at constant speed

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:  # Small one, we're done
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        asteroid_1_new_movement = self.velocity.rotate(random_angle)
        asteroid_2_new_movement = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid_1.velocity = asteroid_1_new_movement * 1.2
        asteroid_2.velocity = asteroid_2_new_movement * 1.2
