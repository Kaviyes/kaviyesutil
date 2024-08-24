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
'''`FILE UTILITY MODULE`

A set of functions to streamline the development process.

'''
import os as _os
import sys as _sys
import json as _json

def get_file_size(file_path: str):
    '''
    Gets the size of a file in bytes.

    Parameters

    - `file_path (str)` : Path to the file.

    Returns
    - int: The size of the file in bytes, or -1 if the file does not exist.
    '''
    if _os.path.isfile(file_path):
        return _os.path.getsize(file_path)
    return -1

def directory_exists(directory_path: str) -> bool:
    '''
    Checks if a directory exists.

    Parameters

    - `directory_path (str)` : Path to the directory.

    Returns
    - bool: True if the directory exists, False otherwise.
    '''
    return _os.path.isdir(directory_path)

def file_exists(file_path):
    '''
    Checks if a file exists at the specified path.

    Parameters

    - `file_path (str)` : The path to the file.

    Returns
    - bool: True if the file exists, False otherwise.
    '''
    return _os.path.isfile(file_path)

def writecontent(file_path, content, append=False, debug=False):
    '''
    Writes content to a file, optionally appending to the file.

    Parameters

    - `file_path (str)` : The path to the file to be written.
    - `content (str)` : The content to write to the file.
    - `append (bool)` : If True, appends to the file instead of overwriting. Defaults to False.
    - `debug (bool)` : If True, prints error messages for IOError. Defaults to False.

    Returns
    - bool: True if writing was successful, False otherwise.
    '''
    mode = 'a' if append else 'w'
    try:
        with open(file_path, mode) as file:
            file.write(content)
        return True
    except IOError as e:
        if debug:
            print(e)
        return False

def readcontent(file_path, strip_whitespace = False, uppercase = False, lowercase = False, debug = False):
    '''
    Reads the content of a file and optionally strips whitespace.

    Parameters

    - `file_path (str)` : The path to the file to be read.
    - `strip_whitespace` : (bool): If True, removes leading and trailing whitespace from the content. Defaults to False.
    - `debug (bool)`: If True, prints error messages for FileNotFoundError or IOError. Defaults to False.
    - `uppercase (bool)` : Changes every strings to uppercase.
    - `lowercase (bool)` : Changes every strings to lowercase.

    Returns
    - str or None: The content of the file, or None if an error occurs.
    '''

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if strip_whitespace:
                content = content.strip()
            if uppercase:
                content = content.upper()
            if lowercase:
                content = content.lower()
    except (FileNotFoundError, IOError) as e:
        if debug: print(e)
        content = None

    return content

def respath(relative_path):
    '''
    Get Absolute path to resource, works for dev and for PyInstaller
    - [Credits to max & Stackoverflow community!](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741)
    '''
    
    try:
        base_path = _sys._MEIPASS
    except Exception:
        base_path = _os.path.abspath(".")

    return _os.path.join(base_path, relative_path)


def write_json(file_path: str, data: dict, debug: bool = False):
    '''
    Writes JSON data to a file.

    Parameters

    - `file_path (str)` : Path to the JSON file.
    - `data (dict)` : The data to write to the file.
    - `debug (bool)` : If True, prints error messages for IOError. Defaults to False.

    Returns
    - bool: True if writing was successful, False otherwise.
    '''
    try:
        with open(file_path, 'w') as file:
            _json.dump(data, file, indent=4)
        return True
    except IOError as e:
        if debug:
            print(e)
        return False

def read_json(file_path: str, debug: bool = False):
    '''
    Reads JSON data from a file.

    Parameters

    - `file_path (str)` : Path to the JSON file.
    - `debug (bool)` : If True, prints error messages for FileNotFoundError or JSONDecodeError. Defaults to False.

    Returns
    - dict or None: The parsed JSON data as a dictionary, or None if an error occurs.
    '''
    try:
        with open(file_path, 'r') as file:
            return _json.load(file)
    except (FileNotFoundError, _json.JSONDecodeError) as e:
        if debug:
            print(e)
        return None
