import pygame

class LoopPlay:
    '''循环播放'''
    def __init__(self, obj,frameList: list = [], timeStampList: list = []):
        """frameList记录这段动画会使用obj的哪些frame, timeStampList表示这段动画每一帧结束的时间点"""
        self.obj = obj
        self.frameList = frameList
        self.timeStampList = timeStampList
        
        self.timer = 0
        self.currentFrame = 0
        

    def init(self):
        self.timer = 0
        self.currentFrame = 0
        self.obj.vision = self.obj.frameList[self.frameList[0]]

    def act(self):
        self.timer += 1
        #timer每动画帧自加一

        if self.timer == self.timeStampList[-1]:
            self.init()
        #如果timer等于动画周期，重置自身

        elif self.timer == self.timeStampList[self.currentFrame]:
            self.currentFrame += 1
            self.obj.vision = self.obj.frameList[self.frameList[self.currentFrame]]
        #如果timer等于当前帧对应的时间戳，则将当前帧记号加一,更新obj的vision
        

class PlayOnce:
    '''循环播放'''
    def __init__(self, obj,frameList: list = [], timeStampList: list = []):
        """frameList记录这段动画会使用obj的哪些frame, timeStampList表示这段动画每一帧结束的时间点"""
        self.obj = obj
        self.frameList = frameList
        self.timeStampList = timeStampList
        self.activeSituation = False
        
        self.timer = 0
        self.currentFrame = 0
        

    def init(self):
        self.timer = 0
        self.currentFrame = 0
        self.obj.vision = self.obj.frameList[self.frameList[0]]
        self.activeSituation = False

    def act(self):
        self.timer += 1
        #timer每动画帧自加一

        if self.timer >= self.timeStampList[-1]:
            self.init()
        #如果timer等于动画周期，重置自身

        if self.timer >= self.timeStampList[self.currentFrame]:
            self.currentFrame += 1
            self.obj.vision = self.obj.frameList[self.frameList[self.currentFrame]]
        #如果timer等于当前帧对应的时间戳，则将当前帧记号加一,更新obj的vision


class SwitchFrame:
    """切换obj的vision到指定frame"""
    def __init__(self, obj, frame):
        self.obj = obj
        self.frame = frame

    def init(self):
        pass

    def act(self):
        self.obj.vision = self.obj.frameList[self.frame]

class CoverAMask:
    """给当前vision盖上一个遮罩(obj自带)"""
    def __init__(self, obj, maskID):
        self.obj = obj
        self.mask = obj.frameList[maskID]

    def init(self):
        pass

    def act(self):
        self.obj.vision = self.obj.vision.copy().blit(self.mask)

class ChangeAlpha:
    """改变当前vision透明度"""
    def __init__(self, obj):
        self.obj = obj
        
        pass

        



    




