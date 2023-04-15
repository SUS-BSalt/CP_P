import globalValue as GV
import Objects.visionObj as visionObj
import Objects.UI as UI
import pygame

class Manage_OpeningMenu:
    def __init__(self):
        self.activeSituation = True
        self.internalEventList = []
        self.globalEventList = []
        self.followingEventList = []
        self.timer = 0

    
openingMenu = UI.UIModule()
GV.moduleList.append(openingMenu)

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




#开始菜单
startMenu = UI.Menu(activeSituation=True, size=[1280,720])
startMenu.frameList.append(pygame.image.load("Source/UI/StartMenu.png"))

def startMethod():
    openingMenu.menuList.clear()
    import Levels.escMenu
    import Levels.level_0
    GV.moduleList.remove(openingMenu)

appendButtonToMenu(startMenu,startMethod,loc=[100,150],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("开始",False,(0,0,0)),
                                    GV.UIfont_02.render("开始",False,(0,0,0))
                                ])

def loadMethod():
    for menu in openingMenu.menuList:
        menu.activeSituation = False
    loadMenu.activeSituation = True

appendButtonToMenu(startMenu,loadMethod,loc=[100,300],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("载入",False,(0,0,0)),
                                    GV.UIfont_02.render("载入",False,(0,0,0))
                                ])

def optionMethod():
    for menu in openingMenu.menuList:
        menu.activeSituation = False
    optionMenu.activeSituation = True

appendButtonToMenu(startMenu,optionMethod,loc=[100,450],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("设置",False,(0,0,0)),
                                    GV.UIfont_02.render("设置",False,(0,0,0)),
                                ])



def confirmMenuMethod():
    for menu in openingMenu.menuList:
        menu.activeSituation = False
    confirmMenu.activeSituation = True

appendButtonToMenu(startMenu,confirmMenuMethod,loc=[100,600],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("退出",False,(0,0,0)),
                                    GV.UIfont_02.render("退出",False,(0,0,0)),
                                ])
openingMenu.menuList.append(startMenu)
#开始菜单#######################################################


def backToStartMenuMethod():
    for menu in openingMenu.menuList:
        menu.activeSituation = False
    startMenu.activeSituation = True

def exitMethod():
    GV.sysSymbol.set('gameRun',False)

def noneMethod():
    return 0

#确认退出菜单
confirmMenu = UI.Menu(activeSituation=False)
confirmMenu.frameList.append(pygame.image.load("Source/UI/StartMenu.png"))

appendButtonToMenu(confirmMenu,exitMethod,loc=[500,350],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("是",False,(0,0,0)),
                                    GV.UIfont_02.render("是",False,(0,0,0))
                                ])

appendButtonToMenu(confirmMenu,backToStartMenuMethod,loc=[700,350],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("否",False,(0,0,0)),
                                    GV.UIfont_02.render("否",False,(0,0,0))
                                ])
appendButtonToMenu(confirmMenu,noneMethod,loc=[400,250],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("确认退出到桌面？",False,(0,0,0)),
                                    GV.UIfont_01.render("确认退出到桌面？",False,(0,0,0))
                                ])
openingMenu.menuList.append(confirmMenu)
#确认退出菜单#########################################################




#载入菜单
loadMenu = UI.Menu(activeSituation=False)
loadMenu.frameList.append(pygame.image.load("Source/UI/StartMenu.png"))


appendButtonToMenu(loadMenu,backToStartMenuMethod,loc=[100,600],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("返回",False,(0,0,0)),
                                    GV.UIfont_02.render("返回",False,(0,0,0)),
                                ])

openingMenu.menuList.append(loadMenu)
#载入菜单#####################################################

#设置菜单
optionMenu = UI.Menu(activeSituation=False)
optionMenu.frameList.append(pygame.image.load("Source/UI/StartMenu.png"))
appendButtonToMenu(optionMenu,backToStartMenuMethod,loc=[100,600],size=[100,50],frameList=
                                [
                                    GV.UIfont_01.render("返回",False,(0,0,0)),
                                    GV.UIfont_02.render("返回",False,(0,0,0)),
                                ])
#appendButtonToMenu(optionMenu,
openingMenu.menuList.append(optionMenu)
#设置菜单######################################################





openingMenu.activeSituation = True

GV.controller = openingMenu.controller


def appendFrame(obj,num,source):
    for i in range(num):
        address = source+'%d'%(i+1)+'.png'
        obj.frameList.append(pygame.image.load(address))



class OpenVision:
    def __init__(self,loc = [0,0], size = [0,0]):
        self.loc = loc
        self.size = size
        self.rect = loc+size
        self.frameList = [
            pygame.image.load("source/maker.png"),
            pygame.image.load("source/pygame.png")
        ]
        self.vision = self.frameList[0]
        self.animationList = []
        self.rect = loc+size

        self.timer = 0

    def act(self):
        self.timer += 1
        if self.timer == 50:
            self.vision = self.frameList[1]
        if self.timer == 100:
            pass

"""openVision =  OpenVision()
GV.objActiveList.append(openVision)
GV.layer_3.append(openVision)"""


