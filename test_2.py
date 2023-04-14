print(0.1+0.3)


def modifyerF(func):
    print(1)
    func()
    print(1)
    return func
"""    def modifyded():
        print("1")
        
        print("2")
    return modifyded"""

@modifyerF
def sss():
    print("3")

sss()