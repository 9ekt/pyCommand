# You can import modules here or anywhere in your code.
try:
    import sys
    import time
    import asyncio
    import importlib
    # Apparently this append bit makes it so python doesnt have a moment.
    ws = sys.path.append("..")
    from src.modules import websockets
    import socket
    import os
    import json
except ImportError as err:
    print(err)

Configuration = {
    'HasKeyBinds' : False,
    'Binds' : 'p + j', # if you have key binds for your mod include them here.
}

# This is required to send data to pyCmd if you edit any of this pyCmd will NOT recieve data.

class MyMod:
    
    def __init__(self, content) -> str:
        if content:
            self.content = content
            
            # lets say you want to send a message to pyCmds visual screen you would do:
            # errtype can be one of these three: [msg, warning and error] these all display differently
            # on the pyCmd UI
            data = {
                'request': 'ui',
                'message': 'Welcome to this very coooool example mod for pyCommand.',
                'errtype': self.content
            }
            
            coro = MyMod.listner(json.dumps(data))
            asyncio.run(coro)
            
            
    
    # This function will be how you send data back to pyCmd for a UI experience.
    # Lets say you want text to display, you'd communicate with this.
    # I recommending threading this, for obvious reasons.
    async def listner(r):
        async with websockets.connect(f'ws://localhost:8080') as wb:
            await wb.send(r)
            response = await wb.recv()
            print(response)
            
            # You can use this simple if statement to check wether pyCommand approved
            # if you dont get anything pyCommand simply didnt recieve it. (py command will most likely silent crash)
            if response == 'yes':
                pass # or do your code here.
            
            # You dont neeeeeeed this part but its nice for debugging
            #print(response)


    
            
        
        
        
def Start():
    MyMod('error')

# We prevent launches from just double clicking the module
# this isnt needed but its helpful in a way atleast for me lol
if __name__ == '__main__':
    print('no')