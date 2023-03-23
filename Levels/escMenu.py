import globalValue as GV
import Objects.visionObj as visionObj
import Objects.UI as UI
import pygame
import os
import sys




def appendButtonToMenu(menu, method,loc,size, frameList):
    button= UI.Button(loc=loc,size=size, method = method)

    button.animationList.append(visionObj.SwitchFrame(button,0))
    #添加切换到第一帧的方法
    button.animationList.append(visionObj.SwitchFrame(button,1))
    #添加切换到第二帧的方法
        
    for frame in frameList:
        button.frameList.append(frame)
    button.vision = button.frameList[0]
    menu.buttonList.append(button)
    return button

#创建module
escMenuModule = UI.UIModule()
GV.escMenuModule = escMenuModule

#esc菜单
escMenu = UI.Menu(activeSituation=True, size=[1280,720])
escMenu.frameList.append(pygame.image.load("Source/UI/StartMenu.png"))

def backMethod():
    GV.controller = GV.tempCupForModule.controller
    GV.tempCupForModule.activeSituation = True
    GV.camera.loc = GV.camera.tempCupForCameraLoc
    
    GV.moduleList.remove(GV.escMenuModule)

appendButtonToMenu(escMenu,backMethod,loc=[100,450],size=[150,80],frameList=
                                [
                                    GV.UIfont_01.render("返回游戏",False,(0,0,0)),
                                    GV.UIfont_02.render("返回游戏",False,(0,0,0))
                                ])

def backToOpeningMenu():
    #@Todo保存游戏
    GV.moduleList.clear()
    GV.sysSymbol.set("gameRun",False)
    os.execl(sys.executable,sys.executable,"./main.py")
    
    

appendButtonToMenu(escMenu,backToOpeningMenu,loc=[100,600],size=[150,80],frameList=
                                [
                                    GV.UIfont_01.render("返回主菜单",False,(0,0,0)),
                                    GV.UIfont_02.render("返回主菜单",False,(0,0,0))
                                ])
    
escMenuModule.menuList.append(escMenu)