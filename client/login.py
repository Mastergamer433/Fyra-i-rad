import pygame
def loginEvent(event, game_info):
    if event.type == 768:
        if event.key == 13: 
            if game_info.net.login(username, password) == 0:
                print(game_info.username)
                print(game_info.password)
                game_info.view = "Game"  
            else:
                password = ""
                username = ""

            print("")
        else:
            if game_info.userFieldActive:
                game_info.username += event.unicode
            if game_info.passFieldActive:
                game_info.password += event.unicode
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if game_info.passwordFeild.collidepoint(event.pos):
            game_info.userFieldActive = False
            game_info.passFieldActive = True
        if game_info.usernameFeild.collidepoint(event.pos):
            game_info.userFieldActive = True
            game_info.passFieldActive = False


def loginDraw(game_info):
    pygame.draw.rect(
        game_info.WIN,
        (0, 255, 0),
        pygame.Rect(
            0,
            0,
            game_info.HEIGHT,
            game_info.WIDTH
        )
    )
    game_info.usernameFeild = pygame.Rect(
            game_info.CENTER_X - (game_info.TEXT_FEILD_WIDTH / 2),
            game_info.CENTER_Y - (game_info.TEXT_FEILD_HEIGHT * 1.5),
            game_info.TEXT_FEILD_WIDTH,
            game_info.TEXT_FEILD_HEIGHT
        ) 
    pygame.draw.rect(
        game_info.WIN,
        (255, 255, 255),
        game_info.usernameFeild
    )
    if game_info.username == "":
        UsernameText = game_info.loginFont.render("Username", False, (90, 90, 91))
        UsernameTextRect = UsernameText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)-(game_info.TEXT_FEILD_HEIGHT)))
    else:
        UsernameText = game_info.loginFont.render(game_info.username, False, (90, 90, 91))
        UsernameTextRect = UsernameText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)-(game_info.TEXT_FEILD_HEIGHT)))

    if game_info.password == "":
        PasswordText = game_info.loginFont.render("Password", False, (90, 90, 91))
        PasswordTextRect = PasswordText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)+((game_info.TEXT_FEILD_HEIGHT)*1.5)))
    else:
        PasswordText = game_info.loginFont.render(game_info.password, False, (90, 90, 91))
        PasswordTextRect = PasswordText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)+((game_info.TEXT_FEILD_HEIGHT)*1.5)))
        
    game_info.passwordFeild = pygame.Rect(
            game_info.CENTER_X - (game_info.TEXT_FEILD_WIDTH / 2),
            game_info.CENTER_Y + (game_info.TEXT_FEILD_HEIGHT),
            game_info.TEXT_FEILD_WIDTH,
            game_info.TEXT_FEILD_HEIGHT
        ) 
    pygame.draw.rect(
        game_info.WIN,
        (255, 255, 255),
        game_info.passwordFeild
    )
    if not game_info.userFieldActive:
        game_info.WIN.blit(UsernameText, UsernameTextRect)
    if not game_info.passFieldActive:
        game_info.WIN.blit(PasswordText, PasswordTextRect)

