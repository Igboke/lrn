#def display_line(length):
#    for i in range(length):
#        print("-", end = "")
#    print()
#Main code starts here
#print("Hello there!")
#display_line(12)
#print("How do you do?")
#display_line(14)
#print("What is your names")

#def total(x,y):
#    return x+y
#print('Enter two digits')
#x,y=int(input()),int(input())
#print(f'the sum of {x} and {y} is',total(x,y))

#practising void functions
#def minimum(val1, val2, val3):
#    minim = val1
#    if val2 < minim:
#        minim = val2
#    if val3 < minim:
#        minim = val3
#    print(minim)
#Main code starts here
#a = float(input())
#b = float(input())
#c = float(input())
#d=minimum(a, b, c)
#print('The End')


'''i.Write a subprogram named display_abs that accepts a numeric value through its formal argument list and then displays its absolute value. Do not use the built-in abs() function of Python'''
#def display_abs(val):
#    abs_=val
#    if abs_<0:
#        abs_=abs_*-1
#    return abs_,val
#print(display_abs(-57))
'''The Body Mass Index (BMI) is often used to determine whether a person is overweight or underweight for his or her height.''' 
#def bmi(h,w):
#    x=w*703/(h**2)
#    if x < 16:
#        print('you must add weight')
#    elif x< 18.5:
#        print('you ahould add some more wight')
#    elif x<25:
#        print('maintain your weight')
#    elif x<30:
#        print('lose some weight')
#    elif x>30:
#        print('must lose weight')
#bmi(180,540)
'''Write a subprogram named num_of_days that accepts a year and a month (1 – 12) through its formal argument list and then displays the number of days in that month. Take special care when a year is a leap year; that is, a year in which February has 29 instead of 28 days.
Hint: A year is a leap year when it is exactly divisible by 4 and not by 100, or when it is exactly divisible by 400.
ii.Using the subprogram cited above, write a Python program that prompts the user to enter a year and then displays the number of the days in each month of that year.''' 
#def num_of_days(yr,mn):
#    if mn in[4,6,9,11]:
#        print('30 days')
#    elif mn in [1,3,5,7,8,10,12]:
#        print('31 days')
#    elif yr %4==0 and yr%100!=0 or yr%400==0:
#        print('Leap Year')
#        if mn==2:
#            print('29 days')
#    else:
#        print('28 days')
#x=int(input())
#for y in range(1,13):
#    num_of_days(x,y)     
#num_of_days(2015,6)
'''The LAV Cell Phone Company charges customers a basic rate of $10 per month, and additional rates are charged based on the total number of seconds a customer talks on his or her cell phone within the month. Use the rates shown in the following table.
i.Write a subprogram named amount_to_pay that accepts a number in seconds through its formal argument list and then displays the total amount to pay. Please note that the rates are progressive. Moreover, federal, state, and local taxes add a total of 11% to each bill
ii.Using the subprogram cited above, write a Python program that prompts the user to enter the number of seconds he or she talks on the cell phone and then displays the total amount to pay.'''         
#def amount_to_pay(secs):
#    if secs <= 600:
#        t=10
#    elif secs <=1200:
#        t=10 + (secs-600)*0.01
#    else:
#        t= 10+(600*0.01)+(secs-1200)*0.02
#    t=t*0.11+t
#    return '$' + str(t)
#x=int(input())
#print(amount_to_pay(x))

#def my_divmod(a, b, results):
#    return_value = True
#    if b == 0:
#        return_value = False
#    else:
#        results[0] = a // b
#        results[1] = a % b
#    return return_value
#Main code starts here
#res = [None] * 2
#val1 = int(input())
#val2 = int(input())
#ret = my_divmod(val1, val2, res)
#if ret:
#    print(res[0], res[1])
#else:
#    print("Sorry, wrong values entered!")
    
    


'''The following Python program is supposed to prompt the user to enter five integers into a list and then display, for each element, its number of digits and the integer itself. For example, if the user enters the values 35, 13565, 113, 278955, 9999, the Python program is supposed to display:
2 are the digits of 35
5 are the digits of 13565
3 are the digits of 113
6 are the digits of 278955
4 are the digits of 9999
Unfortunately, the following Python program displays
2 are the digits of 0
5 are the digits of 0
3 are the digits of 0
6 are the digits of 0
4 are the digits of 0
Can you find out why?'''
ELEMENTS = 5
def get_num_of_digits(x, index):
    count = 0
    m[index]=x[index]
    while m[index] != 0:
        count += 1
        m[index] = m[index] // 10
    return count
#Main code starts here
val = [None] * ELEMENTS
m=[None]*ELEMENTS
for i in range(ELEMENTS):
    val[i] = int(input())
for i in range(ELEMENTS):
    print(get_num_of_digits(val, i), "are the digits of", val[i])