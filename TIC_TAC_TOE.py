from random import randint, choice

print('V= Scissors, O= Rock, W= Paper')
name = input('Enter play: ').upper()
game = ['V', 'O', 'W']
LT = []

def computerplay():
    X = choice(game)
    return X

def winxlose(player,comp):
    if player == 'V':
        if comp == 'V':
            return 'Draw' 
        elif comp == 'O':
            return 'Lose'
        elif comp == 'W':
            return 'Win'
    elif player == 'O':
        if comp == 'V':
            return 'Win'
        elif comp == 'O':
            return 'Draw'
        elif comp == 'W':
            return 'Lose'
    elif player == 'W':
        if comp == 'V':
            return 'Lose'
        elif comp == 'O':
            return 'Win'
        elif comp == 'W':
            return 'Draw'
    else:
        return 'Make the right choice'

def res(L):
    return count(L)

while name != 'END':
    compplay= computerplay()
    print('Player Plays: ', name)
    print('Computer Plays: ', compplay)
    result= winxlose(name,compplay)
    print(result)
    LT.append(result)
    print('')
    print('V= Scissors, O= Rock, W= Paper, End= End game')
    name = input('Enter Play: ').upper()
    

possibility = ['Win', 'Lose', 'Draw']
for a in possibility:
    no= LT.count(a)
    print(a, no)
    