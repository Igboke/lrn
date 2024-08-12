#Simple Logging decorator
#The goal is to create a decorator that logs the name of the function,
#the arguments it was called with and the reult is returns

def simple_logging(func):
    def wrapper(*args,**kwargs):
        print (f'This is the name of the function: {func.__name__}', f'With {args} and {kwargs} as arguments', sep = '\n')
        result = func(*args,**kwargs)
        return result
    return wrapper

@simple_logging
def adder (a,b,c):
    return a + b + c

@simple_logging
def hbd(no):
    print ('Happy birthday!!! '*no)
    return no * 10