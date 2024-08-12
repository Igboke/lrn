#Timing Detector
#Write a decorator that times how long a function takes to execute and print the duration

import time
def timer_(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end=time.time()
        interval=end-start
        return interval
    return wrapper

@timer_
def adder (a,b,c):
    return a + b + c