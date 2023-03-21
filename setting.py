import pygame
import globalValue as GV
import json

option = json.load(open('option.json','r',encoding='UTF-8'))

class Settings:
    def __init__(self):
        self.logicLoopFps = option["sysSettings"]["logicLoopFps"]
        self.drawLoopFps = option["sysSettings"]["drawLoopFps"]
        self.animateLoopFps = option["sysSettings"]["animateLoopFps"]
        
        self.windowsize = (1280,720)#展示窗口的默认大小
        self.org_windowsize = (1280,720)#原始窗口的大小
        
        self.windowflags = (pygame.RESIZABLE)#可调节窗口大小的模式

        self.printSpeed = option["textSettings"]["printSpeed"]

class KeyboardSettings:
    def __init__(self):
        self.autoPlay = option["keyboardSettings"]["autoPlay"]
        self.skip = option["keyboardSettings"]["skip"]
        self.quickSave = option['keyboardSettings']['quickSave']
        

class TextSettings:
    def __init__(self):
        self.textPrintSpeed = option['textSettings']['printSpeed']
        self.textLineGap = option['textSettings']['textLineGap']
        self.textColor = option['textSettings']['textColor']

        self.charType = option['textSettings']['charType']
        self.textSize = option['textSettings']['textSize']

        self.charBlodType = option['textSettings']['charBlodType']
        self.textBlodSize = option['textSettings']['textBlodSize']

        self.margins = option['textSettings']['margins']