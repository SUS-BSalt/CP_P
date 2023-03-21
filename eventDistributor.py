import pygame
import globalValue as GV
from setting import KeyboardSettings


class EventDistributor:
    def __init__(self):
        pass

    def mouseActiveClean(self):
        for obj in GV.mouseActiveList:
            if not GV.mousePosCheck(obj.rect):
                GV.mouseActiveList.remove(obj)
                obj.animation.init()
    
    def check(self):
        self.mouseActiveClean()
        GV.controlSymbol.set("click",False)
        GV.mousePos = GV.getMousePos()
        print(GV.mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GV.sysSymbol.set('gameRun',False)
            

            elif event.type == pygame.KEYUP:
                match pygame.key.name(event.key):
                    case GV.keyboardSettings.autoPlay:
                        if GV.controlSymbol.get("autoPlay"):
                            GV.controlSymbol.set("autoPlay",False)
                        else:
                            GV.controlSymbol.set("autoPlay",True)

            elif event.type == pygame.MOUSEBUTTONUP:
                GV.controlSymbol.set("click",True)

            elif event.type == pygame.WINDOWRESIZED:
                #变化windowsize
                if event.x/event.y > GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1]:
                    GV.settings.windowsize = ((GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1])*event.y,event.y)
                    GV.cameraScaleIndex = event.y / GV.settings.org_windowsize[1]
                else:
                    GV.settings.windowsize = (event.x,event.x/(GV.settings.org_windowsize[0]/GV.settings.org_windowsize[1]))
                    GV.cameraScaleIndex = event.x / GV.settings.org_windowsize[0]
                #更新摄像机修正位置
                GV.cameraRectify = [(event.x-GV.settings.windowsize[0])/2,(event.y-GV.settings.windowsize[1])/2]
                GV.screen.fill((0,0,0))


    

