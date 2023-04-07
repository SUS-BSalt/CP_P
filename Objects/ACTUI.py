import globalValue as GV
import pygame

class bottomUI:
    def __init__(self,size,loc,ACTModule,book):
        self.master = ACTModule
        self.workingSituation = True
        self.rollingTextSymbol = False
        self.rollingTextSpeed = 10

        self.backgroundPic = pygame.image.load("Source\\UI\\ACTbottomUI.png")
        self.backgroundMask_0 = pygame.image.load("Source\\UI\\mask_0.png")

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

        self.wordDeadline = 10
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
        if self.rollingTextSymbol == True:
            self.changeWordYLoc(self.rollingTextSpeed*-1)
            #print(self.wordsList[-1].loc[1])
            self.deleteWord(self.wordDeadline)
            if self.wordsList[-1].loc[1] < 77:
                self.rollingTextSymbol = False
                self.deleteWord(self.wordDeadline)
    
    def draw(self):
        GV.camera.draw_UI(self.backgroundPic,(0,360))
        for word in self.wordsList:
            GV.camera.draw_UI(word.vision,(word.loc[0],word.loc[1]+360))
        GV.camera.draw_UI(self.backgroundMask_0,(0,360))

    def animate(self):
        for word in self.wordsList:
            word.animate()
        pass

    def printer(self, msg, color = (255,255,255), label = 0):
        newWord = singleWord(self.currentWordLoc,msg,color,label)
        newWord.render(color)
        self.wordsList.append(newWord)

        #决定下一个字符位置
        self.currentWordLoc[0] += newWord.size[0]
        if self.currentWordLoc[0] >= self.textLineCutLineLoc:
            self.wrapText()

    def wrapText(self):
        self.currentWordLoc[0] = self.loc[0] + self.margins
        self.currentWordLoc[1] += self.textLineGap + self.textSize
        self.deleteWord(self.wordDeadline)
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
            case _ if self.textEffect[:4] == "roll":
                self.rollingTextSymbol = True
                self.rollingTextSpeed = int(self.textEffect[4:])
            case "yee":
                self.workingSituation = False
                #暂停读取文字
            case _ :
                print("未知效果"+self.textEffect)

    def changeWordYLoc(self,rectify):
        for word in self.wordsList:
            word.loc[1] += rectify
        self.currentWordLoc[1] += rectify
    
    def deleteWord(self,deadline):
        for word in self.wordsList:
            if word.loc[1] < deadline:
                self.wordsList.remove(word)
        #print([word.loc[1] for word in self.wordsList])


    def reader(self):
        try:
            match self.currentSentence[self.currentWord]:
                #匹配特殊字符，否则直接输出
                case "$":
                    #输出下一个字符
                    self.currentWord += 1
                    self.printer(self.currentSentence[self.currentWord], label = self.label)
                    self.currentWord += 1
                case "《":
                    self.textEffectSwitch = True
                    self.textEffectMatcher()
                case _:
                    self.printer(self.currentSentence[self.currentWord], label = self.label)
                    self.currentWord += 1
        except:
            self.currentSentence = self.book.readline().strip()
            self.currentWord = 0
            self.wrapText()
    


class singleWord:
    def __init__(self,loc,char, color, label = 0):
        self.activeSituation = True

        self.colorGradientSym = True
        self.colorGradientSpeed = 50
        self.color_default = (80,80,80)
        self.color_current = color
        self.color_org = self.color_current
        self.color_fin = self.color_default

        self.loc = list(loc)
        self.char = char
        self.label = label
        


        
        self.timer = 0
        self.frameList = []

    def act(self):
        pass
    def draw(self):
        pass
    def animate(self):
        if self.colorGradientSym == True:
            self.timer += 1
            self.color_current = self.colorGradientOnTime(self.color_org,self.color_fin)

            if abs(self.color_current[0] - self.color_fin[0]) <= 5 and \
                abs(self.color_current[1] - self.color_fin[1]) <= 5 and \
                abs(self.color_current[2] - self.color_fin[2]) <= 5:
                self.color_current = self.color_fin
                self.colorGradientSym = False
                self.timer = 0

            self.render(self.color_current)
            #print("yee",self.color_current)


    def render(self,color):
        self.vision = GV.UIfont_03.render(self.char,True,color)
        self.size = self.vision.get_size()
    def colorGradientOnTime(self,color_org,color_fin):
        r = int((color_fin[0] - color_org[0]) * (self.timer/self.colorGradientSpeed) + color_org[0])
        g = int((color_fin[1] - color_org[1]) * (self.timer/self.colorGradientSpeed) + color_org[1])
        b = int((color_fin[2] - color_org[2]) * (self.timer/self.colorGradientSpeed) + color_org[2])
        return(r,g,b)
