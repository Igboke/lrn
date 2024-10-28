import tkinter
from tkinter.messagebox import showinfo, showerror, showwarning
from typing import Dict
import shelve
import logging
#deductions are IOU, LOANS, BANK CHARGES, PAYETAX DEDUCTION, DEV LEVY, CALCULATE TOTAL DEDUCTION
#THEN PRODUCE NETPAY

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Person:
    def __init__(self,name:str,days_worked:int=30,phone_number:str='98706543212',account_number:str='123456789',home_address:str='',bank_name:str='',gross_pay:int=0,IOU:int=0,location: str='General',BVN:int=000000000,NIN:int=1234567890):
        self.name = name
        self.IOU = IOU
        self.location = location
        self.days_worked = days_worked
        self.account_number = account_number
        self.bank_name= bank_name
        self.phone_number = phone_number
        self.BVN = BVN
        self.NIN = NIN
        self.PAYE = 250
        self.DEVY= 100
        self.bankcharges=54
        self.home_address=home_address
        self.pay_per_day = gross_pay // 30
        

    def deductions(self)->int:
        total_deductions= self.IOU + self.PAYE + self.DEVY + self.bankcharges
        return total_deductions 
    
    def grosspay(self)->int:
        self.gross_pay = self.pay_per_day * self.days_worked
        return self.gross_pay
    
    def net_pay(self):
        self.netpay = self.grosspay() - self.deductions()
        return self.netpay
    
    def __str__(self):
        return f'{self.__class__.__name__}, {self.__dict__}'
    



class ContinentalsGUI:
    variables_= ('name','location','days_worked','account_number','bank_name','home_address','phone_number','BVN','NIN','IOU')
    def __init__(self,db_name:str='ContinentalsSecuritytest'):
        self.data_base = shelve.open(db_name)
        self.entries: Dict[str, tkinter.Entry] = {}
        
        self.window = tkinter.Tk()
        self.window.title('Continentals Security')
        self.create_widgets()
    
    def create_widgets(self):
        'create and arrange the GUI objects'
        frame = tkinter.Frame(self.window)
        frame.pack(padx=10,pady=10)

        #create Labels and Entry
        for idx, label in enumerate(('key',)+ContinentalsGUI.variables_):
            tkinter.Label(frame,text=label.title()).grid(row=idx,column=0,sticky=tkinter.W,padx=5,pady=2)
            entry = tkinter.Entry(frame)
            entry.grid(row=idx, column=2, padx=5, pady=2)
            self.entries[label]= entry

        #create button frame
        button_frame = tkinter.Frame(self.window)
        button_frame.pack(pady=5)

        #create buttons
        tkinter.Button(button_frame,text='FETCH',command=self.fetchrecord).pack(side=tkinter.LEFT,padx=5)
        tkinter.Button(button_frame,text='UPDATE',command=self.updateRecord).pack(side=tkinter.LEFT,padx=5)
        tkinter.Button(button_frame,text='CLEAR',command=self.clear_field).pack(side=tkinter.LEFT,padx=5)
        tkinter.Button(button_frame,text='SALARY SCHEDULE',command=self.donnothing).pack(side=tkinter.LEFT,padx=5)
        tkinter.Button(button_frame,text='PAY SLIP',command=self.donnothing).pack(side=tkinter.LEFT,padx=5)
        tkinter.Button(button_frame,text='QUIT',command=self.quit_app).pack(side=tkinter.LEFT,padx=5)
    
    def fetchrecord(self):
        #getting records
        key = self.entries['key'].get().strip().lower()
        #name_key = self.entries['name'].get().strip()
        if not key:
            showwarning('WARNING','PLEASE INPUT KEY OR NAME')
            return
        try:
            record = self.data_base[key]
            self.clear_field()
            self.entries['key'].insert(0,key)
            
            for value in ContinentalsGUI.variables_:
                self.entries[value].insert(0,str(getattr(record,value)))

        except KeyError:
            showerror('Key Error',f'No key: {key} found')

        except Exception as e:
            logger.error(f'Error fetching object: {e}')
            showerror('Error','Error in fetching record')

        
    def clear_field(self):
        #clearing fields
        for values in self.entries.values():
            values.delete(0,tkinter.END)
    
    def quit_app(self):
        #quit app successfully
        self.data_base.close()
        self.window.quit()

    def donnothing(self):
        showinfo(title='Nothing here yet',message='update in progress')
    
    def updateRecord(self):
        #Update or create new record
        key = self.entries['key'].get().strip().lower()
        if not key:
            showerror('Error Message',message='Please Input a key')
            return
        try:
            #get values from entries
            values = {'name':self.entries['name'].get().strip(),
                      'location':self.entries['location'].get().strip(),
                      'days_worked':int(self.entries['days_worked'].get().strip()),
                      'account_number':self.entries['account_number'].get().strip(),
                      'bank_name':self.entries['bank_name'].get().strip(),
                      'home_address':self.entries['home_address'].get().strip(),
                      'phone_number':self.entries['phone_number'].get().strip(),
                      'BVN':self.entries['BVN'].get().strip(),
                      'NIN':int(self.entries['NIN'].get().strip()),
                      'IOU':int(self.entries['IOU'].get().strip())
                      }
            new_instance = Person(**values)
            self.data_base[key]=new_instance
            showinfo('Successful','Record stored successfully')

            
        except ValueError as e:
            # days_worked, NIN and BVN must be integers
            showerror("Value Error",'Please make sure your values are correct')
        except Exception as e:
            logger.error(f'Error updatign record {e}')
            showerror("Error",'Error Updating record')
    
    def run(self):
        self.window.mainloop()


def main():
    app = ContinentalsGUI('employee_db')
    app.run() 

if __name__ == '__main__':
    main()



    

