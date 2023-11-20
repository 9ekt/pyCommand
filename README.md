# pyCommand

Hello friends👋, If your thinking about using pyCommand please follow the [Setup](#Setup) and check out the [Commonly asked questions](#commonly-asked-questions) if your confused or curious.

The most common problems are:
  - [pyCommand wont start](#my-pycommand-wont-start)

# Commonly asked questions

### What is pyCommand?
pyCommand is a solo project that was originally created to be a replica of command prompt with extra features, I originally started working on this project when I was still fairly new to [Python](https://www.python.org/) About over 3 years ago, I actually forgot about this project on my USB for quite some time 😅 but I'm moving back onto this project.

### Whats the point of pyCommand?
Theres multible points for pyCommand, for a start its fast and effiencent ensuring your not going to get unexpected lag or crashes. for example running `dir/s` in normal command prompt it takes acouple of seconds to list your directories while pyCommand will spit it out to you all in one go allowing you to quickly find what your looking for, not only does it do that it also includes a search feature triggered with `Ctrl + F` this will bring up PyCommands search feature, making finding what you need with lots of output a dream.

### What were those extra features you mentioned?
Not only does pyCommand support basic command prompt features, it supports the ability to fully customise it with mods, yes you heard me mods for a command prompt replica, this opens it up to alot more possibilities such as creating games, extra features, and customising the UI design. These modifications can be easily distributed to friends and the community. Thats not all pyCommand has an update check in place to ensure you are always on the latest version and are enjoying them sweet features. 

### Where do I put my mods?
pyCommand natively supports mods but keeps it hidden 👀, in the same directory as `pyCommand.py` or `pyCommand.exe` you'll need to create a `mods` folder the folders name must be all lowercase and must include the sneaky `s` at the end, else pyCommand will not recognise this folder. If your mod includes and errors or problems pyCommand will catch those pesky errors and display them to your pyCommand display, not only does this make debugging more efficient it also allows you to update and save the file without restarting pyCommand once.

### My mods arent being detected
Make sure your mod has more than `0 bytes of size` else pyCommand will assume its a useless file and skip it, if it has more than `0 bytes` and pyCommand still is not detecting it, check to make sure your folder is [correct](#where-do-i-put-my-mods).

### My pyCommand wont start
Make sure you've included the `assets` folder in the same directory as `pyCommand.py` or `pyCommand.exe` the assets folder is used to store `mod` addons and core pyCommand icons. Without this, pyCommand wont even attempt to start so make sure you've included this.

### I'm getting an error with importing a module
If this error is appearing when you are starting pyCommand then you have an out of date python version, all packages are default within pythons instalation but some imports used only become a default package around 3.5~ thats why your python version is required to be 3.10+


# Setup

### Requirements
  - Python 3.10 or later
  - Windows OS / Mac Device (Might work has not been tested)
  - Basic Knowledge on [Python](https://www.python.org/) if you'd like to create mods.

### First things first, lets download pyCommand.
With this it will download the entire repository, but the main folder we need will be `PyCmd`
![howtodownload](https://github.com/9ekt/pyCommand/assets/129973190/b3bcf9ec-714a-41b5-b3d7-0e7bc5982f1b)

### Extrating and using pyCommand
Your folder should look like this.
![image](https://github.com/9ekt/pyCommand/assets/129973190/5562f8db-7569-47cb-9ae9-da6284b73ef5)

You can simply move the PyCmd folder to your desktop or anywhere you'd like, and thats it your done simply run `pyCommand.py` to use.



# 


