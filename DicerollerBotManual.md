# Diceroller Bot Manual

This is the Diceroller Bot manual. If you find any bug tell me on the [Issues page](https://github.com/AlmirPaulo/Diceroller_Bot/issues). 
For instructions about download and installation, see the [README.md](https://github.com/AlmirPaulo/Diceroller_Bot/blob/main/README.md) file. 

## GUI Version

<img src='https://github.com/AlmirPaulo/Diceroller_Bot/blob/main/diceroller.gif'></img>

Actually it's pretty intuitive to run the bot with this interface. There is just three windows: the first where you choose your browser (if it's Firefox or Chrome), the second with a step-by-step guide on how to proceed and a button (basically you need to wait till the browser launch, login on whatsapp web with the QR code and go to your RPG group where you to roll the dices) and the third and last one is where the thing really happens. 

## Terminal Version

I do not recommend this version unless you are one of (us) this computer nerds. Because in case you are not, you can be confused to handle that Bash black screen and you probably never write a single command line. If that is your case download the GUI (Graphic User Interface) version. 
But if you ok with the terminal...you still should use the GUI version, but if you really want, let's go.   

### Requirements
* A terminal emulator
* Python 3
* Internet Connection
* Webdrivers
* Selenium Python module

### Webdrivers?

It's a technology that allows to automatize the browser. If you use Firefox you need to download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and if you use Chrome you need download [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/). In Linux (probably it should work on Mac too) save it in "/usr/local/bin".

### Running the Bot on Command Line:
1. Run this command at the termminal:

    python3 diceroller.py

2. Choose your browser. Just type 1 for Firefox or 2 for Chrome.

3. Now yor browser is going to launch and acess Web Whatsapp. You need to login with the QR Code (there is an option on the mobile app to read the QR Code). 

4. Go to your RPG session group. The place where you want  to roll dices.

5. when the page were completelly loaded, type "go" in the terminal.

6. Now anytime you need to roll a dice type "roll xdy", where "x" is the amount of dices and "y" is the number of faces of the dice. e.g.: roll 2d6, will roll 2 dices of 6 faces.  

7. You can cancel the bot in any point with Ctrl+C.

## Possible Issues and Questions

**1. It would be better if it works on the mobile app!**

My bot uses Selenium to roll the dices, so it can't operate on an app, only on browsers. :unamused:

**2. The browser do not open!**

Make sure you selected a browser you really have installed on your machine. If you are using the terminal version, make sure you have the webdrivers on the correct folder. In any other cases maybe the problem is the version of your browser thats is not compatible with the bot webdrivers. 

**3. The pages do not load.**

The problem is probably your internet connection. Feel free to press F5 to reload the pages before start the bot. 

**4. I start the bot and a error has appear. Something about it doesn't find something...**

You need to be in the correct group you gonna roll the dices before start the bot, than make sure the page is completelly loaded. 

**5. What dices can I roll?**

All the common dices on RPG games: d2, d3, d4, d6, d8, d10, d12, d20 and d100.

**6. I think I find a bug.**

Show me on the [Issues page](https://github.com/AlmirPaulo/Diceroller_Bot/issues).
