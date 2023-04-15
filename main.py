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


        self.fps_Rectify_Frequency = 50
        """每多少帧修正一次"""
        self.fps_Rectify_TimeCell = self.fps_Rectify_Frequency/GV.settings.logicLoopFps
        """每两次修正之间的理想间隔时长"""
        self.fps_Span = 1/GV.settings.logicLoopFps
        """每帧持续时长"""
        self.fps_Span_Rectify = self.fps_Span
        """每帧持续时长的修正，维持fps用"""
        self.fps_Span_Rectify_var = self.fps_Rectify_TimeCell /self.fps_Rectify_Frequency *0.009
        """每次修正时的修正量"""
        
        self.fps_Rectify_Timer = 0
        """用于修正帧率的计时器"""
        self.beg_FrameTimer = 0
        """每帧执行开始时的计时器"""
        self.end_FrameTimer = 0
        """每帧执行结束时的计时器"""
        self.differ_FrameTimer = 0
        """记录每帧实际运行的时长的计时器"""
        self.fps_Span_Rectify_Timer = 0
        """用于修正帧率用的计时器，记录上一次执行修正时的时间"""
        self.fps_Span_Rectify_TimeGap = 0
        """用于修正帧率用的计时器，记录两次修正之间的时间差"""



    
    def logicLoop(self):
        """#逻辑循环，包括控制逻辑与动画"""
        fpsRectifyFrequency = 50
        """每20帧修正一次FPS"""
        fpsRectifyTime = fpsRectifyFrequency/GV.settings.logicLoopFps
        while GV.sysSymbol.get("gameRun"):
            #循环本体
            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓维持FPS的第一块代码↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            self.beg_FrameTimer = time.perf_counter()
            self.fps_Rectify()
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑维持FPS的第一块代码↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓游戏逻辑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            GV.controller()
            #处理输入信号
            for module in GV.moduleList:
                if module.activeSituation == True:
                    module.act()
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑游戏逻辑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓维持FPS的第二块代码↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            self.end_FrameTimer = time.perf_counter()
            self.differ_FrameTimer = self.end_FrameTimer - self.beg_FrameTimer
            if self.differ_FrameTimer > self.fps_Span_Rectify:
                print("Low!")
                continue
            time.sleep(self.fps_Span_Rectify - self.differ_FrameTimer)
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑维持FPS的第二块代码↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

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

    def fps_Rectify(self):
        self.fps_Rectify_Timer += 1
        if  self.fps_Rectify_Timer == self.fps_Rectify_Frequency:
            self.fps_Span_Rectify_TimeGap = self.beg_FrameTimer - self.fps_Span_Rectify_Timer
            if   self.fps_Span_Rectify_TimeGap > (self.fps_Rectify_TimeCell*1.1):
                 self.fps_Span_Rectify -= (self.fps_Span_Rectify_var*10)
                 print(self.fps_Span_Rectify)

            elif self.fps_Span_Rectify_TimeGap > (self.fps_Rectify_TimeCell*1.01):
                 self.fps_Span_Rectify -= self.fps_Span_Rectify_var
                 print(self.fps_Span_Rectify)
    
            elif self.fps_Span_Rectify_TimeGap < (self.fps_Rectify_TimeCell*0.9):
                 self.fps_Span_Rectify += (self.fps_Span_Rectify_var*10)
                 print(self.fps_Span_Rectify)

            elif self.fps_Span_Rectify_TimeGap <  (self.fps_Rectify_TimeCell*0.99):
                 self.fps_Span_Rectify += self.fps_Span_Rectify_var
                 print(self.fps_Span_Rectify)
            #print(tiemGap)
            print(round(1/(self.fps_Span_Rectify_TimeGap)*self.fps_Rectify_Frequency),"FPS")
            #print(pygame.time.get_ticks())
            self.fps_Span_Rectify_Timer = self.beg_FrameTimer
            self.fps_Rectify_Timer = 0


    def No_Threading_Loop(self):
        "Fuck threading"
        while GV.sysSymbol.get("gameRun"):
            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓维持FPS的第一块代码↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            self.beg_FrameTimer = time.perf_counter()
            self.fps_Rectify()
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑维持FPS的第一块代码↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            GV.controller()
            for module in GV.moduleList:
                module.act()
                module.animate()
                module.draw()
            GV.screen.blit(pygame.transform.scale(GV.camera.cameraShot,GV.settings.windowsize),GV.camera.cameraLocRectify)
            pygame.display.update()
            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓维持FPS的第二块代码↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            self.end_FrameTimer = time.perf_counter()
            self.differ_FrameTimer = self.end_FrameTimer - self.beg_FrameTimer
            if self.differ_FrameTimer > self.fps_Span_Rectify:
                print("Low!")
                continue
            time.sleep(self.fps_Span_Rectify - self.differ_FrameTimer)
            #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑维持FPS的第二块代码↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑



    def runningStart(self):
        import Levels.OpeningMenu
        self.thread_drawLoop = threading.Thread(target = self.drawLoop)
        self.thread_drawLoop.start()
        
        self.thread_animateLoop = threading.Thread(target = self.animateLoop)
        self.thread_animateLoop.start()
        
        self.logicLoop()

        

cp_p = MainGame()
cp_p.runningStart()
