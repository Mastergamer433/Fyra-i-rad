import pygame
from gameInfo import GameInfo


def main():
    """The main function"""
    done = False
    game_info = GameInfo(630, 630)
    while not done:
        # Varje sekund kör:
        # netSend(UP_MESSAGE)
        # tryTimes=0
        # while netReceive() != UP_MESSAGE:
        #   if(tryTimes==3):
        #       Visa att klienten har tappat
        #       anslutning
        #       break;
        #   netSend(UP_MESSAGE)
        #   tryTimes+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        game_info.WIN.fill((255, 255, 255))
        pygame.draw.rect(
            game_info.WIN,
            (0, 0, 255),
            pygame.Rect(
                0,
                game_info.circleSizeHeight,
                game_info.WIDTH,
            )
        )
        game_info.WIN.blit(game_info.board, (0, game_info.circleSizeHeight))
        pygame.display.flip()
        game_info.clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
