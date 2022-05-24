import pygame
from gameInfo import GameInfo
from loop import gameLoop

def main():
    """The main function"""
    done = False
    game_info = GameInfo(630, 630)
    while not game_info.done:
        gameLoop(game_info)

if __name__ == "__main__":
    main()
