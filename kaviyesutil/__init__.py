#Kaviyes
'''
## kaviyesutil
### [Experimental] Version 0.1.4 Standard Utility

A toolkit often used with Kaviyes related projects, Its also ideal for small projects.

-----
### List of available functions:
    - Countdown
    - GenerateCustomID
    - Terminal
    - cter
    - Prompt
    - Today
    - CurrentTime
    - sleep
    - Decodefromhex
    - Encodetohex
    - CleanStart
'''

import getpass as _getpass
import os as _os
import datetime as _datetime
import time as _time

___kaviyes_UTILversion___ = '0.1.4'
___kaviyes_UTILversionFull____ = 'Version 0.1.4 (September 2023)'

def Countdown(Seconds, Echo: str = None, EndMessage: str = 'Countdown Complete!'):
    """
    ### [Beta] Countdown
    ---
    #### Countdown from designated seconds.
    ---
    Examples
    ####  Countdown(Seconds=10)
          *Countdowns from 10 seconds*

    ####  Countdown(Seconds=9, Echo="HelloThere!: ")
          Output while countdown HelloThere!: 09

    ####  Countdown(Seconds=8, Echo="Part3: ", EndMessage="Countdown finished!!")
          Output while countdown "  Part3: 08  " | After countdown is finished it will print "  Countdown finished!!  "

    #### Countdown(Seconds7, Echo="Cat!!: ", EndMessage="empty")
          Output after countdown will be nothing
    """
    if Echo:
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

            print(f'{Echo}{timer}', end="\r")
            _time.sleep(1)
            Seconds -= 1
    
    if not Echo:
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
            _time.sleep(1)
            Seconds -= 1
    if EndMessage in [' ', '', None]:
        print('Timer Complete!')
    elif EndMessage == 'empty':
        print('   ')
    else:
        print(EndMessage)


def GenerateCustomID(Format: object = None, Length: int = 0, Type: str = None):
    '''
    #### Standrd Formats
    - STD
      - 08
      - 16
      - 32
    -----
    #### Example:
    - GenerateCustomID('STD08')
        - Output: 5MVI4OA1
    -----
    #### Standard Custom Length
    - Types
        - "all" (A-Z , a-z , 0-1 | Note: This does not include special characters)
        - "standard" (A-Z , 0-1 | Uppercase and digits only)
        - "digits" (0-1)
    -----
    #### Examples:
    - GenerateCustomID(Length="8", Type="standard")
    - GenerateCustomID(Length="8")
        - Output: U1BOQFQ2
    - GenerateCustomID(Length="8", Type="all")
        - Output: SUu0RKF1
    - GenerateCustomID(Length="8", Type "digits")
    - GenerateCustomID(Length="8", Type "digit")
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
    - GenerateCustomID('AA00aa$$')
        - Output: JQ53mx*@

    - GenerateCustomID('aA$0')
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

    if Length:
        if Type in [None, 'standard']:
            return ''.join(random.choices(_STANDARD, k=Length))
        elif Type in ['digit' ,'digits']:
            return ''.join(random.choices(string.digits, k=Length))
        elif Type == 'all':
            return ''.join(random.choices(_ALL, k=Length))

    if Format == 'STD08':
        return ''.join(random.choices(_STANDARD, k=8))

    if Format == 'STD16':
        return ''.join(random.choices(_STANDARD, k=16))
    
    if Format == 'STD32':
        return ''.join(random.choices(_STANDARD, k=16))

    if Format:
        custom_id = ''
        for char in Format:
            if char in id_characters:
                custom_id += random.choice(id_characters[char])
            else:
                custom_id += char

        return custom_id

def Prompt(Message, EnableGetpass: bool = False):
    '''
    It is to mimic keyboard disabled feature but in reality its not, It uses getpass
    '''

    if EnableGetpass:
        userinput = _getpass.getpass(Message)
        return userinput

    _getpass.getpass(Message)

def CurrentTime(Format: str = None,Format_24H: bool = True):
    '''
    Returns Current Time, With "Format" default format will be overridden with your own defined format
    '''
    
    now = _datetime.datetime.now()

    if Format:
        return now.strftime(Format)

    if not Format_24H:
        return now.strftime('%I:%M:%S %p')
    if Format_24H:
        return now.strftime('%H:%M:%S')

def sleep(secs: float):
    '''
    (  Code imported from time.sleep  )

    sleep(seconds)

    Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.

    '''
    _time.sleep(float)

def Decodefromhex(Value : str = None, Reversed : bool = False):
    '''Decodes Hex into String'''
    stage1 = bytes.fromhex(Value)
    stage2 = stage1.decode('utf-8')

    if Reversed == False:
        return stage2
    elif Reversed == True:
        stage3 = stage2[::-1]
        return stage3

def Encodetohex(Value : str = None, Reversed : bool = False):
    '''Converts something to Hex (Old code but usefull sometimes)'''
    if Reversed == False:
        stage1 = hex(int.from_bytes(Value.encode(), 'big'))
        stage2 = str(stage1)
        stage3 = stage2.replace('0x', '')
        return stage3
    elif Reversed == True:
        stage1 = hex(int.from_bytes(Value.encode(), 'little'))
        stage2 = str(stage1)
        stage3 = stage2.replace('0x', '')
        return stage3

def Today():
    '''Returns the current date (DAY.MONTH.YEAR)'''
    now = _datetime.datetime.now()
    return (now.strftime('%d.%m.%y'))

def Terminal(Command):
    '''Oh look a quick access to terminal'''
    _os.system(Command)

def cter():
    '''Clears the terminal'''
    _os.system('cls' if _os.name == 'nt' else 'clear')

def RevealUtilVersion(Args: str = None):

    '''
    - 'get' = returns version info
    
    - 'getFull' = returns detailed version info
    '''

    if Args == 'get':
        return ___kaviyes_UTILversion___
    elif Args == 'getFull':
        return ___kaviyes_UTILversionFull____
    else:
        return ___kaviyes_UTILversion___

def CleanStart(Args: int = 4, Value: str = None, Highlight: bool = True):
    '''
    Cleans terminal and display the creator signature (I added some cool highlight into it)

    Args Values (INT):
    
        - 0 = Nothing

        - 1 = Custom (    With Value Example Cleanstart(1, 'Anything')    )

        - 2 = KaviyesLabs

        - 3 = Kaviyes

        - 4 = KaviyesUtilities

    [It does not serve an actual purpose its just for branding]
    '''
    _os.system('cls' if _os.name == 'nt' else 'clear')
    if Args == 0:
        signature = False
    elif Args == 4:
        signature = 'Kaviyes Utilities'
    elif Args == 2:
        signature = 'KaviyesLabs'
    elif Args == 3:
        signature = 'Kaviyes'
    elif Args == 1:
        signature = Value

    if not signature: return

    if Highlight:
        print(f'\033[30;47m{signature}\033[0m\n')
    
    if not Highlight:
        print(signature, '\n')