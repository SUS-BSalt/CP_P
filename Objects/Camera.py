import globalValue as GV
import pygame

class Camera:
    def __init__(self):
        self.loc = [0,0]
        self.tempCupForCameraLoc = [0,0]
        self.size = [1280,720]
        self.cameraShot = pygame.Surface(self.size)

        self.cameraLocRectify = [0,0]
        self.cameraScaleIndex = GV.settings.windowsize[0] / GV.settings.org_windowsize[0]
        """windowSize / org_windowsize"""
        self.mousePos = (0,0)

    def focalOn(self,focalPointLoc):
        self.loc = [(focalPointLoc[0]-(self.size[0])/2), (focalPointLoc[1]-(self.size[1]/2))]

    def updateCameraLoc(self,rectify):
        self.loc = [self.loc[0]+rectify[0],self.loc[1]+rectify[1]]

    def draw(self,vision,objLocOnPlayGround):
        self.cameraShot.blit(vision,(objLocOnPlayGround[0] - self.loc[0],objLocOnPlayGround[1] - self.loc[1]))

    def getMousePos(self):
        mousePosX = (pygame.mouse.get_pos()[0] + self.loc[0] - self.cameraLocRectify[0])/self.cameraScaleIndex
        mousePosY = (pygame.mouse.get_pos()[1] + self.loc[1] - self.cameraLocRectify[1])/self.cameraScaleIndex
        self.mousePos = (mousePosX, mousePosY)
        return(mousePosX, mousePosY)
    
    def mousePosCheck(self,rect):
        if self.mousePos[0] > rect[0] and self.mousePos[1] > rect[1] \
        and self.mousePos[0] < rect[0]+rect[2] and self.mousePos[1] < rect[1]+rect[3]:
            return True
        else:
            return False
        
    def resetWindow(self,event):
        if event.x/event.y > GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1]:
            GV.settings.windowsize = ((GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1])*event.y,event.y)
            self.cameraScaleIndex = event.y / GV.settings.org_windowsize[1]
        else:
            GV.settings.windowsize = (event.x,event.x/(GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1]))
            self.cameraScaleIndex = event.x / GV.settings.org_windowsize[0]
        #更新摄像机修正位置
        self.cameraLocRectify = [(event.x-GV.settings.windowsize[0])/2,(event.y-GV.settings.windowsize[1])/2]
        GV.screen.fill((0,0,0))