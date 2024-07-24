def my_decorator(func):
    def wrapper():
        print('$$$$$$$$$$$')
        func()
        print('@@@@@@@@@@@@')
    return wrapper


@my_decorator
def hello():
    print('hello')
    
hello()

import time
import numpy as np

def timer(func):
    def wrapper():
        start = time.time()
        func()
        stop = (time.time()-start)
        print(f'it took {stop} seconds')
    return wrapper

@timer
def listx():
    time.sleep(3)
    a = list(np.arange(1,100000))
    print(a)

@timer
def list1():
    b = list(np.arange(1,1000))
listx()