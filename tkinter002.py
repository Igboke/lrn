from tkinter import *
from tkinter.messagebox import showinfo

def reply_guy(name):
    showinfo(title='The reply',message=f'Hello {name}')

window = Tk()
window.title('Tester GUI code')
Label(window,text='Enter your name ').pack(side='top')
ent = Entry(window)
ent.pack(side='left')
buttn = Button(window,text='Enter',command=lambda:reply_guy(ent.get()))
buttn.pack(side='left')

window.mainloop()