#def display_value():
#    global test #Force Python to use the global variable test
#    print(test) #It displays: 10
#    test = 20
#    print(test) #It displays: 20
#Main code starts here
#test = 10 #This is a global variable
#display_value()
#print(test) #It displays: 20
'''Write a subprogram named find_area that accepts the base and the height of a parallelogram through its formal argument list and then returns its area.'''
'''Using the subprograms cited above, write a Python program that prompts the user to enter the base and the height of a parallelogram and then calculates and displays its area. The program must iterate as many times as the user wishes. At the end of each calculation, the program must ask the user whether he or she wishes to calculate the area of another parallelogram. If the answer is “yes” the program must repeat.'''
#def find_area(b,h):
#    return 0.5*b*h
#x=''
#while True:
#    if x=='end':
#        break
#    print('Enter base and height')
#    b=int(input())
#    h=int(input())
#    print(find_area(b,h))
#    x=input('Do you wish to continue? Type end to terminate: ').lower()
    
'''On a chessboard you must place grains of wheat on each square, such that one grain is placed on the first square, two on the second, four on the third, and so on (doubling the number of grains on each subsequent square). Do the following:
i.Write a recursive function named woc that accepts the index of a square and returns the number of grains of wheat that are on this square. Since a chessboard contains 8 × 8 = 64 squares, assume that the index is an integer between 1 and 64.'''
def woc(i):
    if i ==1:
        grain =1
    else:
        grain=woc(i-1)*2
    return grain
print(woc(4))