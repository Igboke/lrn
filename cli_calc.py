#CLI_CALC

#Define functionality



#Number 1, basic calculations
def basic_cli_calc():
    print('Enter Numbers only')
    operand_1 = input('Operand 1: ')
    operator = input('+, *, /, - : ') 
    operand_2 = input('Operand 2: ')
    if operand_1.isdigit() and operand_2.isdigit() :
        operand_1,operand_2=int(operand_1),int(operand_2)
        if operator == '+':
            ad=add(operand_1,operand_2)
            return ad
        elif operator == '-':
            su=subtract(operand_1,operand_2)
            return su
        elif operator == '/':
            di=divide(operand_1,operand_2)
            return di
        elif operator == '*':
            mu=multiply(operand_1,operand_2)
            return mu
    else:
        return 'Invalid Operands'
        
def add(a:int,b:int) ->  int:
    return  a+b
def subtract(a:int,b:int) ->  int:
    return a-b
def divide (a:int,b:int) ->  int:
    return a/b
def multiply (a:int,b:int) ->  int:
    return a*b 
                                            
#Even vs Odd
def even_vs_odd():
    digit = input('Enter digit: ') 
    if digit.isdigit():
        digit=int(digit)
        return 'Even' if digit % 2 == 0 else 'Odd'    
    else:
        return 'Enter a number'   
        
options = {1:basic_cli_calc, 2:even_vs_odd ,3:' ',4:'end'}
options_clone = {1:'Basic Calculations', 2:'Even or Odd' ,3:'Complex calculations',4:'end'}

while True:
    print('')
    print(options_clone)
    number = input('Enter valid Digit: ')
    if not number.isdigit():
        continue
    elif number in ['1','2','3']:
        print(options[int(number)]())    
    else:
        break  
           