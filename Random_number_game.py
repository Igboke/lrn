#Guess the correct number, the computer would produce two variables
# whether a number is odd or even
# the range of the number up to 10 numbers

import math
import random
 
def is_even(no):
    return no % 2 == 0 
    
def rnd_choice():
    lst = list(range(0,100))
    a = random.choice(lst)
    b= a+10
    return [a,  b]        

def answer(a,b):
    lst=list(range(a,b+1))
    no=random.choice(lst)
    if is_even(no):
        odd_even = 'The number is Even'
    else:
        odd_even = 'The number is odd'
    return [no,odd_even]
    


#The Game proper
def game_play():
    print('Pick a number between')
    a,b= rnd_choice()
    print(a, '--', b)
    comp_choice, hint= answer (a,b)
    print('Hint: ', hint)
    choie = input('Pick Your number: ')
    if choie == str(comp_choice):
        print('Congratulations')
    else:
        print('Wrong Choice')
        print(comp_choice)
        
Continue = ''
while Continue != 'END':
    game_play()
    Continue=input(f'Continue?... Type end to end game \nType anything to continue:  ').upper()
    print('')

print('Thanks for playing!!!')    