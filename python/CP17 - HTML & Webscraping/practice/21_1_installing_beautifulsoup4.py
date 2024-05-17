# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

from bs4 import BeautifulSoup
import requests


'''
FIRST:
    Try running this code. You're probably going to get an error.
    This is because psycopg2 and sqlalchemy are libraries that you need to download from the internet.

HOW TO DOWNLOAD LIBRARIES:
    Python comes installed with a package/library downloader called pip!

    1. In VS Code, go to Terminal > New Terminal (at the top of the screen)

    2. Then in the bottom Terminal window, type:
                pip install beautifulsoup4
                pip install requests
        and then hit the enter/return key. If that doesn't work, try:
                pip3 install beautifulsoup4
                pip3 install requests
    
    3. Then, try and run this python file again, if it prints out the message below, you are good.

    Note: If you prefer, you can also just run pip in the normal terminal application on Mac
            or the command line on Windows (or powershell). It doesn't have to be in VS Code.

IT STILL ISN'T WORKING FOR ME:

    1. Most likely, you are installing the package to one version of python, and then running a different version in 
        VS Code.

    2. Try clicking the numbers near the bottom right of your screen in VS Code and then select the version of python that
        says "Recommended" 
'''

print("If this prints, that means you installed beautifulsoup4 and requests correctly")