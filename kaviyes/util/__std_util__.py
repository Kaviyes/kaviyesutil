# Copyright (c) 2023 Kaviyes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''`STANDARD UTILITY MODULE`

A set of functions to streamline the development process.

'''
from time import sleep as _sleep
from os import system as _system
from datetime import datetime as _datetime
import requests as _requests

def connected(url='http://www.google.com', timeout=5):
    '''Checks if there is an active internet connection.

    Parameters

    - `url (str)` : URL to test the connection. Defaults to Google.
    - `timeout (int)` : Timeout in seconds for the connection test. Defaults to 5.

    Returns

    - bool: True if connected, False otherwise.
    '''
    try:
        response = _requests.get(url, timeout=timeout)
        return response.status_code == 200
    except _requests.ConnectionError:
        return False

def reverse_string(s):
    '''
    Reverses a given string.

    Parameters

    - `s (str)` : The string to reverse.

    Returns
    - str: The reversed string.
    '''
    return s[::-1]

def timenow(format: str = None, format_24H: bool = True):
    '''
    Returns the current time in a specified format.

    - If `format` is provided, it will use that format.
    - If `format` is not provided, it uses 24-hour format if `format_24H` is True; otherwise, it uses 12-hour format.

    Examples:
    ```
    print(timenow('%H:%M:%S'))
    # Default 24-hour format
    print(timenow(format_24H=True))
    # 12-hour format
    print(timenow(format_24H=False))
    ```
    
    '''
    now = _datetime.now()

    if format:
        return now.strftime(format)

    return now.strftime('%H:%M:%S') if format_24H else now.strftime('%I:%M:%S %p')

def delay(secs: float):
    '''
    Delay function using time.sleep()

    A delay function based on how many seconds.

    Examples:
    ```
    delay(1) # Delays for 1 second.
    delay(2.5) # Delays for 2.5 seconds.
    ```
    '''

    _sleep(secs)

def terminal(command: str):
    '''
    Executes a terminal command using os.system.

    This function allows you to quickly execute any command as if you were typing it directly into the terminal.

    Examples:
    ```
    terminal('echo Hello, Kaviyes!')  # Outputs 'Hello Kaviyes!' to the terminal
    terminal('title Kaviyesutil')    # Sets the terminal window title (Windows only)
    ```
    
    Note:
    - The command will be executed in the context of the shell used by os.system, which is platform-dependent.
    - On Windows, some commands may have different syntax or requirements compared to Unix-like systems.
    '''

    try:
        _system(command)
    except Exception as e:
        print(f"An error occured: {e}")

def clter(message: object = None):
    ''' Clears the contents of the terminal screen'''

    print("\033c", end="")
    if message:
        print(message)
