import pygame
import setting
import Objects.Camera
import Objects.Scence

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
    
    def get(self, name, default=False):
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




camera = Objects.Camera.Camera()
scence = Objects.Scence.Scence()
