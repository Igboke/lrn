import tkinter as tk
import time
from datetime import datetime, timedelta
from playsound import playsound
import threading

class AlarmGUI:
    def __init__(self):
        '''These acts will be realised once the class is instantiated'''

        #create the Tkinter object
        self.window = tk.Tk()

        #Create a title
        self.window.title('Alarm Clock')

        #initial size
        self.window.geometry('400x300')

        #resizing
        self.window.grid_rowconfigure(2,weight=3)
        self.window.grid_columnconfigure(0,weight=3)
        self.padding = {'padx':5,'pady':5}

        #creating the widegets
        #Label
        self.label = tk.Label(self.window, text='Enter the Time in Minutes')
        #grid it
        self.label.grid(column=0,row=0,**self.padding)

        #entry object
        self.ent = tk.Entry(self.window)
        self.ent.grid(column=0,row=1,**self.padding)

        #giant display stopwatch
        self.display = tk.Label(self.window, text='00:00',font=('Times New Roman','36'))
        self.display.grid(column=0,row=2,**self.padding)

        #buttons
        #button frame so the buttons can be aligned
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.grid(row=3,column=0)
        self.button1 = tk.Button(self.buttonframe,text='START',command=self.start_func)
        self.button2 = tk.Button(self.buttonframe,text='STOP',command=self.stop_func,state='disabled')
        self.button1.pack(side='left',padx=10)
        self.button2.pack(side='left',padx=10)

        #controller for stop and start
        self.control = False

    def validate_input(self) -> (int|None):
        try:
            timex = int(self.ent.get())
            if timex <= 0:
                raise ValueError('Time must be Positive')
            return timex
        except ValueError:
            self.display.config(text='Invalid Input')
            return None
    
    
    def start_func(self):
        minutes = self.validate_input()
        if minutes is None:
            return
        self.control = True
        self.button1.config(state='disabled')
        self.button2.config(state='normal')
        self.ent.config(state='disabled')
        #use threading. looks like threading is the only way available to me to run multiple processes, i.e countdown and update gui simultaneously
        #i should consider this n intro to concurrent programming
        self.timer_thread = threading.Thread(target=self.countdown,args=(minutes,),daemon=True)
        self.timer_thread.start()
        

    def stop_func(self):
        self.control=False
        self.button1.config(state='normal')
        self.ent.config(state='normal')
        self.button2.config(state='disabled')
        self.display.config(text='00:00')   
    
    def countdown(self,minutes):
        timex = datetime.now() + timedelta(minutes=minutes)
        #datetime.now gives us the current date and time
        #times is the date and time we wish the alarm to sound
        while self.control and datetime.now() < timex:
            remaining_time = timex - datetime.now()
            mins,secs= divmod(remaining_time.seconds,60)

            #after 0.1 seconds update the giant clock
            self.window.after(0,self.display.config,{'text':f'{mins:02d}:{secs:02d}'})
        
        if self.control:
            #if it ends normally without interruption
            self.stop_func()
            self.play_alarm()

    def play_alarm(self):
        try:
            playsound(r'C:\\Users\\Lenovo\\Documents\\scripts\\alarm.mp3')
        except Exception as e:
            self.display.config(text=f'Could not play sound: {e}')

    def run(self) -> None:
        #run the application
        self.window.mainloop()

if __name__ == '__main__':
    a=AlarmGUI()
    a.run()
