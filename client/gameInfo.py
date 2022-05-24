import pygame, sys, os

class GameInfo:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.done = False
        self.WIN = pygame.display.set_mode((width, height))
        self.circleSizeHeight = height/7
        self.circleSizeWidth = width/7
        self.clock = pygame.time.Clock()
        self.board = pygame.image.load(os.path.join(sys.path[0], "Assets", "board.png"))
        self.view = "Login"
        self.TEXT_FEILD_WIDTH = (self.WIDTH/10)*5
        self.TEXT_FEILD_HEIGHT = (self.WIDTH/10)*1
        self.CENTER_X = self.WIDTH/2
        self.CENTER_Y = self.HEIGHT/2
        self.loginFont = pygame.font.SysFont('Comic Sans', 30)
        self.userFieldActive = True
        self.passFieldActive = False
        self.username = ""
        self.password = ""
