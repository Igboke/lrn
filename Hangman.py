#Hangman game
#without the graphic hanging
import random

words = ['concatenate','graphic','describe','xylophone','aquarius','bellend','quintessential','amoeba','messi', 'greatest']

#randomly generated word selector
def pick_word():
    return random.choice(words)

#game proper
def dash(word,lst):
     x=''
     for char in word:
         if char in lst:
             x+=char
         else:
             x+=' _ '
     return x
            

def dashes(word):
    a=len(word)
    return a, a * ' _ '

wrd= pick_word()
vo=[]
name,v='',''

#start game
qq,dd= dashes(wrd)
print(f'It is a/an {qq} letter word')

while v != wrd:
    name = input('pick a word: ')
    vo.append(name)
    v= dash(wrd,vo)
    print(v)       
    

    