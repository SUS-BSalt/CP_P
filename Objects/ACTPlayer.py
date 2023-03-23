import pygame
import globalValue as GV

class Player:
    def __init__(self, loc):
        self.inputList = []

        self.eventList = []

        self.loc = loc

        self.faceSide = "r"
        self.frontFoot = "l"

        self.beatingSymbol = False
        self.rightMoveSymbol = False
        self.leftMoveSymbol = False
        self.shiftSymbol = False
        self.defenceSymbol = False

        self.coerciveActingSymbol = False
        self.beHitSymbol = False

        self.timer = 0

        self.cameraIsNotCenterSym = False

        self.standing = Standing(self)
        self.standingToLeft = Standing(self)
        self.standingToLeft.changeFaceSides()

        self.walking = Walking(self)
        self.walkingToLeft = Walking(self).changeFaceSides()
        self.cameraMovingSpeed = 3.25
        self.cameraMovingSpeedToLeft = -3.25

        self.normalAttack = NormalAttack(self)
        self.normalAttackToLeft = NormalAttack(self)
        self.normalAttackToLeft.changeFaceSides()

        self.currentAction = self.standing
        self.standing.execute()

        self.redPoint = pygame.image.load("Source\\test\\redPoint.png")
        

    def init(self):
        self.inputList.clear()

    def cameraTracking(self):
        if self.currentAction == self.standing:
            pass
        elif self.cameraIsNotCenterSym:
            if self.loc[0] > (GV.camera.loc[0] + 680):
                GV.camera.updateCameraLoc([15,0])
            elif self.loc[0] < (GV.camera.loc[0] + 600):
                GV.camera.updateCameraLoc([-15,0])
            else:
                self.cameraIsNotCenterSym = False

        elif self.loc[0] > (GV.camera.loc[0] + 800) or self.loc[0] < (GV.camera.loc[0] + 480):
            self.cameraIsNotCenterSym = True

    def faceSideCheck(self):
        if GV.camera.mousePos[0] >= self.loc[0]:
            if self.faceSide == "l":
                self.loc[0] += 25
                self.faceSide = "r"
                return True
        else:
            if self.faceSide == "r":
                self.loc[0] -= 25
                self.faceSide = "l"
                return True
        return False


    def act(self):
        #只认可最新输入的两个指令
        #节奏的判定
        #当其执行攻击或防御时，传递一个打击的事件，让上层的模组去读取。
        #print(self.loc,GV.camera.getMousePos())
        self.cameraTracking()
        if self.beHitSymbol == True:
            #被打中时
            pass

        elif self.coerciveActingSymbol == True:
            #如果在强制行动中，执行当前动作
            self.currentAction.act()
            pass

        elif self.coerciveActingSymbol == False:
            #当玩家不在强制行动中
            self.currentAction.act()
            #执行当前动作
            
            if self.inputList != []:
                self.timer = 0
                self.inputList = self.inputList[-3:]


                self.actionDistributor()
                #print(self.loc[0],GV.getMousePos()[0])
                self.inputList.clear()
            
            GV.camera.getMousePos()
            if self.faceSideCheck():
                self.resetAction()
                pass

            #如果输入列表不为空，执行输入信号，归零计时器，重置动作

        
    def draw(self):
        GV.camera.draw(self.currentAction.vision,self.currentAction.picLoc)

        pass
        


    def animate(self):
        pass


    def resetAction(self):
        self.timer = 0
        if self.rightMoveSymbol == True:
            #向右走
            if self.faceSide == "r":
                #向右走，面向右
                if self.shiftSymbol == True:
                    #向右走，面向右，奔跑
                    pass
                else:
                    #向右走，面向右，慢走
                    self.walking.execute()
            else:
                #向右走，面向左，后退
                self.faceSide = "l"
                pass
        elif self.leftMoveSymbol == True:
            #向左走
            if self.faceSide == "r":
                #向左走，面向右，后退
                self.faceSide = "r"
                pass
            else:
                #向左走，面向左
                if self.shiftSymbol == True:
                    #向左走，面向左，奔跑
                    pass
                else:
                    #向左走，面向左，慢走
                    self.walkingToLeft.execute()

        else:
            #站立
            if self.faceSide == "r":
                    self.standing.execute()
            else:
                self.standingToLeft.execute()

    def actionDistributor(self):
        if "a" in self.inputList:
            #攻击
            self.eventList.append("a")
            if self.faceSide == "r":
                #向右攻击
                if self.faceSide == "l":
                    #向右攻击，面向左，回身攻击
                    self.normalAttack.execute()
                    self.faceSide = "r"
                    pass
                elif self.leftMoveSymbol == True:
                    #向右攻击，向左走，后退攻击
                    pass
                else:
                    self.normalAttack.execute()
                    
                    #向右攻击，面向右，正常攻击
                    pass
                
            else:
                #向左攻击
                if self.faceSide == "r":
                    #向左攻击，面向右，回身攻击
                    self.normalAttackToLeft.execute()
                    self.faceSide = "l"
                    pass
                elif self.rightMoveSymbol:
                    #向左攻击，向右走，后退攻击
                    pass
                else:
                    self.normalAttackToLeft.execute()
                    #向左攻击，面向左，正常攻击
                    pass
                
        elif "d" in self.inputList:
            #防御
            self.eventList.append("d")
            if self.faceSide == "r":
                #向右防御
                pass
            else:
                 #向左防御
                 pass

        elif "r" in self.inputList:
            #向右走
            if self.faceSide == "r":
                #向右走，面向右
                if self.shiftSymbol == True:
                    #向右走，面向右，向前冲刺右！
                    pass
                else:
                    #向右走，面向右，慢走
                    self.walking.execute()
                    
                    pass
            else:
                #向右走，鼠标在左
                if self.faceSide == "r":
                    self.faceSide = "l"
                    self.loc[0] -= 25
                if self.shiftSymbol == True:
                    #向右走，面向左，向后闪身右！
                    pass
                else:
                    #向右走，面向左，后退
                    pass

        elif "l" in self.inputList:
            #向左走
            if self.faceSide == "r":
                #向左走，面向右
                if self.shiftSymbol == True:
                    #向左走，面向右，向后闪身左！
                    pass
                else:
                    #向左走，面向右，后退
                    pass
            else:
                #向左走，鼠标在左
                if self.shiftSymbol == True:
                    #向左走，面向左，向前冲刺左！
                    pass
                else:
                    #向左走，面向左，慢走
                    self.walkingToLeft.execute()


        elif "keyUP" in self.inputList:
            if self.rightMoveSymbol == True:
                #向右走
                if self.faceSide == "r":
                    #向右走，面向右
                    if self.shiftSymbol == True:
                        #向右走，面向右，奔跑
                        pass
                    else:
                        #向右走，面向右，慢走
                        self.walking.execute()
                else:
                    #向右走，面向左，后退
                    self.faceSide = "l"
                    pass
            elif self.leftMoveSymbol == True:
                #向左走
                if self.faceSide == "r":
                    #向左走，面向右，后退
                    pass
                else:
                    #向左走，面向左
                    if self.shiftSymbol == True:
                        #向左走，面向左，奔跑
                        pass
                    else:
                        #向左走，面向左，慢走
                        self.walkingToLeft.execute()

            else:
                #站立
                self.loc[0] += self.currentAction.movingSteps[-1]
                if self.faceSide == "r":
                    self.standing.execute()
                else:
                    self.standingToLeft.execute()

        elif "shift" in self.inputList:
            if self.rightMoveSymbol == True:
                #向右奔跑
                pass
            elif self.leftMoveSymbol == True:
                #向左奔跑
                pass
        
        elif "shiftUP" in self.inputList:
            if self.rightMoveSymbol == True:
                #向右走慢走
                self.walking.execute()

            elif self.leftMoveSymbol == True:
                #向左走慢走
               self.walkingToLeft.execute()




class NormalAttack:
    def __init__(self, master):
        self.master = master

        self.picSize = (348,200)
        self.picLoc = (0,0)
        self.picLocRectify = (112,200)
        
        self.frames = [
            pygame.image.load("Source/character/Azure/act_Attack/1.png"),
            pygame.image.load("Source/character/Azure/act_Attack/2.png"),
            pygame.image.load("Source/character/Azure/act_Attack/3.png"),
            pygame.image.load("Source/character/Azure/act_Attack/4.png"),
            pygame.image.load("Source/character/Azure/act_Attack/5.png"),
            pygame.image.load("Source/character/Azure/act_Attack/6.png"),
            pygame.image.load("Source/character/Azure/act_Attack/7.png"),
        ]
        self.act0_FrameList = [1,2,3]
        self.act0_movingSteps = [0,0,38,100]
        self.act0_timeStampList = [5,10,20]
        self.act0_picLocRectify = (112,200)

        self.act1_FrameList = [4,5,6]
        self.act1_movingSteps = [0,168,0,0]
        self.act1_timeStampList = [5,10,20]
        self.act1_picLocRectify = (150,200)

        self.currentFrame = 0

        self.frameList = self.act0_FrameList
        self.movingSteps = self.act0_movingSteps
        self.timeStampList = self.act0_timeStampList

        self.vision = self.frames[self.frameList[0]]

        self.coerciveActingFrame = 10

    def locatedPicLoc(self,rectify):
        self.picLoc = (self.master.loc[0] - rectify[0] , self.master.loc[1] - rectify[1])

    def init(self):
        self.currentFrame = 0
        self.vision = self.frames[self.frameList[0]]

    def changeFaceSides(self):
        self.frames = [pygame.transform.flip(image,True,False) for image in self.frames]

        self.act0_movingSteps = [0,0,-38,-100]
        self.act0_picLocRectify = (self.picSize[0] - self.act0_picLocRectify[0],self.act0_picLocRectify[1])

        self.act1_movingSteps = [0,-168,0,0]
        self.act1_picLocRectify = (self.picSize[0] - self.act1_picLocRectify[0],self.act1_picLocRectify[1])



    def execute(self):
        self.master.coerciveActingSymbol = True
        self.master.currentAction = self
        if self.master.frontFoot == 'l':
            self.frameList = self.act0_FrameList
            self.movingSteps = self.act0_movingSteps
            self.timeStampList = self.act0_timeStampList
            self.master.frontFoot = 'r'
            self.locatedPicLoc(self.act0_picLocRectify)
        else:
            self.frameList = self.act1_FrameList
            self.movingSteps = self.act1_movingSteps
            self.timeStampList = self.act1_timeStampList
            self.master.frontFoot = 'l'
            self.locatedPicLoc(self.act1_picLocRectify)
        self.init()
        
    def act(self):
        self.master.timer += 1

        if self.master.timer > self.coerciveActingFrame:
            self.master.coerciveActingSymbol = False

        if self.master.timer >= self.timeStampList[-1]:
            self.master.loc[0] += self.movingSteps[-1]
            
            self.master.resetAction()

        elif self.master.timer >= self.timeStampList[self.currentFrame]:
            self.currentFrame += 1

            self.master.loc[0] += self.movingSteps[self.currentFrame]

            self.vision = self.frames[self.frameList[self.currentFrame]]


class Walking:
    def __init__(self, master):
        self.master = master

        self.picSize = (112,200)
        self.picLoc = (0,0)
        self.picLocRectify = (22,200)

        
        self.frames = [
            pygame.image.load("Source/character/Azure/act_Walking/1.png"),
            pygame.image.load("Source/character/Azure/act_Walking/2.png"),
            pygame.image.load("Source/character/Azure/act_Walking/3.png"),
            pygame.image.load("Source/character/Azure/act_Walking/4.png"),
        ]

        self.act0_FrameList = [0,1,2,3]
        self.act0_timeStampList = [10,20,30,40]
        #self.act0_timeStampList = [30,60,90,120]
        self.act0_movingSteps = [0,24,72,0,0,24]
        self.act0_picLocRectify = [(22,200),(14,200),(64,200),(36,200)]
        self.cameraMovingSpeed = 3.1

        self.currentFrame = 0

        self.frameList = self.act0_FrameList
        self.timeStampList = self.act0_timeStampList
        self.movingSteps = self.act0_movingSteps
        self.picLocRectify = self.act0_picLocRectify

        self.vision = self.frames[self.frameList[0]]

        self.coerciveActingFrame = 0


    def locatedPicLoc(self,rectify):
        self.picLoc = (self.master.loc[0] - rectify[0] , self.master.loc[1] - rectify[1])

    def init(self):
        self.vision = self.frames[self.frameList[0]]
        self.currentFrame = 0
        pass

    def changeFaceSides(self):
        self.frames = [pygame.transform.flip(image,True,False) for image in self.frames]

        self.act0_picLocRectify = [(self.picSize[0] - n[0],n[1]) for n in self.act0_picLocRectify]
        self.act0_movingSteps = [0,-24,-72,0,0,-24]

        self.frameList = self.act0_FrameList
        self.timeStampList = self.act0_timeStampList
        self.movingSteps = self.act0_movingSteps
        self.picLocRectify = self.act0_picLocRectify
        self.cameraMovingSpeed *= -1

        return self

        
    def execute(self):
        self.master.currentAction = self
        self.master.frontFoot = 'l'
        self.locatedPicLoc(self.picLocRectify[0])
        self.init()

    def act(self):
        self.master.timer += 1
        GV.camera.updateCameraLoc((self.cameraMovingSpeed,0))
        
        if self.master.timer >= self.timeStampList[-1]:
            self.master.timer = 0
            self.master.loc[0] += self.movingSteps[-1]
            self.locatedPicLoc(self.picLocRectify[-1])
            self.init()

        elif self.master.timer >= self.timeStampList[self.currentFrame]:

            self.currentFrame += 1

            self.vision = self.frames[self.frameList[self.currentFrame]]

            self.master.loc[0] += self.movingSteps[self.currentFrame]

            self.locatedPicLoc(self.picLocRectify[self.currentFrame])
            


class Standing:
    def __init__(self, master):
        self.master = master

        self.picSize = (70,200)
        self.picLoc = (0,0)
        self.picLocRectify = (64,200)
        
        self.frames = [
            pygame.image.load("Source/character/Azure/act_Standing/1.png"),
            pygame.image.load("Source/character/Azure/act_Standing/2.png")
        ]

        self.act0_FrameList = [0,1]
        self.act0_timeStampList = [70,140]
        self.act0_picLocRectify = (64,200)

        self.currentFrame = 0

        self.frameList = self.act0_FrameList
        self.timeStampList = self.act0_timeStampList
        self.movingSteps = [0]

        self.vision = self.frames[self.frameList[0]]

        self.coerciveActingFrame = 0

    def locatedPicLoc(self,rectify):
        self.picLoc = (self.master.loc[0] - rectify[0] , self.master.loc[1] - rectify[1])

    def init(self):
        self.vision = self.frames[self.frameList[0]]
        self.currentFrame = 0
        pass

    def changeFaceSides(self):
        self.frames = [pygame.transform.flip(image,True,False) for image in self.frames]

        self.act0_picLocRectify = (self.picSize[0] - self.act0_picLocRectify[0],self.act0_picLocRectify[1])
        self.picLocRectify = self.act0_picLocRectify
        
    def execute(self):
        self.master.currentAction = self
        self.master.frontFoot = 'l'
        self.locatedPicLoc(self.picLocRectify)
        self.init()

    def act(self):
        self.master.timer += 1

        if self.master.timer >= self.timeStampList[-1]:
            self.master.timer = 0
            self.init()
        elif self.master.timer >= self.timeStampList[self.currentFrame]:
            self.currentFrame += 1
            self.vision = self.frames[self.frameList[self.currentFrame]]