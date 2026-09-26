import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
    clock = pygame.time.Clock()
    dt = 0.0 # delta time

    # Game loop
    while True:
        log_state()
        
        # pygame event queue
        for event in pygame.event.get():
            # If user terminates, exit loop
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        # Refresh screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
