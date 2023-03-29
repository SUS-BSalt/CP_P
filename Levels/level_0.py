import Objects.AVGObjects as AVGObjects
import Objects.ACTObjects as ACTObjects
import Objects.Scence as Scence
import globalValue as GV

import os
import sys

import pygame

def appendFrame(obj,num,source):
    for i in range(num):
        address = source+'%d'%(i+1)+'.png'
        obj.frameList.append(pygame.image.load(address))

class Manage_Level_0:
    def __init__(self):
        self.activeSituation = True
        self.internalEventList = []
        self.globalEventList = []
        self.followingEventList = []
        
    def act(self):
        for checker in self.followingEventList:
            checker()

    def draw(self):
        pass

    def animate(self):
        pass

    def start(self):
        #self.ACTModule = createACTModule()
        self.AVGModule = createAVGModule()

        self.followingEventList.append(self.check_0)
        print(GV.moduleList)

    def check_0(self):
        for event in self.AVGModule.eventList:
            if event == "END":
                print("end")
                #self.followingEventList.remove(self.check_0)
                GV.moduleList.remove(self.AVGModule)
                self.ACTModule = createACTModule()
                self.followingEventList.remove(self.check_0)
                self.followingEventList.append(self.check_1)

    def check_1(self):
        pass



def createAVGModule():
    #（创建模块）
    module_AVG = AVGObjects.AVGModule(open('books/level_0.txt','r',encoding='UTF-8'))
    GV.controller = module_AVG.controller
    module_AVG.clickArea = [0,470,800,300]
    module_AVG.activeSituation = True
    module_AVG.workingSituation = True
    #（创建模块）
    #（创建textBox）
    module_AVG.textBox = AVGObjects.TextBox(loc=[0,470], size=[800,300])
    module_AVG.textBox.frameList.append(pygame.image.load('source/test/testarea_02.png'))
    module_AVG.textBox.init()
    #（创建textBox）
    #(创建logsBox)
    module_AVG.logsBox = AVGObjects.LogsBox(loc=[0,0], size=[800,770], textBoxHeight=300)
    module_AVG.logsBox.backGroundVision = pygame.image.load('source/UI/logs.png')
    #(创建logsBox)
    #（人物）
    satmic = AVGObjects.Character(size=[150,200],loc=[600,70],color = (200,200,200))
    #（表情1）
    expressions = AVGObjects.Expression()

    expressions.body = pygame.image.load('Source/character/Satmic/body.png')

    expressions.eyes = AVGObjects.Eye(loc=[72,51])
    appendFrame(expressions.eyes,3,"Source/character/Satmic/eye/")

    expressions.mouth = AVGObjects.Mouth(loc=[88,89])
    appendFrame(expressions.mouth,4,"Source/character/Satmic/mouth/")

    satmic.expressionList.append(expressions)
    #（表情1）
    satmic.init()
    satmic.setExpression(0)

    module_AVG.characterDict["Satmic"] = satmic
    #（人物）

    #（人物）
    Azure = AVGObjects.Character(size=[150,200],loc=[700,270],color = (200,200,200))
    #（表情1）
    expressions = AVGObjects.Expression()

    expressions.body = pygame.image.load('Source/character/Azure/blank/body.jpg')

    expressions.eyes = AVGObjects.Eye(loc=[72,51])
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))

    expressions.mouth = AVGObjects.Mouth(loc=[88,89])
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))

    Azure.expressionList.append(expressions)
    #（表情1）
    #（表情2）
    expressions = AVGObjects.Expression()

    expressions.body = pygame.image.load('Source/character/Azure/angry/body.jpg')

    expressions.eyes = AVGObjects.Eye(loc=[72,51])
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))

    expressions.mouth = AVGObjects.Mouth(loc=[88,89])
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))

    Azure.expressionList.append(expressions)
    #（表情2）
    #（表情3）
    expressions = AVGObjects.Expression()

    expressions.body = pygame.image.load('Source/character/Azure/cute/body.jpg')

    expressions.eyes = AVGObjects.Eye(loc=[72,51])
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.eyes.frameList.append(pygame.image.load("Source/test/transparent.png"))

    expressions.mouth = AVGObjects.Mouth(loc=[88,89])
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))
    expressions.mouth.frameList.append(pygame.image.load("Source/test/transparent.png"))

    Azure.expressionList.append(expressions)
    #（表情3）
    Azure.init()
    Azure.setExpression(0)

    module_AVG.characterDict["Azure"] = Azure
    #（人物）

    GV.moduleList.append(module_AVG)

    return module_AVG

def appendObjToScence(obj):
    GV.scence.objList.append(obj)

def createACTModule():
    module_ACT = ACTObjects.ACTModule()
    GV.controller = module_ACT.controller
    GV.moduleList.append(module_ACT)
    GV.scence = Scence.Scence()
    appendObjToScence(Scence.Plane([0,0],(1280,720),pygame.image.load("Source\\Scence\\level_01\\slide\\backGround_0.png"),0))
    appendObjToScence(Scence.Plane([180,0],(1280,720),pygame.image.load("Source\\Scence\\level_01\\slide\\mid_2.png"),0.2))
    appendObjToScence(Scence.Plane([600,0],(1280,720),pygame.image.load("Source\\Scence\\level_01\\slide\\mid_3.png"),0.3))
    

    #appendObjToScence(Scence.BackgroundImage([0,0],(1280,720),pygame.image.load("Source\\test\\testScence.png"),0))


    appendObjToScence(Scence.Plane([500,0],(108,361),pygame.image.load("Source\\Scence\\level_01\\obj\\02_11.png"),0.55))
    appendObjToScence(Scence.Plane([0,0],(538,188),pygame.image.load("Source\\Scence\\level_01\\obj\\02_1.png"),0.95))
    appendObjToScence(Scence.PerspectiveObject([538,0],(461,361),[0,0],[1178,0],"right",pygame.image.load("Source\\Scence\\level_01\\obj\\02_2.png"),0.95))
    
    appendObjToScence(Scence.PerspectiveObject([1376,-37],(447,397),[-351,0],[716,0],"left",pygame.image.load("Source\\Scence\\level_01\\obj\\04_01.png"),1))
    
    appendObjToScence(Scence.PerspectiveObject([961,115],(188,245),[341,188],[1610,188],"right",pygame.image.load("Source\\Scence\\level_01\\obj\\01_2.png"),1))
    appendObjToScence(Scence.PerspectiveObject([1221,166],(118,195),[-158,188],[600,188],"left",pygame.image.load("Source\\Scence\\level_01\\obj\\04_0.png"),1))
    appendObjToScence(Scence.Plane([940,228],(252,133),pygame.image.load("Source\\Scence\\level_01\\obj\\03_1.png"),0.95))
    
    appendObjToScence(Scence.Plane([0,118],(981,243),pygame.image.load("Source\\Scence\\level_01\\obj\\01_1.png"),1))

    #appendObjToScence(Scence.PerspectiveObject([1050,0],(108,361),[600,0],[900,0],"right",pygame.image.load("Source\\Scence\\level_01\\obj\\02_11.png"),0.45))

    appendObjToScence(Scence.PerspectiveObject([1667,-37],(722,397),[1027,0],[2389,0],"right",pygame.image.load("Source\\Scence\\level_01\\obj\\04_2.png"),1))
    
    appendObjToScence(Scence.Plane([1480,0],(543,361),pygame.image.load("Source\\Scence\\level_01\\obj\\wall_05.png"),0.31))


    appendObjToScence(Scence.Plane([1350,145],(179,215),pygame.image.load("Source\\Scence\\level_01\\obj\\combine_01.png"),0.7))
    appendObjToScence(Scence.Plane([1700,137],(175,224),pygame.image.load("Source\\Scence\\level_01\\obj\\combine_02.png"),0.5))

    appendObjToScence(Scence.Plane([2300,273],(255,87),pygame.image.load("Source\\Scence\\level_01\\obj\\combine_03.png"),0.8))

    appendObjToScence(Scence.Plane([1220,-35],(447,397),pygame.image.load("Source\\Scence\\level_01\\obj\\04_1.png"),1))



    
    GV.camera.focalOn(module_ACT.player.loc)
    GV.scence.init(GV.camera.loc)
    return module_ACT


manager = Manage_Level_0()
GV.moduleList.append(manager)
manager.start()