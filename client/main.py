import pygame
import numpy as np
import threading
import time
import os
from  net import *
from logger import *

WIDTH, HEIGHT = 700, 700  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
active=True
def main():
    password=""
    username=""
     
    done = False
    rect = pygame.Rect(0,0,50,50)
    vel = 2
    ClientThread = threading.Thread(target=netInit, args=())
    while done != True:
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
        startTime = time.time()
        for event in pygame.event.get():
            log(event, "EVENT")
            if event.type == pygame.QUIT:
                done = True
            elif event.type == 771:
                if active:
                    username+=event.text
            elif event.type == 768:
                if event.key == 13:
                    print(username)
        
        WIN.fill((255,255,255)) 
        pygame.draw.rect(WIN, (255,210,20), rect)
        
         
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
