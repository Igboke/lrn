#bagels
import random
def control(guess):
    return guess.isdigit() and len(guess) == 3
    
def bagels(guess,number):
    for i in guess:
        if i in number:
            return False
    return True

def digi_checker(guess,number):
    lst=[]
    if bagels(guess,number):
        lst.append('bagels')
    for i in range(0,3):
        if guess[i] == number[i]:
            lst.append('Fermi')
        elif guess[i] in number:
            lst.append('Pico')
    return ' '.join(lst)           

i = 0
number = str(random.randint(100,999))
while i < 10:
    guess = input ('Enter Guess: ') 
    if not control(guess):
        print('Check the length and nature of your guess')
        continue
    print(digi_checker (guess,number))
    i+=1
    if guess == number:
        break
else:
    print('wow what a loser')
    print(number)