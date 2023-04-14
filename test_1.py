import pygame
pygame.init()
import threading
import time

pygame.mixer.init()

pygame.display.set_caption("CP_P")
screen = pygame.display.set_mode((1280,720))

ss = pygame.image.load("Source\\test\\testScence.png")
dd = pygame.image.load("Source\\test\\testarea_01.png")
a = pygame.mixer.Sound("Source\\sadIntro_01.ogg")
#a.play()
#pygame.mixer.music.load("Source\\sadIntro_01.ogg")
#pygame.mixer.music.play()

class Timer:
     def __init__(self):
          self.a = 1


c_timer = Timer()

def loop_0():
    timer = 0
    while True:
        c_timer.a = 1
        if timer == 10:
             a.play()
             timer = 0
             timer
        screen.blit(ss,(0,0))
        #pygame.mixer.music.play()
        pygame.display.update()
        print("running")
        time.sleep(0.1)
        
def loop_1():
     while True:
          screen.blit(dd,(50,0))
          
    
def runningStart():
        loop_0()
runningStart()