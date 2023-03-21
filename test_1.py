class PerspectiveObject:
    def __init__(self,loc,appearLoc,disappearLoc,flag):
        self.loc = loc
        self.appearLoc = appearLoc
        self.disappearLoc = disappearLoc
        if flag == "right":
            self.update = self.updateMethodForRight
        elif flag == "left":
            self.update = self.updateMethodForLeft
    
    def update(self):
        pass
    def updateMethodForRight(self):
        print("right")
        pass
    def updateMethodForLeft(self):
        print("left")
        pass

ssisissi = PerspectiveObject((1,1),(1,1),(1,1),"right")
ssisissi.update()