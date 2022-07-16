'''Bank of Nigeria founded 2022 by Igboke Daniel'''
from math import *
class Bank:
    #The Bank accept Users, providing access to secure savings account, fast withdrawal (no limit), and secure low interest loans
    def __init__(self,name,id,cash=0,loan=0):
        #deposit is automatically 0, id is given and name
        #add feature for multiple account holders, done, cust1=Bank(...), cust2=Bank(...)
        self.name=name
        self.id=id
        self.balance=cash
        self.loan=loan
        
    def getbalance(self):
        return self.balance
        
    def deposit(self,cash):
        #amount to deposit
        self.balance+= cash
        return self.balance
        
    def withdraw(self,cash):
        #cash to withdraw
        if cash > 150000:
            return 'Withdrawal Limit Reached Reduce Amount'
        elif cash>self.balance:
            return 'Insufficient funds'
        else:
            self.balance= self.balance-cash
        return self.balance
    
    def loans(self,amount):
        #method for requestimg loan, dependent on BALANCE, returns interest if balance is right
        if self.balance>10000:
            self.loan+=amount
            self.balance+=amount
            x=(5/100)*amount
            y=self.loan+x
            self.loan=y
            return str(self.balance) + 'Amount to be repaid '+ str(y)+ 'interest:' + str(x)
        else:
            return 'Loan application denied'
    def __str__(self):
        return 'Name: ' + self.name +'\n'+'ID: ' + self.id +'\n' + 'Balance:' + str(self.balance) + '\n' + 'Amount to be repaid: '+ str(self.loan)