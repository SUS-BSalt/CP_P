import globalValue as GV
import pygame

class bottomUI:
    def __init__(self,size,loc,ACTModule,book):
        self.master = ACTModule
        self.workingSituation = True

        self.backgroundPic = pygame.image.load("Source\\UI\\ACTbottomUI.png")

        self.sleepSwitch = False
        self.sleepTime = 50

        self.printSpeed = GV.settings.printSpeed*GV.settings.logicLoopFps
        self.timer = 0

        self.size = size
        self.loc = loc
        
        self.book = book

        self.currentSentence = self.book.readline().strip()
        self.currentWord = 0
        self.textEffectSwitch = False

        self.textSize = 40
        """文字大小"""
        self.textLineGap = GV.textSettings.textLineGap
        """#行间距"""
        self.margins = GV.textSettings.margins
        """#页边距"""
        self.textLineCutLineLoc = self.size[0] - self.margins*2
        """#换行的边线坐标"""
        self.textLineCutLineLoc = self.size[0] - self.margins*2
        """换行的位置"""
        GV.UIfont_03 = pygame.font.Font(GV.textSettings.charType,self.textSize)
        """字体"""


        self.currentWordLoc = [self.loc[0] + self.margins, self.loc[1] +  self.margins]

        self.label = 0

        self.wordsList = []

    def act(self):
        if self.workingSituation == True :
                #自身活跃
                if self.sleepSwitch == True :
                    #（睡眠的方法）自身活跃，有睡眠
                    self.timer += 1
                    if self.timer >= self.sleepTime:
                        self.sleepSwitch = False
                        self.timer = 0
                    #（睡眠的方法）
                else:
                    #（常规输出的方法）自身活跃，无睡眠
                    self.timer += 1
                    if self.timer >= self.printSpeed:
                        self.reader()
                        self.timer = 0
                    #（常规输出的方法）
    def draw(self):
        GV.camera.cameraShot.blit(self.backgroundPic,(0,360))
        for word in self.wordsList:
            GV.camera.cameraShot.blit(word.vision,(word.loc[0],word.loc[1]+360))
        pass
    def animate(self):
        pass

    def printer(self, msg, label, color = (120,120,120)):
        newWord = singleWord(self.currentWordLoc,msg,label,color)
        newWord.render(color)
        self.wordsList.append(newWord)

        #决定下一个字符位置
        self.currentWordLoc[0] += newWord.size[0]
        if self.currentWordLoc[0] >= self.textLineCutLineLoc:
            self.wrapText()

    def wrapText(self):
        self.currentWordLoc[0] = self.loc[0] + self.margins
        self.currentWordLoc[1] += self.textLineGap + self.textSize
        #换行的判断及执行

    def textEffectMatcher(self):
        self.textEffect = ""
        while self.textEffectSwitch:
            self.currentWord += 1
            if self.currentSentence[self.currentWord] == "》":
                self.currentWord += 1
                self.textEffectSwitch = False
                break
            self.textEffect += self.currentSentence[self.currentWord]
        #将文本特殊样式读取进来

        match self.textEffect:
            #停顿
            case _ if self.textEffect[:4] == 'wait':
                self.sleepSwitch = True
                self.sleepTime = float(self.textEffect[4:])*GV.settings.logicLoopFps
            #换行
            case '/n':
                self.wrapText()
            case _ if self.textEffect[:3] == "lab":
                self.label = int(self.textEffect[3:])
            case "yee":
                self.workingSituation = False
            case _ :
                print("未知效果"+self.textEffect)

    def reader(self):
        try:
            match self.currentSentence[self.currentWord]:
                #匹配特殊字符，否则直接输出
                case "$":
                    #输出下一个字符
                    self.currentWord += 1
                    self.printer(self.currentSentence[self.currentWord], self.label)
                    self.currentWord += 1
                case "《":
                    self.textEffectSwitch = True
                    self.textEffectMatcher()
                case _:
                    self.printer(self.currentSentence[self.currentWord], self.label)
                    self.currentWord += 1
        except:
            self.currentSentence = self.book.readline().strip()
            self.currentWord = 0
            self.wrapText()

class singleWord:
    def __init__(self,loc,char,label = 0, color = (120,120,120)):
        self.activeSituation = True
        self.loc = list(loc)
        self.char = char
        self.label = label
        self.defaultColor = color
        self.timer = 0
        self.frameList = []

    def act(self):
        pass
    def draw(self):
        pass
    def animate(self):
        pass
    def render(self,color):
        self.vision = GV.UIfont_03.render(self.char,True,color)
        self.size = self.vision.get_size()

