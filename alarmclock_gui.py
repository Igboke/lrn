import tkinter as tk
from tkinter import filedialog
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
        self.buttonframe.grid(row=4,column=0,pady=10)
        self.button1 = tk.Button(self.buttonframe,text='START',command=self.start_func)
        self.button2 = tk.Button(self.buttonframe,text='STOP',command=self.stop_func,state='disabled')
        self.button1.pack(side='left',padx=10)
        self.button2.pack(side='left',padx=10)

        #alarm sound selection frame
        self.sound_frame = tk.Frame(self.window)
        self.sound_frame.grid(row=3,column=0,pady=10)

        #sound selection
        self.sound_label = tk.Label(self.sound_frame,text='Alarm Sound: ')
        self.sound_label.pack(side='left')
        #initialization
        self.selected_sounds= tk.StringVar(self.sound_frame)
        self.selected_sounds.set('Select a Sound File')
        self.recent_sounds = ['Select a Sound File']

        #Option menu
        self.sound_option = tk.OptionMenu(self.sound_frame,self.selected_sounds,*self.recent_sounds,self.update_selected_sounds)
        self.sound_option.pack(side='left',padx= 5)

        #Browser button
        self.browse_button = tk.Button(self.sound_frame,text='Browse',command=self.browse_sound_files)
        self.browse_button.pack(side='left',padx=5)

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
        #timex is the date and time we wish the alarm to sound
        while self.control and datetime.now() < timex:
            remaining_time = timex - datetime.now()
            mins,secs= divmod(remaining_time.seconds,60)

            #after 0.1 seconds update the giant clock
            self.window.after(0,self.display.config,{'text':f'{mins:02d}:{secs:02d}'})
            self.window.after(100) #added this since the quick transition from updating the giant clock and calculating the time was lagging the clock
        
        if self.control:
            #if it ends normally without interruption
            self.stop_func()
            self.play_alarm()

    def update_selected_sounds(self,value):
        pass
    def browse_sound_files(self):
        filename = filedialog.askopenfilename(title='Select Sound File',filetypes=[('Audio Files',['.wav','.mp3','.ogg'])])
        if filename:
            #sets the song file to be played, will be gotten using self.selected_sounds.get()
            self.selected_sounds.set(filename)
            if filename not in self.recent_sounds:
                #adds the file name to the drop down menu through the list options created when instantiated
                self.recent_sounds.append(filename)
                self.sound_option['menu'].delete(0,'end')
                for sound in self.recent_sounds:
                    #just in case you browsed more than 1 song the option you pick already has a command attached to it once you select it
                    #learned about late binding
                    #the for loop asigns all our songs added to the list (recent sounds) to the variable sound, because of late binding only the last song added is eligible for 'setting i.e to .set' but when a x = song is used we assign the current clicked object to x, in late binding we cannot do that since the last value automatically gets assigned the variable name 
                    self.sound_option['menu'].add_command(label=sound,command=lambda x=sound:self.selected_sounds.set(x))
        
    def play_alarm(self):
        sound_ = self.selected_sounds.get()
        if sound_ != 'Select a Sound File':
            try:
                playsound(sound_)
            except Exception as e:
                self.display.config(text=f'Could not play sound: {e}')

    def run(self) -> None:
        #run the application
        self.window.mainloop()

if __name__ == '__main__':
    a=AlarmGUI()
    a.run()
