import pygame
import globalValue as GV
import Objects.visionObj as visionObj
import Objects.ACTPlayer as ACTPlayer
import Objects.ACTUI as ACTUI

class ACTModule:
    def __init__(self,book):
        self.activeSituation = True
        self.bottomUI = ACTUI.bottomUI((1280,360),(0,0),self,book)
        
        self.enemyList = []

        self.timer = 0
        self.player = ACTPlayer.Player([1300,363])

        self.playGround = pygame.Surface((640,360))

        self.playerBeatSymbol = False
        self.playerBeatAward = False
        self.beatSpeed = 30
        #节奏速度
        self.beatZoneStartPoint = 20
        #判定区间开始的节点

    def controller(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                match pygame.key.name(event.key):
                    case "a":
                        self.player.leftMoveSymbol = True
                        self.player.inputList.append("l")
                    case "d":
                        self.player.rightMoveSymbol = True
                        self.player.inputList.append("r")
                    
                    case "shift":
                        self.player.shiftSymbol = True
                        self.player.inputList.append("shift")

                    case "escape":
                        print("coerciveActingSymbol",self.player.coerciveActingSymbol)
                        print("playLoc",self.player.loc)
                        print("playerFaceSide",self.player.faceSide)
                        print("cameraLoc",GV.camera.loc)
                        print("mousePos",GV.camera.mousePos)
                        print("word_0",self.bottomUI.wordsList[0].self.colorGradientSym)
                        GV.controller = GV.escMenuModule.controller
                        GV.escMenuModule.activeSituation = True
                        GV.camera.tempCupForCameraLoc = GV.camera.loc
                        GV.camera.loc = [0,0]
                        GV.moduleList.append(GV.escMenuModule)
                        GV.tempCupForModule = self
                        self.activeSituation = False
                        

            if event.type == pygame.KEYUP:
                match pygame.key.name(event.key):
                    case "a":
                        self.player.leftMoveSymbol = False
                        self.player.inputList.append("keyUP")

                    case "d":
                        self.player.rightMoveSymbol = False
                        self.player.inputList.append("keyUP")
                    
                    case "shift":
                        self.player.shiftSymbol = False
                        self.player.inputList.append("shiftUP")


            elif event.type == pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 1 :
                        self.player.inputList.append("a")
                    case 3:
                        self.player.inputList.append("d")

            elif event.type == pygame.QUIT:
                GV.sysSymbol.set('gameRun',False)

            elif event.type == pygame.WINDOWRESIZED:
                #变化windowsize
                GV.camera.resetWindow(event)
    def act(self):
        self.timer += 1
        if self.timer == self.beatSpeed:
            if self.playerBeatAward == True:
                #奖励
                pass
            for enemy in self.enemyList:
                enemy.act()
        self.player.act()
        self.bottomUI.act()



        
        pass
    def draw(self):
        GV.camera.cameraLocOnThatFrame = tuple(GV.camera.loc)
        GV.scence.update(GV.camera.loc)
        GV.scence.draw()
        GV.camera.draw(self.player.redPoint, self.player.loc)
        self.player.draw()
        self.bottomUI.draw()

        
    def animate(self):
        self.bottomUI.animate()
        
        pass
        #print(self.camera.loc)
        #self.player.animate()
        















"""
def actionDistributor(self):
        if "a" in self.inputList:
            #攻击
            if GV.getMousePos()[0] >= self.loc:
                #向右攻击
                if "r" in self.inputList:
                    #向右攻击，向右走
                    if self.faceSide == "r":
                        #向右攻击，向右走，面向右
                        pass
                    else:
                        #向右攻击，向右走，面向左
                        pass
                elif "l" in self.inputList:
                    #向右攻击，向左走
                    if self.faceSide == "r":
                        #向右攻击，向左走，面向右
                        pass
                    else:
                        #向右攻击，向左走，面向左
                        pass
                else:
                    #向右攻击，不动
                    if self.faceSide == "r":
                        #向右攻击，不动，面向右
                        pass
                    else:
                        #向右攻击，不动，面向左
                        pass
                
            else:
                #向左攻击
                if "r" in self.inputList:
                    #向左攻击，向右走
                    if self.faceSide == "r":
                        #向左攻击，向右走，面向右
                        pass
                    else:
                        #向左攻击，向右走，面向左
                        pass
                elif "l" in self.inputList:
                    #向左攻击，向左走
                    if self.faceSide == "r":
                        #向左攻击，向左走，面向右
                        pass
                    else:
                        #向左攻击，向左走，面向左
                        pass
                else:
                    #向左攻击，不动
                    if self.faceSide == "r":
                        #向左攻击，不动，面向右
                        pass
                    else:
                        #向左攻击，不动，面向左
                        pass
        elif "d" in self.inputList:
            #防御
            if GV.getMousePos()[0] >= self.loc:
                #向右防御
                if self.faceSide == "r":
                    #向右防御，不动，面向右
                    pass
                else:
                    #向右防御，不动，面向左
                    pass
            else:
                 #向左防御
                if self.faceSide == "r":
                    #向左防御，不动，面向右
                    pass
                else:
                    #向左防御，不动，面向左
                    pass

        elif "r" in self.inputList:
            #向右走
            if GV.getMousePos()[0] >= self.loc:
                #向右走，面向右
                if self.shiftSymbol == True:
                    #向右走，面向右，冲刺！
                    pass
                else:
                    #向右走，面向右，慢走
                    pass
            else:
                #向右走，面向左
                if self.shiftSymbol == True:
                    #向右走，面向左，冲刺！
                    pass
                else:
                    #向右走，面向左，慢走
                    pass

        elif "l" in self.inputList:
            #向左走
            if GV.getMousePos()[0] >= self.loc:
                #向左走，面向右
                if self.shiftSymbol == True:
                    #向左走，面向右，冲刺！
                    pass
                else:
                    #向左走，面向右，慢走
                    pass
            else:
                #向左走，面向左
                if self.shiftSymbol == True:
                    #向左走，面向左，冲刺！
                    pass
                else:
                    #向左走，面向左，慢走
                    pass

        else:
            #无输入，查看自身控制标签进行动作
            if self.rightMoveSymbol:
                #向右走
                if GV.getMousePos()[0] >= self.loc:
                    #向右走，面向右
                    if self.shiftSymbol == True:
                        #向右走，面向右，奔跑
                        pass
                    else:
                        #向右走，面向右，慢走
                        pass
                else:
                    #向右走，面向左，慢走
                    pass
            elif self.leftMoveSymbol:
                #向左走
                if GV.getMousePos()[0] >= self.loc:
                    #向左走，面向右，慢走
                    pass
                else:
                    #向左走，面向左
                    if self.shiftSymbol == True:
                        #向左走，面向左，奔跑
                        pass
                    else:
                        #向左走，面向左，慢走
                        pass
            pass
"""