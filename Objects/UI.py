import pygame
import globalValue as GV
import Objects.visionObj as visionObj

class UIModule:
    def __init__(self):
        self.activeSituation = False

        self.menuList = []

    def controller(self):
        GV.controlSymbol.set("click",False)
        GV.camera.getMousePos()
        for event in pygame.event.get():            
            if event.type == pygame.KEYUP:
                if pygame.key.name(event.key) == "escape":
                    #todo新增一个标签，用于按钮方法的检测
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                GV.controlSymbol.set("click",True)
            
            elif event.type == pygame.QUIT:
                GV.sysSymbol.set('gameRun',False)

            elif event.type == pygame.WINDOWRESIZED:
                #变化windowsize
                GV.camera.resetWindow(event)


    def act(self):
        for menu in self.menuList:
            if menu.activeSituation == True:
                menu.act()

    def animate(self):
        for menu in self.menuList:
            if menu.activeSituation == True:
                menu.animate()

    def draw(self):
        for menu in self.menuList:
            if menu.activeSituation == True:
                menu.draw()


class Menu:
    def __init__(self,loc = [0,0], size = [0,0], activeSituation = False):
        self.activeSituation = activeSituation
        
        self.loc = loc
        self.size = size
        self.rect = loc+size
        self.vision = pygame.Surface(tuple(size))
        self.frameList = []
        self.animationList = []
        self.buttonList = []
        

    def act(self):
        for button in self.buttonList:
            if GV.camera.mousePosCheck(button.rect) == True:
                if GV.controlSymbol.get('click'):
                    button.act()
                    GV.controlSymbol.set('click', False)

    def draw(self):
        GV.camera.draw(self.frameList[0],self.loc)
        for button in self.buttonList:
            GV.camera.draw(button.vision,button.loc)
                
    def animate(self):
        for button in self.buttonList:
            if GV.camera.mousePosCheck(button.rect) == True and button.mouseActive == False:
                button.mouseActive = True
                button.animationList[1].act()
            elif GV.camera.mousePosCheck(button.rect) == False and button.mouseActive == True:
                button.mouseActive = False
                button.animationList[0].act()


class Button:
    def __init__(self,loc = [0,0], size = [0,0], method = None):
        self.mouseActive = False
        self.loc = loc
        self.size = size
        self.rect = loc+size
        self.vision = None
        self.frameList = []
        self.animationList = []
        
        self.method = method

        self.animationList.append(visionObj.SwitchFrame(self,0))
        #切换到第一帧的方法
        self.animationList.append(visionObj.SwitchFrame(self,1))
        #切换到第二帧的方法
        

    def act(self):
        self.method()

    def animate(self):
        if GV.camera.mousePosCheck(self.rect) == True and self.mouseActive == False:
            self.mouseActive = True
            self.animationList[1].act()
        elif GV.camera.mousePosCheck(self.rect) == False and self.mouseActive == True:
            self.mouseActive = False
            self.animationList[0].act()