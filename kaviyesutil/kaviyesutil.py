#Copyright 2023 Kaviyes.

'''
[Experimental]

A set of functions that's often used with Kaviyes related projects.

- KaviyesUtil Standard
- Version 0.1
'''

import os, datetime, time, getpass

___kaviyes_UTILversion___ = '0.1'
___kaviyes_UTILversionFull____ = 'Version 0.1.3 (September 2023)'

def Prompt(Message, EnableGetpass: bool = False):
    '''
    It is to mimic keyboard disabled feature but in reality its not, It uses getpass
    '''

    if EnableGetpass:
        userinput = getpass.getpass(Message)
        return userinput

    getpass.getpass(Message)

def CurrentTime(Format: str = None,Format_24H: bool = True):
    '''
    Returns Current Time, With "Format" default format will be overridden with your own defined format
    '''
    
    now = datetime.datetime.now()

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
    time.sleep(float)

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
    now = datetime.datetime.now()
    return (now.strftime('%d.%m.%y'))

def Terminal(Command):
    '''Oh look a quick access to terminal'''
    os.system(Command)

def cter():
    '''Clears the terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

def RevealUtilVersion(Args: str = None):

    '''
    'get' = returns version info | 'getFull' = returns detailed version info
    '''

    if Args == 'get':
        return ___kaviyes_UTILversion___
    elif Args == 'getFull':
        return ___kaviyes_UTILversionFull____
    else:
        return ___kaviyes_UTILversion___

def CleanStart(Args: int = 1, Value: str = None, Highlight: bool = True):
    '''
    Cleans terminal and display the creator signature (I added some cool highlight into it)

    [0] = Nothing
    [1] = KaviyesUtilities
    [2] = KaviyesLabs
    [3] = Kaviyes
    [4] = Custom (With Value Example Cleanstart(4, 'Anything'))
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    if Args == 0:
        signature = False
    elif Args == 1:
        signature = 'Kaviyes Utilities'
    elif Args == 2:
        signature = 'KaviyesLabs'
    elif Args == 3:
        signature = 'Kaviyes'
    elif Args == 4:
        signature = Value

    if not signature: return

    if Highlight:
        print(f'\033[30;47m{signature}\033[0m\n')
    
    if not Highlight:
        print(signature, '\n')