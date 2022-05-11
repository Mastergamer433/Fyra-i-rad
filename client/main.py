import pygame
import numpy as np
import threading
import time
import os
from  net import *
from logger import *

WIDTH, HEIGHT = 700, 700  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

 
def main():
    done = False
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

        endTime = time.time()
    pygame.quit()

if __name__ == "__main__":
    main()
