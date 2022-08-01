#a = "Ares"
#print("Hello", a, end = " - ")
#print("Halo", a, end = " - ")
#print("Salut", a)
#print("John\tGeorge\nSofia\tMary")
#print("What is your name? ", end='')
#name = input()
#print("What is your age? ", end = "")
#age = int(input())
#print("Wow, you are already", age, "years old,", name, "!")

#import random
#print(random.randrange(10, 101))
#y = random.randrange(11)
#print(y)
#print(random.randrange(-20, 21))
#print(random.randrange(1, 99, 2))
#print(random.randrange(0, 100, 2))
#print(round(2.767,2))

#mport math
#print("Enter coordinates for point A: ")
#x1, y1 = float(input()), float(input())
#print("Enter coordinates for point B: ")
#x2, y2 = float(input()), float(input())
#d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#print("Distance between points:", d)

#import math
#print('Enter no')
#a = float(input())
#a += 6 / math.sqrt(a) * 2 + 20
#b = round(a) % 4
#c = b % 3
#print(a, ",", b, ",", c)

#x = float(input("Enter value for x: "))
#w = float(input("Enter value for w: "))
#z = float(input("Enter value for z: "))
#y = (5 * (3 * x ** 2 + 5 * x + 2) / (7 * w - 1 / z) - z) / (4 * ((3 + x) / 7))
#y=((3*x**2)-(x**3/4))**0.2
#y=7*x/((2*x+4*(x**2+4)))
#print("The result is:", y)

#no=int(input('Enter 4 digit number: '))
#a,w=divmod(no,1000)
#b,x=divmod(w,100)
#c,y=divmod(x,10)
#d,z=divmod(y,1)
#print(a+b+c+d)

#x=input()
#l=len(x)
#newstr=x[l::-1]
#print(newstr)

#x=input()
#y=len(x)
#w=x[-1]
#v=int(w)
#print(v*8)

#count20=0
#count10=0
#count5=0
#count1=0
#number=int(input())
#while number > 0:
#    if number%20==0:
#        count20+=1
#        number-=20
#    elif number%10==0:
#        count10+=1
#        number-=10
#    elif number%5==0:
#        count5+=1
#        number-=5
#    else:
#        count1+=1
#        number-=1
#print(count20,'note(s) of $20', '\n', count10, 'note(s) of $10','\n',count5, 'note(s) of $5', '\n',count1, 'note(s) of $1')

#a = "       Hello       "
#a = a.strip()
#print(a,"Poseidon!"*3,sep='\n')
#print(a, "Poseidon!")

#a='shit'.replace('shit','johncena').upper()
#x=a[:2:-1]#in the form [a:b:c]a= end(if c is -ve)/length of string,b=start(when -ve),c=step/direction(when -ve)
#print(x)

#name = [1,2,3,4,5,6,7,8]
#a, b, c, d,e,r,t,t = name
#print(a)
#print(b)
#print(c)
#print(d)

#import string
#re=string.ascii_lowercase
#count=0
#for alpha in re:
#    count+=1
#    if alpha=='c':
#        print('dance')
#        print(count)

x='Igboke Daniel'
a,b=x.split()
print(b,a)
f=x[5]
print(f)

