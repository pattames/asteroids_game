import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    # New instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)

    while True:
        log_state()
        
        # Start processing pygame event queue
        for event in pygame.event.get():
            # If the user terminates the program, exit loop
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
