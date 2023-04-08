class SDd:
    def __init__(self):
        self.a = 1

a1 = SDd()
b1 = a1
a1.a = 2
print(b1.a)
