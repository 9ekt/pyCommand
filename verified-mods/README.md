# pyCommand Mods

in this `README` I'll go over some questions and go into detail on how the mods here work and how to create your own!

I dont wanna read let me skip to these places:
  - [How to create mods (unfinished)]()
  - [Mod Information](#verified-mods-information)


## Are these mods safe?
Yes! All mods are open source and checked before uploading them here, if you do download and use a mod thats not present in this folder than please make sure you double check its code before starting that module in `pyCmd`, if something sounds too good to be true it most likely is.

## Where do I put my mods?
pyCommand natively supports mods but keeps it hidden 👀, in the same directory as `pyCommand.py` or `pyCommand.exe` you'll need to create a `mods` folder the folders name must be all lowercase and must include the sneaky `s` at the end, else pyCommand will not recognise this folder. If your mod includes and errors or problems pyCommand will catch those pesky errors and display them to your pyCommand display, not only does this make debugging more efficient it also allows you to update and save the file without restarting pyCommand once.

## My mods arent being detected
Make sure your mod has more than `0 bytes of size` else pyCommand will assume its a useless file and skip it, if it has more than `0 bytes` and pyCommand still is not detecting it, check to make sure your folder is [correct](#where-do-i-put-my-mods).

## I'm getting an error running my mod
Please check the requirements section for the mod you are attempting to you. 9 times out of 10 its an image or required module you're missing.

For any addon modules you need to place them in the `assets/modules` directory.

For any images you need to place them in the `assets/img` directory.


# Verified Mods Information
In this section I will go over the `verified mods`, what they do in detail and how you can use them in your `pyCmd`. This section will also include the author, keybinds, modules used and total lines.

## win10bsod.py

__Author__: [Preston (9ekt)](https://github.com/9ekt)

__Description__: win10bsod is a `pyCmd` addon/mod that adds the ability to emulate a fake windows 10 blue screen (bug check), This addon will create a `tkinter window` with the style, colors and font of the real windows 10 bug check screen. win10bsod will also count up the percent complete to continue to sell the idea of a real bug check screen. If it reaches it will restart your pc by running a os command `shutdown /s /t 0` (you can remove this if you'd like to). You can view this os command yourself [here](https://github.com/9ekt/pyCommand/blob/5d4895151cbb698ac1552b581ad12ad5671663c3/verified-mods/win10bsod.py#L125C24-L125C40).

__Keybinds__: S + P to close win10bsod.


__Modules Used__: 
  - tkinter as tk (+including messagebox)
  - math
  - random
  - time
  - ctypes
  - os

__Requirements__:
  - [QR Image](https://github.com/9ekt/pyCommand/blob/main/verified-mods/img/qr.png) (QR code is a rickroll link)

__Screenshot of addon__:
![image](https://github.com/9ekt/pyCommand/assets/129973190/44b89fd2-55b7-48cd-9516-0379ef9cdee1)




