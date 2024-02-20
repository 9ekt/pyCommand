try:
    import asyncio
    import websockets
    import os
    import threading
    import tkinter as tk
    from tkinter import messagebox, colorchooser
    import uuid
except Exception as err:
    print(err)


account = 'No Name'
printlist = 0
lastSearchPos = 1.0
defultHEX = '#ffffff'
websock = "wss://free.blr2.piesocket.com/v3/1?api_key=fAKgINTsOVhYKF1d7NE3U5xOs4QwoDN2Do5Bp0D4&notify_self=1"
ChatDisabled = False
Configuration = {
    'HasKeyBinds' : False,
    'Binds' : ''
}

async def listner(r):
    global ChatDisabled
    async with websockets.connect(websock) as wb:
        if r == 'SilenceChat':
            await wb.send(f'SilenceChat')
        elif r == 'troll':
            await wb.send(f'^*!*^8')
        elif r == 'cmd_status':
            await wb.send('cmd_status')
            response = await wb.recv()
        elif not ChatDisabled:
            await wb.send(f'[{account}]: {r}^{defultHEX}')
            response = await wb.recv()
        else:
            UI.Output([f'The chat is currently disabled and can only be used by admins.\n','msg'],False)
            
        

        
async def receive_data():
    global ChatDisabled
    async with websockets.connect(websock) as websocket:
        while True:
            data = await websocket.recv()
            
            if data == "SilenceChat":
                ChatDisabled = not ChatDisabled
                UI.Output([f'The chat has been toggled by a moderator.\n','msg'],False)
            elif data == '^*!*^8':
                messagebox.showerror('pycmd Global Chat', 'womp womp did u get banned sad boy.')
                quit()
            
            UI.Output([f'{data}\n','msg'],False)

def init_recv():
    coro_connec = receive_data()
    asyncio.run(coro_connec)

OutputManager = None
class UI(tk.Tk):
    
    def __init__(self):
        global OutputManager
        super().__init__()
        self.menubar = tk.Menu(self)
        
        self.title('Global Chat')
        self.resizable(False, False)
        self.geometry('350x450')
        
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Chat Color", command=self.SelectCustomChatColor)
        #self.filemenu.add_command(label="Clear Console")
        #self.filemenu.add_separator()
        #self.filemenu.add_command(label="Settings", command=Menu.Settings)
        #self.filemenu.add_separator()
        self.menubar.add_cascade(label="Settings", menu=self.filemenu)
        
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side = 'right', fill = 'both')
        
        self.Output_Storage = tk.StringVar(self, 'Welcome to the pyCommand global chat\nRules:\n1. No rules.')
        
        self.Output = tk.Text(self, wrap='word',font=("Raster Fonts", 10, 'normal'))
        self.Output.config(bg='#1e2124',fg='white',state="disabled",yscrollcommand = self.scrollbar.set)
        self.Output.pack(expand=True, fill='both')
        OutputManager = self.Output
        
        self.Input = tk.Entry(self)
        self.Input.config(bg='#282b30',fg='white')
        self.Input.pack(fill='x',expand=False,anchor='center')
        
        
        
        self.Input.bind('<Return>', lambda e: [self.ProcessMessage(self.Input.get()),self.Input.delete(0, 'end')])
        
        self.config(menu=self.menubar)
        self.mainloop()
        
    def SendMessage(self, s):
        self.title('Global Chat - Sending Message')
        coro_listen = listner(s)
        asyncio.run(coro_listen)
        self.title('Global Chat')
        
    def ProcessMessage(self, msg):
        global account
        global ChatDisabled
        if msg.lower() == '/help':
            UI.Output([f'Help:\n1. /name (new name)- Allows you to change your name\n','msg'],False)
        elif '/name' in msg.lower():
            split = msg.split('/name', 1)[1].lstrip()
            
            if len(split) > 15:
                UI.Output([f'Your name is too long.\n','msg'],False)
            else:
                account = split
                UI.Output([f'Your name has been set to {account}\n','msg'],False)
        elif '/troll' in msg.lower():
            self.SendMessage('troll')
        elif '/test' in msg.lower():
            self.SendMessage('cmd_status')
        else:
            if len(msg) >= 1:
                self.SendMessage(self.Input.get())
            else:
                UI.Output([f'Warning: Your message is too small to send.\n','warning'],False)
    
    def SelectCustomChatColor(self):
        global defultHEX
        new_color = colorchooser.askcolor()[1]
        
        if new_color != None:
            defultHEX = new_color
    def Output(win=None,advancelog=False):
        global OutputManager
        global printlist
        global lastSearchPos
        if isinstance(win, (list,tuple)):
            if len(win) >= 2:
                store_dataval = uuid.uuid4()
                if win[1].lower() == 'error':
                    OutputManager.config(state="normal")
                    OutputManager.insert('end', '[ X ] ' + win[0] + '\n')
                    OutputManager.config(state="disabled")
                    printlist = printlist + 1
                    OutputController.yview('end')
                    

                    pos_start = OutputManager.search('[ X ] ' + win[0], lastSearchPos, 'end')
                    offset = '+%dc' % len('[ X ] ' + win[0])
                    pos_end = pos_start + offset
                    OutputManager.tag_add(f"err{store_dataval}", pos_start, pos_end)
                    OutputManager.tag_config(f"err{store_dataval}", background="#1e2124", foreground="red") 
                    lastSearchPos = pos_end
                elif win[1].lower() == 'warning':
                    OutputManager.config(state="normal")
                    OutputManager.insert('end', '[ ! ] ' + win[0] + '\n')
                    OutputManager.config(state="disabled")
                    printlist = printlist + 1
                    OutputManager.yview('end')
                    
                    pos_start = OutputManager.search('[ ! ] ' + win[0], lastSearchPos, 'end')
                    offset = '+%dc' % len('[ ! ] ' + win[0])
                    pos_end = pos_start + offset
                    OutputManager.tag_add(f"warn{store_dataval}", pos_start, pos_end)
                    OutputManager.tag_config(f"warn{store_dataval}", background="#1e2124", foreground="yellow")
                    lastSearchPos = pos_end
                else: 
                    new_split = win[0].split('^')
                    color = 0
                    
                    try:
                        color = new_split[1].rstrip()
                    except Exception as err:
                        color = 'white'
                        
                    
                    
                    OutputManager.config(state="normal")
                    OutputManager.insert('end', new_split[0] + '\n\n')
                    OutputManager.config(state="disabled")
                    printlist = printlist + 1
                    OutputManager.yview('end')
                    
                    pos_start = OutputManager.search(new_split[0] + '\n\n', lastSearchPos, 'end')
                    offset = '+%dc' % len(new_split[0] + '\n\n')
                    pos_end = pos_start + offset
                    OutputManager.tag_add(f"custom_msg{store_dataval}", pos_start, pos_end)
                    OutputManager.tag_config(f"custom_msg{store_dataval}", background="#1e2124", foreground=color)
                    lastSearchPos = pos_end
        


def Start():
    threading.Thread(target=init_recv).start()
    UI()
    
    

