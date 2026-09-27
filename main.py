import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
    clock = pygame.time.Clock()
    dt = 0.0  # delta time
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)  # Positioned at the middle of the screen

    # Game loop
    while True:
        log_state()
        
        # pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user terminates, exit loop
                return
        
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()  # Refresh screen
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
