from tkinter import *
from tkinter.messagebox import showinfo
def messages():
    showinfo(title='son of a Bitch',message='Lucky guy')
window = Tk()
button = Button(window,text='squeeze',command=messages)
button.pack()
window.mainloop()