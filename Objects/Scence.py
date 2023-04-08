import pygame
import globalValue as GV


class Scence:
    def __init__(self):
        self.objList = []
        self.tempCameraLocContainer = (0,0)

    def init(self,cameraLoc):
        for obj in self.objList:
            obj.init(cameraLoc)

    def draw(self):
        for obj in self.objList:
            obj.draw()
    def animate(self):
        for obj in self.objList:
            obj.animate()
    def update(self,cameraLoc):
        #画面出现跳闪的一个原因便是：只有部分的obj完成更新时，camera的位置改变了，导致之后的obj根据新的loc进行更新
        # 故必须用一个新容器来把传入的loc固定住，因为python语言的特性，传入给函数的值永远是其指针，不能自行控制，真不方便！
        
        #顺带一提，另一个原因是画面没更新完毕时就开始了新的绘制，这个问题可以简单的把两个任务强制拉到一个线程里进行来解决
        #但是我希望能找到一个优雅的方法处理它,2023.3.22
        if self.tempCameraLocContainer != cameraLoc:
            self.tempCameraLocContainer = tuple(cameraLoc)
            for obj in self.objList:
                obj.update(self.tempCameraLocContainer)
        

class Plane:
    def __init__(self,loc,size,vision,movingSpeed):
        self.loc = loc
        self.org_loc = tuple(loc)
        self.size = size
        self.vision = vision
        self.movingSpeed = movingSpeed

    def init(self,cameraLoc):
        pass

    def draw(self):
        GV.camera.draw(self.vision,self.loc)
        
    def animate(self):
        pass
    def update(self,cameraLoc):
        self.loc[0] = (cameraLoc[0]*(1-self.movingSpeed)) + self.org_loc[0]


class PerspectiveObject:
    def __init__(self,loc,size,appearLoc,disappearLoc,flag,vision,movingspeed):
        self.loc = loc
        self.org_loc = tuple(loc)
        self.size = size
        self.movingSpeed = movingspeed

        self.appearLoc = appearLoc
        self.disappearLoc = disappearLoc
        self.theCameraMovingDistanceThenTheObjAppearOnScreen = self.disappearLoc[0] - self.appearLoc[0]
        
        self.scaleIndex = 1
        self.vision = vision
        self.org_vision = vision
        self.blitLoc = [0,0]

        if flag == "right":
            self.blitLoc = self.loc
            self.update = self.updateMethodForRight
            self.init = self.initRightSide
        elif flag == "left":
            self.blitLoc = (self.loc[0] - self.size[0],self.loc[1] - self.size[1])
            self.update = self.updateMethodForLeft
            self.init = self.initLeftSide
        self.init(GV.camera.loc)

    def init(self,cameraLoc):
        pass
    def initRightSide(self,cameraLoc):
        if cameraLoc[0] < self.appearLoc[0]:
            self.vision = pygame.transform.scale(self.org_vision, (0,self.size[1]))
        elif cameraLoc[0] > self.disappearLoc[0]:
            self.vision = self.org_vision
        else:
            self.updateMethodForRight(cameraLoc)
    def initLeftSide(self,cameraLoc):
        if cameraLoc[0] < self.appearLoc[0]:
            self.vision = self.org_vision 
        elif cameraLoc[0] > self.disappearLoc[0]:
            self.vision = pygame.transform.scale(self.org_vision, (0,self.size[1]))
        else:
            self.updateMethodForLeft(cameraLoc)
    
    
    def draw(self):
        GV.camera.draw(self.vision,self.blitLoc)
    
    def animate(self):
        pass
    
    
    def update(self,cameraLoc):
        pass
    
    def updateMethodForRight(self,cameraLoc):
        self.loc[0] = cameraLoc[0]*(1-self.movingSpeed) + self.org_loc[0]
        if cameraLoc[0] < self.appearLoc[0] or cameraLoc[0] > self.disappearLoc[0]:
            return
        self.scaleIndex=(cameraLoc[0]-self.appearLoc[0])/self.theCameraMovingDistanceThenTheObjAppearOnScreen
        self.vision = pygame.transform.scale(self.org_vision, (self.size[0]*self.scaleIndex,self.size[1]))
        

    def updateMethodForLeft(self,cameraLoc):
        self.loc[0] = cameraLoc[0]*(1-self.movingSpeed) + self.org_loc[0]
        if cameraLoc[0] < self.appearLoc[0] or cameraLoc[0] > self.disappearLoc[0]:
            return
        self.scaleIndex=(self.disappearLoc[0] - cameraLoc[0])/self.theCameraMovingDistanceThenTheObjAppearOnScreen
        self.vision = pygame.transform.scale(self.org_vision, (self.size[0]*self.scaleIndex,self.size[1]))
        self.blitLoc = (self.loc[0] - self.size[0]*self.scaleIndex,self.loc[1])
