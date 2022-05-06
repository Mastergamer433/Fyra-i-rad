import pygame
import numpy as np

WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    done = False
    while done != True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                done = True
    pygame.quit()

if __name__ == "__main__":
    main()