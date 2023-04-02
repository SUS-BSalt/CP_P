import time
import random
pre = 0 
beg = 0

while True:
    pre = beg
    beg = time.perf_counter()
    time.sleep(0.2)
    end = time.perf_counter()
    differ = end - beg
    print(differ)

    """if differ < 1:
        print(differ,beg - pre)
        time.sleep(1 - differ)
    else:
        print(differ,beg - pre)
        print("lowFPS!")"""
    
    