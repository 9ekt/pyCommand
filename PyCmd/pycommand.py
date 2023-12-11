# pycommand

try:
    import tkinter as tk
    from tkinter import Menu, messagebox
    from tkinter.ttk import *
    import os
    import urllib
    from urllib.request import urlopen, Request
    import webbrowser
    import threading
    import json
    import importlib
    import asyncio
    import uuid
    from assets.modules import websockets as websockets
    from assets.modules.playsound import playsound
except ImportError as err:
    print(err)


class Window():
    
    
    def Console():
        global ConsoleWindow
        global Input
        global Output
        ConsoleWindow = tk.Tk()
        menubar = tk.Menu(ConsoleWindow)
        ConsoleWindow.title('pyCommand')
        ConsoleWindow.geometry(Resolution)
        ConsoleWindow.minsize(MinSize['x'], MinSize['y'])
        ConsoleWindow.config(bg=tkWinBackground)
        ConsoleWindow.iconbitmap("assets/source/icon.ico")
        #ConsoleWindow.after(100, Window.ListenForOutputChanges, ConsoleWindow)
        
        scrollbar = tk.Scrollbar(ConsoleWindow)
        scrollbar.pack(side = 'right', fill = 'both')
        
        Output_Storage = tk.StringVar(ConsoleWindow, BootText)
        
        Output = tk.Text(ConsoleWindow, wrap='word',font=("Raster Fonts", 10, 'normal'))
        Output.config(bg='black',fg='white',state="disabled",yscrollcommand = scrollbar.set)
        Output.pack(expand=True, fill='both')
        
        
        Output.config(state="normal")
        Output.insert('end', Output_Storage.get())
        Output.config(state="disabled")
        
        
        Input = tk.Entry()
        Input.config(bg=EntryInputColor,fg='white')
        Input.pack(fill='x',expand=False,anchor='center')
        
        
        
        #x = threading.Thread(target=Menu.KeepFocus)
        #x.start()
        
        # Menus # File Menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Window", command=lambda: Menu.New(ConsoleWindow))
        filemenu.add_command(label="Clear Console", command=lambda: Menu.Clear(Output))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)
        menubar.add_cascade(label="Console", menu=filemenu)
        
        if Mods > 0:
            Output.config(state="normal")
            Output.insert('end', f'\n{str(Mods)} Mods have been found in your mods directory.\nYou can use "start <mod-name>" to start a mod.\n')
            Output.config(state="disabled")
            
            modMenu = tk.Menu(menubar, tearoff=0)
            modMenu.add_command(label="Open Mods Folder", command=Menu.PromptModsFolder)
            modMenu.add_separator()
            modMenu.add_command(label=f"{Mods} Mods Found", command= lambda: Menu.DisplayMods(Output))
            menubar.add_cascade(label="Mods", menu=modMenu)
        
        
        
        versiondetails = tk.Menu(menubar, tearoff=0)
        
        Menu.CheckForUpdates(False)

        if Version != UpToDateVersion:
            versiondetails.add_command(label="Update pyCommand", command=Menu.UpdateClient)  
        else:
            versiondetails.add_command(label="Check for updates", command=Menu.CheckForUpdates)
        
        versiondetails.add_separator()
        versiondetails.add_command(label="Github", command=Menu.Credits)
        menubar.add_cascade(label=Version, menu=versiondetails)
        
        
        Input.bind('<Return>', lambda e: [Window.ProcessCommand(Input.get(),Output),Input.delete(0, 'end')])
        Input.bind('<Up>', lambda e: [Input.delete(0, 'end'),Input.insert(0,lastcmd)])
        Input.bind('<Down>', lambda e: Input.delete(0, 'end'))
        Input.bind('<Key>', lambda e: Window.CheckCharacterLength(Input,Output))
        
        ConsoleWindow.config(menu=menubar)
        ConsoleWindow.mainloop()
        

        
    def Output(win=None,OutputController=None,advancelog=False):
        global printlist
        global lastSearchPos
        if isinstance(win, (list,tuple)):
            if len(win) >= 2:
                store_dataval = uuid.uuid4()
                if win[1].lower() == 'error':
                    OutputController.config(state="normal")
                    OutputController.insert('end', '[ X ] ' + win[0] + '\n')
                    OutputController.config(state="disabled")
                    printlist = printlist + 1
                    OutputController.yview('end')
                    
                    if not lastSearchPos:
                        pos_start = OutputController.search('[ X ] ' + win[0], '1.0', 'end')
                        offset = '+%dc' % len('[ X ] ' + win[0])
                        pos_end = pos_start + offset
                        OutputController.tag_add(f"err{store_dataval}", pos_start, pos_end)
                        OutputController.tag_config(f"err{store_dataval}", background="black", foreground="red") 
                        lastSearchPos = pos_end
                    else:
                        pos_start = OutputController.search('[ X ] ' + win[0], lastSearchPos, 'end')
                        offset = '+%dc' % len('[ X ] ' + win[0])
                        pos_end = pos_start + offset
                        OutputController.tag_add(f"err{store_dataval}", pos_start, pos_end)
                        OutputController.tag_config(f"err{store_dataval}", background="black", foreground="red")
                        lastSearchPos = pos_end
                elif win[1].lower() == 'warning':
                    OutputController.config(state="normal")
                    OutputController.insert('end', '[ ! ] ' + win[0] + '\n')
                    OutputController.config(state="disabled")
                    printlist = printlist + 1
                    OutputController.yview('end')
                    
                    if not lastSearchPos:
                        pos_start = OutputController.search('[ ! ] ' + win[0], '1.0', 'end')
                        offset = '+%dc' % len('[ ! ] ' + win[0])
                        pos_end = pos_start + offset
                        OutputController.tag_add(f"warn{store_dataval}", pos_start, pos_end)
                        OutputController.tag_config(f"warn{store_dataval}", background="black", foreground="yellow") 
                        lastSearchPos = pos_end
                    else:
                        pos_start = OutputController.search('[ ! ] ' + win[0], lastSearchPos, 'end')
                        offset = '+%dc' % len('[ ! ] ' + win[0])
                        pos_end = pos_start + offset
                        OutputController.tag_add(f"warn{store_dataval}", pos_start, pos_end)
                        OutputController.tag_config(f"warn{store_dataval}", background="black", foreground="yellow")
                        lastSearchPos = pos_end
                else:
                    OutputController.config(state="normal")
                    OutputController.insert('end', win[0] + '\n')
                    OutputController.config(state="disabled")
                    printlist = printlist + 1
                    OutputController.yview('end')
            
    def ProcessCommand(Command=None,OutputController=None):
        global lastcmd
        global result
        global InVarEdit
        lastcmd = Command
        if Command != '':
            Window.Output([f'> {str(Command)}','msg'],OutputController,False)
            
            # Stop obvious crash commands (until i find a working method)
            try:
                if '{some random text for testing}' in Command.lower():
                    Window.Output([f'This command has been disabled due to pyCommand not being able to handle it','error'],OutputController,False)
                    return
                elif 'explorer.exe' in Command.lower():
                    Window.Output([f'This command has been disabled due to pyCommand not being able to handle it','error'],OutputController,False)
                    return
                elif 'netsh' in Command.lower():
                    Window.Output([f'This command has been disabled due to pyCommand not being able to handle it','error'],OutputController,False)
                    return
            except Exception as err:
                print(err)
             
            # Default py Commands
            try:
                if Command.lower() == 'cls' and not InVarEdit:
                    Menu.Clear(Output)
                    #OutputController.config(state="normal")
                    #OutputController.delete('1.0','end')
                    #OutputController.config(state="disabled")
                    return 'Cleared'
                elif 'start' in Command.lower() and not InVarEdit:
                    try:
                        module = importlib.import_module(f'mods.{Command.split("start", 1)[1].lstrip()}')

                        if hasattr(module, 'Configuration'):
                            if module.Configuration['HasKeyBinds']:
                                Window.Output([module.Configuration['Binds'],'msg'],OutputController,False)
                                # wait if we have keybinds.
                                var = tk.IntVar()
                                ConsoleWindow.after(3000, var.set, 1)
                                ConsoleWindow.wait_variable(var)
                            
                            if hasattr(module, 'Start'):
                                module.Start()
                            else:
                                Window.Output(['This module could not start due to a missing Start function.','error'],OutputController,False) 
                        else:
                            Window.Output(['This module could not start due to a missing Configuration.','error'],OutputController,False)
                    except Exception as err:
                        Window.Output([str(err),'warning'],OutputController,False)
                        
                    
                    return
                elif 'pyhelp' in Command.lower():
                    split = Command.split("pyhelp", 1)[1].lstrip()
                    
                    if split == '':
                        Window.Output([f'PLAY      Play a song in the assets/sounds\nFETCH      Fetch raw data from a site\nREADIMG      Read the bytes of an image','msg'],OutputController,False)
                    
                    return
                elif 'play' in Command.lower():
                    split = Command.split("play", 1)[1].lstrip()
                    
                    try:
                        play = threading.Thread(target=playsound.playsound, args=(f"./assets/sounds/{Command.split('play', 1)[1].lstrip()}.mp3", True))
                        play.start()
                        Window.Output([f'Playing sound/song {Command.split("play", 1)[1].lstrip()}.mp3','msg'],OutputController,False)
                        #playsound.playsound(f"assets/sounds/{Command.split('play', 1)[1].lstrip()}.mp3", True)
                    except Exception as err:
                        Window.Output([str(err),'error'],OutputController,False)
                        
                    return
                elif 'fetch' in Command.lower():
                    split = Command.split('fetch', 1)[1].lstrip()
                    
                    Menu.PyCmdDedicated.fetch(split)
                    
                    return
                elif 'readimg' in Command.lower():
                    split = Command.split('readimg', 1)[1].lstrip()
                    
                    Menu.PyCmdDedicated.read_image(split)
                    
                    return

                
                    
                
                                
                                          
                                          
                                          
                
                if not InVarEdit:   
                    f = threading.Thread(target=Window.RunCommand(Command,ConsoleWindow)).start()
                    #Window.RunCommand(Command,ConsoleWindow)

                if result and not InVarEdit:
                    Window.Output([result,'msg'],OutputController,False)
                else:
                    if InVarEdit:
                        Window.Output([Command + ' is not a valid var command.','error'],OutputController,False)
                    else:
                        Window.Output([Command + ' is not recognized as an internal or external command, operable program or batch file','error'],OutputController,False)
                    return
            except Exception as err:
                return
                    #Window.Output([Command + ' is not recognized as an internal or external command, operable program or batch file','error'],OutputController,False)
        else:
            Window.Output(['Command can\'t be empty or NoneType','warning'],OutputController,False)
            
            
            

    def CheckCharacterLength(textbox=None,OutputController=None):
        global replace_max
        if len(textbox.get()) == 100:
            textbox.delete(0, 'end')
            textbox.insert(0,replace_max)
            Window.Output(['Limit 100 Characters.','warning'],OutputController,False)
        else:
            replace_max = textbox.get()

    def RunCommand(Command,ConsoleWindow):
        global result
        result = os.popen(Command).read().strip()
        
            
            
class Menu:
    
    class PyCmdDedicated:
        
        def fetch(urlMain=None):
            if urlMain:
                urlresult = urllib.request.urlopen(url=urlMain).read().decode().strip()
                Window.Output([urlresult,'msg'],Output,False)
        
        def read_image(file_path=None):
            print('no')
            with open(file_path, "rb") as file:
                image_bytes = file.read()
            print(image_bytes)
            Window.Output([str(image_bytes),'msg'],Output,False)
    
    def New(window):
        window.destroy()
        Window.Console()
        
    def Clear(window):
        global lastSearchPos
        lastSearchPos = 0
        window.config(state="normal")
        window.delete('1.0','end')
        window.config(state="disabled")
        
    def CheckForUpdates(shouldnotify=True):
        try:
            UpToDateVersion = urllib.request.urlopen(url='https://raw.githubusercontent.com/9ekt/pyCommand/main/Details/Version.ver').read().decode().strip()
        except Exception as err:
            UpToDateVersion = 'No Internet Connection'
        
        if Version != UpToDateVersion:
            verify = messagebox.askyesno('pyCommand',f'Your pyCommand is out of date.\n\nWould you like to install the newest version?\n\nYour Version: {Version}\nNewest Version: {UpToDateVersion}')
            
            if verify:
                webbrowser.open('https://github.com/9ekt/pyCommand/releases')
        else:
            if shouldnotify:
                messagebox.showinfo('pyCommand','Your pyCommand is up to date')

    def UpdateClient():
        webbrowser.open('https://github.com/9ekt/pyCommand/releases')
        
    def Credits():
        webbrowser.open('https://github.com/9ekt/pyCommand')
        
    def Settings():
        return
    
    def DisplayMods(OutputController=None):
        Menu.Clear(OutputController)
        #messagebox.showinfo('Mods', '(testing)')
        Window.Output(['Current mods found in your mods directory','msg'],OutputController,False)
        try:
            for path in os.listdir("mods"):
                if os.path.isfile(os.path.join("mods", path)):
                    if os.path.getsize(os.path.join("mods", path)) > 0:
                        Window.Output([str(path),'msg'],OutputController,False)
                    else:
                        messagebox.showerror(f'mods/{path}', f'The following file returned {str(os.path.getsize(os.path.join("mods", path)))} bytes. This file will not work with "start {path.split(".", 1)[0]}" until this is corrected.')
        except Exception as err:
            messagebox.showerror('Critical Error from DisplayMods', str(err))
            
    def RetrieveVariables(lookingfor=None):
        try:
            if os.path.exists('var.data') and lookingfor:
                varFile = open('var.data', 'r')
                Lines = varFile.readlines()
 
                # Strips the newline character
                for line in Lines:
                    fline = line.strip()
                
                    split = fline.split(': ')
                    var = split[0]
                    value = split[1]
                    print(var, value)
                    if var.lower() == lookingfor.lower():
                        return value
        except Exception as err:
            messagebox.showerror('Critical Error from RetrieveVariables', str(err))
            exit()
        
    def PromptModsFolder():
        os.startfile("mods")
        
    def SaveVariables(): #todo
        varFile = open("var.data", "a")
        varFile.close()
        
    def GetMods():
        if not os.path.exists('mods'):
            return None
        
        global Mods
        Mods = 0
        try:
            for path in os.listdir("mods"):
                if os.path.isfile(os.path.join("mods", path)):
                    if os.path.getsize(os.path.join("mods", path)) > 0:
                        Mods += 1
                    else:
                        messagebox.showerror(f'mods/{path}', f'The following file returned {str(os.path.getsize(os.path.join("mods", path)))} bytes. This file will not work with "start {path.split(".", 1)[0]}" until this is corrected.')
        except Exception as err:
            messagebox.showerror('Critical Error', 'pycmd can not run due to a missing mods folder.\nWas this a spelling mistake?')
            exit(0)
                
        return Mods


# Mod compatibility with sending and recieving data.
async def handler(websocket, path):
 
    data = await websocket.recv()

    print(f'[INCOMING] {data}')
    
    reply = f"Data recieved as:  {data}"
    await websocket.send('yes')
    await websocket.close()
    
    Data = json.loads(data)

    
    try:
        if Data['request'] and Data['message'] and Data['errtype']:
            if Data['request'] == 'ui':
                Window.Output([Data['message'],Data['errtype']],Output,False)
    except Exception as err:
        print(err)
        messagebox.showerror('Critical Error from Mod Communication Handler', err)
            

 
# Mod compatibility
def CreateWebhookServer():
    try:
        start_server = websockets.serve(handler, "localhost", 8000)
    
 
        asyncio.get_event_loop().run_until_complete(start_server)
    
        print('Server Startup success')
        
        asyncio.get_event_loop().run_forever()
    except Exception as err:
        if Mods > 0:
            messagebox.showwarning('Warning from Mod Communication Handler', f'Mod Compatibility failed, mods will NOT be able to communicate with pyCommand.\n\n[{err}]')

    
            
                

    
# Pycmd variables    
Mods = 0
printlist = 1
lastSearchPos = 0
replace_max = ''
lastcmd = ''
result = None
InVarEdit = False


## Windows Settings
Output_Variable = None
ConsoleWindow = None
Output = None
Input = None

# Var edit Config Settings
Resolution = Menu.RetrieveVariables('Resolution') or '700x450'
MinSize = Menu.RetrieveVariables('ResolutionMin') or {'x':700,'y':450} # TODO: Allow this to be changable. (can be changed by hard editing your var.data file)
tkWinBackground = Menu.RetrieveVariables('tkWinBackground') or 'Black'
EntryInputColor = Menu.RetrieveVariables('EntryInputColor') or 'Black'


try:
    UpToDateVersion = urllib.request.urlopen(url='https://raw.githubusercontent.com/9ekt/pyCommand/main/Details/Version.ver').read().decode().strip()
except Exception as err:
    UpToDateVersion = 'No Internet Connection'

Version = 'v1.0.0'
BootText = f'Thanks for using pyCommand ({Version})\n\nrun "help" to view possible commands\nrun "pyhelp" for pyCommands' + '\n'    

if __name__ == '__main__':
    try:
        Menu.GetMods()
        
        serv = threading.Thread(target=Window.Console)
        serv.start()
        
        CreateWebhookServer()
        

        #Window.Console()
        
    except Exception as err:
        messagebox.showerror('Critical Error', f'There was an issue loading the console:\n{str(err)}')
        #print('Error > Booting Console: ' + str(err))
        


