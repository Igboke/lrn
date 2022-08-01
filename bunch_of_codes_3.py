#population=50000
#ini_yr=0
#RATE=0.1
#while population > 20000:
#    population =population-population*RATE
#    if population<=20000:break
#    ini_yr+=1
#    print(ini_yr,population)
    
    
#n = int(input("Enter quantity of numbers to enter: "))
#total = 0
#for i in range(n):
#    a = float(input("Enter number No" + str(i + 1) + ": "))
#    total += a
#print("Sum:", total)


#x=1
#for no in range(20):
#    number=int(input('Enter number'+str(no+1)+': '))
#    val=number *x
#    x=val
#print(val,'\n',val/20)



'''Design a Python program that prompts the user to enter 30 four-digit integers and then calculates and displays the sum of those with a first digit of 5 and a last digit of 3. For example, values 5003, 5923, and 5553 are all such integers.'''
#val=0
#for _ in range(10):
#    x=int(input('Enter 4 digit number: '))
#    if x//1000==5 and (x-3)%10==0:
#        val+=x
#print(val)



'''Design a Python program that prompts the user to enter two integers into variables start and finish and then displays all integers from start to finish that are multiples of five. However, at the beginning the program must check if variable start is bigger than variable finish. If this happens, the program must swap their values so that they are always in the proper order.'''
#start=int(input())
#finish=int(input())
#start1=min(start,finish)
#finish1=max(start,finish)
#for val in range(start1,finish1,5):
#    print(val)
    
    
'''Write a Python program that prompts the user to enter a real and an integer and then displays the result of the first number raised to the power of the second number, without using either the exponentiation operator ( ** ) or the built-in pow() function of Python.'''
#n1=int(input())
#n2=int(input())
#val=1
#for i in range(n2):
#    val=n1*val
#    print(val)


'''Write a Python program that prompts the user to enter a message and then displays the average number of letters in each word. For example, if the message entered is “My name is Aphrodite Boura”, the program must display “The average number of letters in each word is 4.4”. Space characters must not be counted.'''
#message=input()
#x=message.split()
#count=0
#len(sentence)/no. of words
#nowds=len(x)
#for val in x:
#    for dr in val:
#        count+=1
#print(count/nowds)




#for val in range(1,5):
#    print('*'*val)
#for val in range(5,0,-1):
#    print('*'*val)

#multiplicarion table hsing nested loops
#for i in range(1, 10):
#    for j in range(1, 10):
#        print(i, "x", j, "=", i * j, end = "\t")
#    print()
    
    
    
#count_names = 0
#count_not_johns = 0
#name = ""
#while name != "Stop":
#    count_names += 1
#    name = input("Enter a name: ").capitalize()
#    if name != "John":
#        count_not_johns += 1
#print(count_names, "names entered")
#print("Names other than John entered", count_not_johns, "times")




'''2.Write a Python program that prompts the user to enter some text. The text can be either a single word or a whole sentence. Then, the program must display a message stating whether the given text is one single word or a complete sentence.'''
sen=input()
count =0
for ch in sen:
    if ch == ' ':
        count+=1
if count > 0:
    print('sentence')
else:
    print('word')