import pygame
import setting
import Objects.Scence as Scence

settings = setting.Settings()
keyboardSettings = setting.KeyboardSettings()
textSettings = setting.TextSettings()


pygame.display.set_caption("CP_P")
screen = pygame.display.set_mode(settings.windowsize,settings.windowflags)
playGround = pygame.Surface((0,0))



class GlobalValue:
    #设置全局变量，一共两个方法，set与get
    def __init__(self):
        self.content = {}
    
    def set(self, name, value):
        self.content[name] = value
    
    def get(self, name, default=None):
        try:
            return self.content[name]
        except:
            return default
testRect = pygame.Rect(0,0,100,100)
sysSymbol = GlobalValue()
controlSymbol = GlobalValue()




moduleList = []
#正在活动的模块，每个循环都会执行每个在这里面的模块的act与draw与animate



escMenuModule = None
#因为esc菜单不需要经常删改，所以扔到这里面缓解其他列表查找压力
tempCupForModule = None
UIfont_01 = pygame.font.Font(textSettings.charType,40)
UIfont_02 = pygame.font.Font(textSettings.charType,50)
toDoList = []
#把level里的紧跟事件加上判断写成函数，丢进这个list让逻辑线程循环检测是否应该执行

controller = None


class Camera:
    def __init__(self):
        self.loc = [0,0]
        self.tempCupForCameraLoc = [0,0]
        self.size = [1280,720]
        self.cameraShot = pygame.Surface(self.size)

        self.cameraLocRectify = [0,0]
        self.cameraScaleIndex = settings.windowsize[0] / settings.org_windowsize[0]
        """windowSize / org_windowsize"""
        self.mousePos = (0,0)

    def focalOn(self,focalPointLoc):
        self.loc = [(focalPointLoc[0]-(self.size[0])/2), (focalPointLoc[1]-(self.size[1]/2))]
        scence.update(self.loc)

    def updateCameraLoc(self,rectify):
        self.loc = [self.loc[0]+rectify[0],self.loc[1]+rectify[1]]
        scence.update(self.loc)

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
        if event.x/event.y > settings.org_windowsize[0]/settings.org_windowsize[1]:
            settings.windowsize = ((settings.org_windowsize[0]/settings.org_windowsize[1])*event.y,event.y)
            self.cameraScaleIndex = event.y / settings.org_windowsize[1]
        else:
            settings.windowsize = (event.x,event.x/(settings.org_windowsize[0]/settings.org_windowsize[1]))
            self.cameraScaleIndex = event.x / settings.org_windowsize[0]
        #更新摄像机修正位置
        self.cameraLocRectify = [(event.x-settings.windowsize[0])/2,(event.y-settings.windowsize[1])/2]
        screen.fill((0,0,0))

camera = Camera()
scence = Scence.Scence()
