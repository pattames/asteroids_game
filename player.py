import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Pre-written drawing geometry (triangle) for the ship
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b ,c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # "move-left" key
            self.rotate(dt * -1)
        if keys[pygame.K_d]:  # "move-right" key
            self.rotate(dt)
        if keys[pygame.K_w]:  # "move-forwards" key
            self.move(dt)
        if keys[pygame.K_s]:  # "move-backwards" key
            self.move(dt * -1)

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)  # matching player's rotation
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt  # the length the player should move
        self.position += rotated_with_speed_vector  # move player
