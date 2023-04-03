import pygame
pygame.init()
import threading

pygame.display.set_caption("CP_P")
screen = pygame.display.set_mode((1280,720))

ss = pygame.image.load("Source\\test\\testScence.png")
dd = pygame.image.load("Source\\test\\testarea_01.png")
def loop_0():
    while True:
        screen.blit(ss,(0,0))
        
def loop_1():
     while True:
          screen.blit(dd,(50,0))
          pygame.display.update()
    
def runningStart():
        thread_01 = threading.Thread(target = loop_0)
        thread_01.start()
        loop_1()
runningStart()