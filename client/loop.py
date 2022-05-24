import pygame
from login import loginDraw, loginEvent
pygame.font.init() 

username = ""
password = ""
def gameLoop(game_info):
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
        print(event)
        if game_info.view == "Login":
            loginEvent(event, game_info)
        if event.type == pygame.QUIT:
            game_info.done = True
    game_info.WIN.fill((255, 255, 255))
    if game_info.view == "Game":
        pygame.draw.rect(
            game_info.WIN,
            (0, 0, 255),
            pygame.Rect(
                0,
                game_info.circleSizeHeight,
                game_info.HEIGHT-game_info.circleSizeHeight,
                game_info.WIDTH
            )
        )
        game_info.WIN.blit(game_info.board, (0, game_info.circleSizeHeight))
           
    elif game_info.view == "Login":
        loginDraw(game_info)
    pygame.display.flip()
    game_info.clock.tick(60)
 
