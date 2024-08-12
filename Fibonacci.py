''' the timer_decorator has been created to check the speed of the fumction's execution. feel free to decorate it  '''

import time
def timer_(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end=time.time()
        interval=end-start
        return interval
    return wrapper

#fibonacci generator
def fibonacci(no):
    #initialize the list
    lst =[0,1]
    if no == 0:
        #self explanatory, and empty list
        return []
    elif no == 1:
        #0 is the first number in the fibonacci sequence
        return [0]
    else:
        #initialize counter to 2 since there are 2 numbers control while loop
        count = 2
        #the list starts with [0,1], a situation where the count equals the 'no' of digits' that we want, the while loop should end
        while count < no:
            count += 1
            #sum of the last 2 numbers on the list and append them at the end
            new_no = lst[-1] + lst[-2]
            lst.append(new_no)
        return lst     #return list 
        

