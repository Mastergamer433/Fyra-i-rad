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
<<<<<<< HEAD
        if game_info.login_button.collidepoint(event.pos):
            res = game_info.netThread.getNet().login(game_info.username, game_info.password) 
            print(type(res))
            print(res)
            if res == "1":
                username = ""
                password = ""
            elif res == "0":
                game_info.view = "Game"
                game_info.password = ""
=======
>>>>>>> 06505bee6c1fd2105a4acf76c38977527d233bd5


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
        game_info.CENTER_Y - (game_info.TEXT_FEILD_HEIGHT * 2.5),
        game_info.TEXT_FEILD_WIDTH,
        game_info.TEXT_FEILD_HEIGHT
    ) 
    pygame.draw.rect(
        game_info.WIN,
        (255, 255, 255),
        game_info.usernameFeild
    ) 
    game_info.login_button = pygame.Rect(
        game_info.CENTER_X - (game_info.TEXT_FEILD_WIDTH / 2),
        game_info.CENTER_Y + (game_info.TEXT_FEILD_HEIGHT*1.5),
        game_info.TEXT_FEILD_WIDTH,
        game_info.TEXT_FEILD_HEIGHT
    )
    pygame.draw.rect(
        game_info.WIN,
        (20,200,20),
        game_info.login_button
    )
    if game_info.username == "":
        UsernameText     = game_info.loginFont.render("Username", False, (90, 90, 91))
        UsernameTextRect = UsernameText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)-(game_info.TEXT_FEILD_HEIGHT*2)))
    else:
        UsernameText     = game_info.loginFont.render(game_info.username, False, (90, 90, 91))
        UsernameTextRect = UsernameText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)-(game_info.TEXT_FEILD_HEIGHT*2)))

    if game_info.password == "":
        PasswordText     = game_info.loginFont.render("Password", False, (90, 90, 91))
        PasswordTextRect = PasswordText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)))
    else:
        PasswordText     = game_info.loginFont.render(game_info.password, False, (90, 90, 91))
        PasswordTextRect = PasswordText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)))
    
    loginButtonText      = game_info.loginFont.render("Login", False, (0, 0, 0))
    loginButtonTextRect  = loginButtonText.get_rect(center=(game_info.WIDTH/2, (game_info.HEIGHT/2)+((game_info.TEXT_FEILD_HEIGHT)*2))) 

    game_info.passwordFeild = pygame.Rect(
            game_info.CENTER_X - (game_info.TEXT_FEILD_WIDTH / 2),
            game_info.CENTER_Y - (game_info.TEXT_FEILD_HEIGHT*0.5),
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
    game_info.WIN.blit(loginButtonText, loginButtonTextRect)
