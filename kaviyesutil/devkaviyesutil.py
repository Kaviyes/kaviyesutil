#Kaviyes
'''
## kaviyesutil
### [Experimental] Version 0.1.5 Standard Utility

A toolkit often used with Kaviyes related projects, Its also ideal for small projects.

-----
### List of available functions:
    - FancyText
    - ConvertUnits
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

___kaviyes_UTILversion___ = '0.1.5'
___kaviyes_UTILversionFull____ = 'Version 0.1.5 (September 2023)'



def FancyText(Text: str = '', TextColor: str = 'default', HighlightColor: str = 'default', ReturnText: bool = False):
    '''
    ### FancyText
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

    #### Examples
    ```
    FancyText('Hello Kaviyes!', 'red', 'magenta')
    print(FancyText('Hello Kaviyes!', 'red', 'magenta', True))
    ```

    ---

    #### Notes
    - Colors may seem like its not affected but its completely terminal dependent
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

    if HighlightColor == 'default':
        FinalText = f"\033[{TextCode.get(TextColor, '39')}m{Text}\033[0m"
    if HighlightColor:
        FinalText = f"\033[{TextCode.get(TextColor, '39')};{HighlightCode.get(HighlightColor, '49')}m{Text}\033[0m"

    if ReturnText:
        return FinalText
    else: 
        print(FinalText)

def ConvertUnits(value, from_unit, to_unit, Precise: bool = False):
    '''
    ### [Experimental] ConvertUnits
    #### a quick unit conversation function
    
    ---

    Available Units
    - kilometer
    - meter
    - feet
    - inches

    #### Examples
    ```
    Converted = ConvertUnits(1000, 'kilometer', 'meter', False)
    print(ConvertUnits(1000, 'kilometer', 'meter', False))
    ```

    ---

    #### Notes
    - This is an experimental, function I don't suggest to use this for big projects
    - This function is not that precise
    '''

    meter_to_feet = 3.28084
    meter_to_inches = 39.3701
    meter_to_kilometer = 0.001
    kilometer_to_meter = 1000
    feet_to_meter = 1 / meter_to_feet
    inches_to_meter = 1 / meter_to_inches
    feet_to_kilometer = 0.0003048  # Adjusted value for feet to kilometer

    # Ensure input units are lowercase for case-insensitive comparison
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Check if the units are valid
    valid_units = ['meter', 'feet', 'inches', 'kilometer']
    if from_unit not in valid_units or to_unit not in valid_units:
        return "Invalid units. Please use 'meter', 'feet', 'inches', or 'kilometer'."

    # Perform the conversion
    if from_unit == to_unit:
        return round(value, 3) if not Precise else value

    if from_unit == 'meter':
        if to_unit == 'feet':
            result = value * meter_to_feet
        elif to_unit == 'inches':
            result = value * meter_to_inches
        elif to_unit == 'kilometer':
            result = value * meter_to_kilometer
    elif from_unit == 'feet':
        if to_unit == 'meter':
            result = value * feet_to_meter
        elif to_unit == 'inches':
            result = value * meter_to_inches * feet_to_meter
        elif to_unit == 'kilometer':
            result = value * feet_to_kilometer
    elif from_unit == 'inches':
        if to_unit == 'meter':
            result = value * inches_to_meter
        elif to_unit == 'feet':
            result = value * feet_to_meter
        elif to_unit == 'kilometer':
            result = value * inches_to_meter * meter_to_kilometer
    elif from_unit == 'kilometer':
        if to_unit == 'meter':
            result = value * kilometer_to_meter
        elif to_unit == 'feet':
            result = value * kilometer_to_meter * meter_to_feet
        elif to_unit == 'inches':
            result = value * kilometer_to_meter * meter_to_inches
    else:
        return "Conversation failed. [Not supported]"

    return round(result, 3) if not Precise else result

def Countdown(Seconds, Echo: str = None, EndMessage: str = 'Countdown Complete!'):
    '''
    ### [Experimental] Countdown
    #### A verbose countdown timer

    ---

    #### Example
    ```
    Countdown(10,'Timer: ' ,'Timer complete!')
    ```
    '''
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
        print('Countdown Complete!')
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

def Prompt(Message: object = False, EnableGetpass: bool = False, Anykey: bool = False):
    '''
    ### Prompt
    #### Prompts user with desired message

    ---

    #### Examples
    ```
    #default value / Waits until the user press enter
    Prompt()

    #Pause until user press any key
    Prompt(Anykey=True)

    #Add Desired message / Waits until the user press enter
    Prompt('Hello Kaviyes!')
    ```
    '''

    if Anykey:
        EnableGetpass = False
        if _os.name == 'nt':
            import msvcrt

            if not Message:
                print('Press any key to continue...')
            
            if Message:
                print(Message)

            msvcrt.getch()
            return

        else:
            EnableGetpass = False
            import sys, tty, termios

            if not Message:
                print('Press any key to continue...')
            if Message:
                print(Message)
            sys.stdout.flush()
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return
    
    if not Message:
        _getpass.getpass('Press Enter to continue...')
    if Message:
        _getpass.getpass(Message)

    if EnableGetpass:
        userinput = _getpass.getpass(Message)
        return userinput

def CurrentTime(Format: str = None,Format_24H: bool = True):
    '''
    ### CurrentTime
    #### A simplified version of datetime function

    ---

    #### Examples
    ```

    #Using own format
    CurrentTime('%H:%M:%S')

    #Printing the results
    time = CurrentTime('%H:%M:%S')
    print(time)
    or
    print(CurrentTime('%H:%M:%S'))

    #quick preset
    CurrentTime(Format_24H=True) # its true by default
    ```
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
    ### sleep
    #### a delay function / This function is from time.sleep()

    ---

    #### Example
    ```
    sleep(1) # delays for 1 second
    ```
    '''

    _time.sleep(secs)

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
    '''
    Returns the current date (DAY.MONTH.YEAR)

    Kept for legacy, I suggest to use the function ```CurrentTime()```
    '''
    now = _datetime.datetime.now()
    return (now.strftime('%d.%m.%y'))

def Terminal(Command):
    '''
    ### Terminal
    #### a quick access to terminal / os.system()

    ---

    #### Examples
    ```
    Terminal('echo Hello Kaviyes!') #Outputs Hello Kaviyes! to terminal
    Terminal('title Kaviyesutil') #Sets terminal window title
    ```
    '''
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