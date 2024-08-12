#decorator with arguments
#create a decorator that takes arguments like a multiplier, and modifies the behaviour
#of the function it decorates
def multiply_res(no):
    def multiplier (func):
        def wrapper(*args,**kwargs):
            fundue = func(*args,**kwargs)
            return fundue * no
        return wrapper
    return multiplier

@multiply_res(6)
def adder (a,b,c):
    return a + b + c

g = adder (10,11,12)
print(g)