import pygame
pygame.init()
import threading
import Objects.SysObjects as SysObjects
import Objects.visionObj as visionObj
import globalValue as GV
import sys
import time

#我将注释写在其描述对象的下一行或，描述代码块的注释在其起始条件语句同缩进的代码块尾，也就是说每行注释描述的都是它上面的代码



class MainGame:
    def __init__(self):

        GV.sysSymbol.set("gameRun",True)
        self.logicLoop_Pre_FrameTimeSnape = 0
        self.logicLoop_Beg_FrameTimeSnape = 0
        self.logicLoop_End_FrameTimeSnape = 0
        self.Rectify_frameGapTime = 1 / GV.settings.logicLoopFps
        self.timer = 0



    
    def logicLoop(self):
        """#逻辑循环，包括控制逻辑与动画"""
        fpsRectifyFrequency = 50
        """每20帧修正一次FPS"""
        fpsRectifyTime = fpsRectifyFrequency/GV.settings.logicLoopFps
        while GV.sysSymbol.get("gameRun"):
            #循环本体
            #self.logicLoopclock.tick(GV.settings.logicLoopFps)
            #维持FPS频率的第一块代码
            self.logicLoop_Beg_FrameTimeSnape = time.perf_counter()
            self.timer += 1
            
            if self.timer == fpsRectifyFrequency:
                tiemGap = self.logicLoop_Beg_FrameTimeSnape - self.logicLoop_Pre_FrameTimeSnape
                if tiemGap > fpsRectifyTime*1.1:
                    self.Rectify_frameGapTime -= 0.001
                elif tiemGap > fpsRectifyTime*1.01:
                    self.Rectify_frameGapTime -= 0.00001
                elif tiemGap < fpsRectifyTime*0.9:
                    self.Rectify_frameGapTime += 0.001
                elif tiemGap < fpsRectifyTime*0.99:
                    self.Rectify_frameGapTime += 0.00001
                #print(tiemGap)
                #print(round(1/(tiemGap)*fpsRectifyFrequency),"FPS")
                self.logicLoop_Pre_FrameTimeSnape = self.logicLoop_Beg_FrameTimeSnape
                self.timer = 0
            #维持FPS频率的第一块代码
                
            #游戏逻辑
            GV.controller()
            #处理输入信号
            
            for module in GV.moduleList:
                if module.activeSituation == True:
                    module.act()
            #游戏逻辑

            #维持FPS频率的第二块代码
            self.logicLoop_End_FrameTimeSnape = time.perf_counter()
            differ = self.logicLoop_End_FrameTimeSnape - self.logicLoop_Beg_FrameTimeSnape
            if differ > self.Rectify_frameGapTime:
                continue
            time.sleep(self.Rectify_frameGapTime - differ)
            #维持FPS频率的第二块代码

        sys.exit()


    def drawLoop(self):
        """#画面循环，基本只负责绘制可见对象"""
        """还有更新场景2023.4.7"""
        self.drawLoopclock = pygame.time.Clock()

        while GV.sysSymbol.get("gameRun"):
            #0循环本体
            self.drawLoopclock.tick(GV.settings.drawLoopFps)
            #保持循环的fps
            #GV.playGround.fill((255,255,255))
            #刷新屏幕，如果有了全屏性的playGround就不用了
            
            for module in GV.moduleList:
                module.draw()
            #GV.camera.cameraShot_UI.set_alpha(255)
            #GV.camera.cameraShot.blit(GV.camera.cameraShot_UI,(0,0))
            GV.screen.blit(pygame.transform.scale(GV.camera.cameraShot,GV.settings.windowsize),GV.camera.cameraLocRectify)
            #摄像机相关

            pygame.display.update()
        
        sys.exit()

    def cameraLoop(self):
        pass
        "负责"


    def animateLoop(self):
        self.animateLoopclock = pygame.time.Clock()
        self.timer = 0
        while GV.sysSymbol.get("gameRun"):
            self.animateLoopclock.tick(GV.settings.animateLoopFps)

            #self.camera.act()@To 根据主角位置修正camera位置

            for module in GV.moduleList:
                module.animate()
            
            #print(' ')
            """self.timer += 1
            if self.timer >= 50:
                print(self.logicLoopclock.get_fps(),self.drawLoopclock.get_fps(),self.animateLoopclock.get_fps())
                self.timer = 0"""
        sys.exit()



    def runningStart(self):
        self.thread_drawLoop = threading.Thread(target = self.drawLoop)
        self.thread_drawLoop.start()
        
        self.thread_animateLoop = threading.Thread(target = self.animateLoop)
        self.thread_animateLoop.start()
        
        self.logicLoop()

        

cp_p = MainGame()

import Levels.OpeningMenu

cp_p.runningStart()
