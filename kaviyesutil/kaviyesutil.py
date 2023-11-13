# Author Karl Vince Reyes (Kaviyes)
'''
## KAVIYESUTIL
### Version 2.0.1 Standard Kaviyes utility for python
A standard kaviyes utility for python thats ideal for small projects and prototypes.

----

Check documentations [here!](https://github.com/Kaviyes/kaviyesutil)

'''

from getpass import getpass as _getpass
from time import sleep as _sleep
import os as _os
import datetime as _datetime
import sys as _sys

def printc(
        text: object = "",
        textColor: str = "default",
        highlightColor: str = "default",
        *formats,
        returnText: bool = False,
        sep: str = None,
        end: str = "\n",
):
    '''
    ### printc
    #### an easy way to customize your text
    
    ---

    Available colors
    - black
    - red
    - green
    - yellow
    - blue
    - magenta
    - cyan
    - white

    Available formats
    - bold
    - italic
    - underlined
    - strikethrough

    #### Examples
    ```
    printc('Hello Kaviyes!', 'red', 'magenta')
    print(printc('Hello Kaviyes!', 'red', 'magenta', True))
    
    printc('Hello Kaviyes!', 'red', 'magenta', 'bold', 'italic')
    print(printc('Hello Kaviyes!', 'red', 'magenta', 'bold', 'italic', ReturnText='True'))
    ```

    ---

    #### Notes
    - Colors may seem like its not affected but its completely terminal dependent.
    - Some functions will be overridden when returnText is true.
    '''
    
    TextCode = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'default': '39',
        'reset': '0'
    }

    HighlightCode = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
        'default': '49',
        'reset': '0'
    }

    FormatCode = {
        'bold': ';1',
        'italic': ';3',
        'underlined': ';4',
        'strikethrough': ';9'
    }

    FinalText = f"\033[{TextCode.get(textColor, '39')}"

    if highlightColor != 'default':
        FinalText += f";{HighlightCode.get(highlightColor, '49')}"

    for formatoption in formats:
        if formatoption in FormatCode:
            FinalText += FormatCode[formatoption]

    FinalText += f'm{text}\033[0m'


    if returnText:
        return FinalText
    else:
        print(FinalText,sep=sep ,end=end)

def countdown(seconds, echo: str = None, endMessage: str = 'Countdown Complete!'):
    '''
    ### [Experimental] Countdown
    #### A verbose countdown timer

    ---

    #### Example
    ```
    countdown(10,'Timer: ' ,'Timer complete!')
    ```
    '''
    if echo:
        while seconds:
            if seconds < 60:
                timer = '{:02d}'.format(seconds)
            elif seconds < 3600:
                mins, secs = divmod(seconds, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
            else:
                hours, remainder = divmod(seconds, 3600)
                mins, secs = divmod(remainder, 60)
                timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

            print(f'{echo}{timer}', end="\r")
            _sleep(1)
            seconds -= 1
    
    if not echo:
        while Seconds:
            if Seconds < 60:
                timer = '{:02d}'.format(Seconds)
            elif Seconds < 3600:
                mins, secs = divmod(Seconds, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
            else:
                hours, remainder = divmod(Seconds, 3600)
                mins, secs = divmod(remainder, 60)
                timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

            print(f'{timer}', end="\r")
            _sleep(1)
            Seconds -= 1
    if endMessage in [' ', '', None]:
        print('Countdown Complete!')
    elif endMessage == 'empty':
        print('   ')
    else:
        print(endMessage)

def cloakedLink(text, url, Print: bool = False):
    '''
    ### CloakedLink
    #### create a visually appealing links

    ---

    #### Examples
    ```
    cloakedLink('visit kaviyes on github!', 'https://github.com/Kaviyes', True)
    print(cloakedLink('visit kaviyes on github!', 'https://github.com/Kaviyes'))
    cloakedLink(printc('Visit Kaviyes on Github!', 'cyan', 'default', 'underlined', ReturnText=True), 'https://github.com/Kaviyes', Print=True)
    ```
    '''
    if Print:
        print(f"\033]8;;{url}\033\\{text}\033]8;;\033\\")
    else:
        return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def resourcePath(relative_path):
    #Credits to max & community
    '''
    ### ResourcePath
    #### Get absolute path to resource, works for dev and for PyInstaller

    ---

    #### Notes

    - Credits to [max & Stackoverflow Community!](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741)

    '''
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = _sys._MEIPASS
    except Exception:
        base_path = _os.path.abspath(".")

    return _os.path.join(base_path, relative_path)

def generateCustomID(format: object = None, length: int = 0, type: str = None):
    '''
    #### Standrd Formats
    - STD
      - 08
      - 16
      - 32
    -----
    #### Example:
    - generateCustomID('STD08')
        - Output: 5MVI4OA1
    -----
    #### Standard Custom Length
    - Types
        - "all" (A-Z , a-z , 0-1 | Note: This does not include special characters)
        - "standard" (A-Z , 0-1 | Uppercase and digits only)
        - "digits" (0-1)
    -----
    #### Examples:
    - generateCustomID(Length="8", Type="standard")
    - generateCustomID(Length="8")
        - Output: U1BOQFQ2
    - generateCustomID(Length="8", Type="all")
        - Output: SUu0RKF1
    - generateCustomID(Length="8", Type "digits")
    - generateCustomID(Length="8", Type "digit")
        - Output: 92621248
    -----
    #### Custom Format
    - Formats
        - A = Uppercase letter A-Z
        - a = Lowercase letter a-z
        - $ = Custom Characters
        - 0 = Digits 0-9
    -----
    #### Examples:
    - generateCustomID('AA00aa$$')
        - Output: JQ53mx*@

    - generateCustomID('aA$0')
        - Output: hR%0
    -----
    #### NOTE: Using "Length" will override "Format"
    -----
    '''
    import random
    import string

    id_characters = {
        'A': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'a' :'abcdefghijklmnopqrstuvwxyz',
        '$': '!@#$%^&*()_+-=[]{}|;:,.<>?',
        '0': '0123456789'
    }

    _STANDARD = string.ascii_uppercase + string.digits
    _ALL = string.ascii_letters + string.digits

    if length:
        if type in [None, 'standard']:
            return ''.join(random.choices(_STANDARD, k=length))
        elif type in ['digit' ,'digits']:
            return ''.join(random.choices(string.digits, k=length))
        elif type == 'all':
            return ''.join(random.choices(_ALL, k=length))

    if format == 'STD08':
        return ''.join(random.choices(_STANDARD, k=8))

    if format == 'STD16':
        return ''.join(random.choices(_STANDARD, k=16))
    
    if format == 'STD32':
        return ''.join(random.choices(_STANDARD, k=16))

    if format:
        custom_id = ''
        for char in format:
            if char in id_characters:
                custom_id += random.choice(id_characters[char])
            else:
                custom_id += char

        return custom_id

def prompt(message: object = False, enableGetpass: bool = False, anyKey: bool = False):
    '''
    ### Prompt
    #### Prompts user with desired message

    ---

    #### Examples
    ```
    #default value / Waits until the user press enter
    prompt()

    #Pause until user press any key
    prompt(Anykey=True)

    #Add Desired message / Waits until the user press enter
    prompt('Hello Kaviyes!')
    ```
    '''

    if anyKey:
        EnableGetpass = False
        if _os.name == 'nt':
            import msvcrt

            if not message:
                print('Press any key to continue...')
            
            if message:
                print(message)

            msvcrt.getch()
            return

        else:
            EnableGetpass = False
            import sys, tty, termios

            if not message:
                print('Press any key to continue...')
            if message:
                print(message)
            sys.stdout.flush()
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return
    
    if not message:
        _getpass('Press Enter to continue...')
    if message:
        _getpass(message)

    if enableGetpass:
        userinput = _getpass(message)
        return userinput

def currentTime(format: str = None,format_24H: bool = True):
    '''
    ### CurrentTime
    #### A simplified version of datetime function

    ---

    #### Examples
    ```

    #Using own format
    currentTime('%H:%M:%S')

    #Printing the results
    time = currentTime('%H:%M:%S')
    print(time)
    or
    print(currentTime('%H:%M:%S'))

    #quick preset
    currentTime(Format_24H=True) # its true by default
    ```
    '''
    
    now = _datetime.datetime.now()

    if format:
        return now.strftime(format)

    if not format_24H:
        return now.strftime('%I:%M:%S %p')
    if format_24H:
        return now.strftime('%H:%M:%S')

def delay(secs: float):
    '''
    ### delay
    #### a delay function / This function is from time.sleep()

    ---

    #### Example
    ```
    delay(1) # delays for 1 second
    ```
    '''

    _sleep(secs)

def decodeHex(value : str, reversed : bool = False):
    '''Decodes Hex into String'''
    stage1 = bytes.fromhex(value)
    stage2 = stage1.decode('utf-8')

    if reversed == False:
        return stage2
    elif reversed == True:
        stage3 = stage2[::-1]
        return stage3

def encodeHex(value : str, reversed : bool = False):
    '''Converts something to Hex (Old code but usefull sometimes)'''
    if reversed == False:
        stage1 = hex(int.from_bytes(value.encode(), 'big'))
        stage2 = str(stage1)
        stage3 = stage2.replace('0x', '')
        return stage3
    elif reversed == True:
        stage1 = hex(int.from_bytes(value.encode(), 'little'))
        stage2 = str(stage1)
        stage3 = stage2.replace('0x', '')
        return stage3

def terminal(command):
    '''
    ### Terminal
    #### a quick access to terminal / os.system()

    ---

    #### Examples
    ```
    terminal('echo Hello Kaviyes!') #Outputs Hello Kaviyes! to terminal
    terminal('title Kaviyesutil') #Sets terminal window title
    ```
    '''
    _os.system(command)

def cter(message: object = ""):
    '''Clears the contents of the terminal screen'''
    if message:
        _os.system('cls' if _os.name == 'nt' else 'clear')
        print(message)
    else:
        _os.system('cls' if _os.name == 'nt' else 'clear')

