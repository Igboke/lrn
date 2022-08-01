'''Write a Python program that lets the user enter 50 integers in a list and then calculates and displays the sum of those that have two digits'''

#l=[]
#v=[]
#for i in range(10):
#    x=int(input())
#    l.append(x)
#for ch in l:
#    if ch >9:
#        v.append(ch)
#print(sum(v))


'''Write a Python program that lets the user enter numeric values into a 10 × 10 list and then calculates the sum of the elements of its main diagonal.'''
#N=8
#total=0
#matrix=[[None]*N for i in range(N)]
#for i in range(N):
#    for j in range(N):
#        if i==j:
#            matrix[i][j]=10
#        elif i<j:
#            matrix[i][j]=5
#        else:
#            matrix[i][j]=20
#for c in range (N):
#    total+=matrix[c][c]
#print(total)
#print(matrix)
#            
#for x in range(N):
#    for y in range(N):
#            print(matrix[x][y],end='\t')
#    print()
            
'''Write a Python program that lets the user enter words in a 10 × 7 list and displays those that have less than 5 characters, then those that have less than 10 characters, and finally those that have less than 20 characters. Assume that the user enters only words with less than 20 characters.'''
#table=[[None]*7 for i in range(10)]
#for i in range(10):
#    for j in range(7):
#        table[i][j]=input(f'enter word located at row {i},column{j}: ')
#print(table)
#for i in range(10):
#    for j in range(7):
#        if len(table[i][j])<5:
#            print(table[i][j],'is less than 5 characters')
            

'''Write a Python program that lets the user enter 10 positive numerical values into a list. Then, the program must create a new list of 8 elements. This new list must contain, in each position the average value of the three elements that exist in the current and the next two positions of the given list.'''
  
            
#original_list=[]
#new_list=[]
#for i in range(10):
#    original_list.append(int(input(f'Enter no{i}: ')))
#for i in range(8):
#    x=original_list[i:i+3]
#    new_list.append(round(sum(x)/3))
#for ch in new_list:
#   print(ch,end='\t')


'''Write a Python program that prompts the user to enter 20 odd positive integers into a list and then displays them in the exact reverse of the order in which they were given. The program must also validate data input, not allowing the user to enter a non-positive value, a float, or an even integer. There is no need to display any error messages.'''
#odd=[]
#for i in range(5):
#    while True:
#        print('Enter an odd number')
#        x=float(input())
#        if x >0 and x%2!=0 and x==int(x):break
#    odd.append(x)
#for element in odd[::-1]:
#    print(element,end='\t')                                                 

#ELEMENTS =5
#odds = [None] * ELEMENTS
#for i in range(ELEMENTS):
#        while True:
#            x = float(input("Enter an odd positive integer: "))
#            if x > 0 and x == int(x) and x % 2 != 0: break
#        odds[i] = int(x)
#for i in range(ELEMENTS - 1, -1, -1): 
#    print(odds[i], end = "\t")


#sorting a list
#l=[5,67,865,43,446]
#l.sort(reverse=True)
#x=sorted(l)
#print(l) 
#print(x)


'''Twelve teams participate in a football tournament, and each team plays 20 games, one game each week. Write a Python program that prompts the user to enter the name of each team and the letter “W” for win, “L” for loss, or “T” for tie (draw) for each game. Then the program must prompt the user for a letter (W, L, or T) and display, for each team, the week number(s) in which the team won, lost, or tied respectively. For example, if the user enters “L”, the Python program must search and display, for each team, the week numbers (e.g., Week 3, Week 14, and so on) in which the team lost the game.'''

#names=[]
#team_table=[[None]*10 for i in range(10)]  
#for i in range(10):
#    names.append(input('Enter Football team: '))
#for i in range(10):
#    for j in range(10):
#        team_table[i][j]=input(f'enter score for week{i}, team {names[j]}: ')
#for team in team_table:
#    print (team,end='\t')


def display(color, exists):
    neg = ""
    if not exists:
        neg = "n't any"
    return "There is" + neg + " " + color + " in the rainbow"
#Main code starts here
print(display("red", True))
print(display("yellow", True))
print(display("black", False))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                              