import tkinter
import os
window =tkinter.Tk
window = tkinter.Tk()
window.title('knopkani boss')
window.geometry('340x440')
window.configure(bg='white')
def kopiyuter_ochadi():
    os.system('shutdown /s /t 0')
tugma = tkinter.Button(window, text="ustiga bosing",command=kopiyuter_ochadi)
tugma.pack(pady=70)

window.mainloop()