[<img src="https://raw.githubusercontent.com/Kaviyes/kaviyesutil/37c00cd0806a99bded88d82c255ae12161ffd6ef/Kaviyesutil.svg" width="385"/>](https://github.com/Kaviyes/kaviyesutil)

![Open Issues](https://img.shields.io/github/issues/Kaviyes/kaviyesutil.svg) ![Python](https://camo.githubusercontent.com/3da9491fa3fce6afca8e32177b260cb87bea5d4dbcc057da64589a94dbc5815a/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f676f6f676c652d67656e657261746976656169) ![Closed Issues](https://img.shields.io/github/issues-closed/Kaviyes/kaviyesutil.svg)

A standard kaviyes utility for python thats ideal for small projects and prototypes.

## Installation
You can install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)
```
pip install kaviyesutil -U
```

## Usage
```
import kaviyes.util as util
```

## Functions and Parameters

|FUNCTION|DESCRIPTION|
|---|---|
|[`connected`](#connected)|Checks if there is an active internet connection.|
|[`reverse_string`](#reverse_string)|Reverses a given string.|
|[`timenow`](#timenow)|Returns the current time in a specified format.|
|[`delay`](#delay)|A delay function based on how many seconds.|
|[`terminal`](#terminal)|This function allows you to quickly execute any command as if you were typing it directly into the terminal.|
|[`clter`](#clter)|Clears the contents of the terminal screen|
|[`get_file_size`](#get_file_size)|Gets the size of a file in bytes.|
|[`directory_exists`](#directory_exists)|Checks if a directory exists.|
|[`file_exists`](#file_exists)|Checks if a file exists at the specified path.|
|[`writecontent`](#writecontent)|Writes content to a file, optionally appending to the file.|
|[`readcontent`](#readcontent)|Reads the content of a file and optionally strips whitespace.|
|[`respath`](#respath)|Get Absolute path to resource, works for dev and for PyInstaller|
|[`write_json`](#write_json)|Writes JSON data to a file.|
|[`read_json`](#read_json)|Reads JSON data from a file.|

<br>

## Examples

### `connected`

Parameters
- `url (str)` : URL to test the connection. Defaults to Google.
- `timeout (int)` : Timeout in seconds for the connection test. Defaults to 5.

```
util.connected(url='http://www.google.com', timeout=5):
```
OUTPUT
```
True
```

Returns
- bool : True if conneted, False otherwise,

---

### `reverse_string`

Parameters:
- `s (str)` : The string to reverse.


```
x = util.reverse_string("Hello, World!")
print(x)
```
OUTPUT
```
!dlroW ,olleH
```

Returns:
- str : The reversed string.

---

### `timenow`

Parameters:
`format (str, optional)` :

A string specifying the format in which to return the time. 

If provided, this format string will be used. Common format codes include:
- `'%H:%M:%S'` for hours, minutes, and seconds in 24-hour format
- `'%I:%M:%S %p'` for hours, minutes, and seconds in 12-hour format with AM/PM

<br>

`format_24H (bool, optional)` :

A boolean that determines the time format when `format` is not provided. 
- If `True`, the function uses the 24-hour format (e.g., '14:30:00').
- If `False`, the function uses the 12-hour format with AM/PM (e.g., '2:30:00 PM'). 
Defaults to `True`.

```
x = util.timenow()
print(x)
```
OUTPUT
```
18:00:00
```
Returns:
- str : The current time formatted according to the provided `format` string or default settings.

---

### `delay`

Parameters:
- `secs (float)` : The number of seconds to delay the execution.

```
util.delay(2.3)
```
OUTPUT
```
None
```
Returns:
- None : This function does not return any value.

---

### `terminal`

Parameters:
- `command (str)` : The command to be executed in the terminal.

```
util.terminal("echo Hello, World!")
```
OUTPUT
```
Hello, World!
```

Returns:
- None : This function does not return any value.

---

### `clter`

Parameters:
- `message (object, optional)` : An optional message to print after clearing the terminal screen.

```
util.clter()
```
OUTPUT
```

```
---
```
util.clter("Hello, World!")
```
OUTPUT
```
Hello, World!
```
Returns:
- None : This function does not return any value.

---

### `get_file_size`

Parameters:
- `file_path (str)` : Path to the file.

```
x = util.get_file_size("story.txt")
print(x)
```
OUTPUT
```
2313
```

Returns:
- int : The size of the file in bytes, or -1 if the file does not exist.

---

### `directory_exists`

Paramters:
- `directory_path (str)` : Path to the directory.

```
x = util.directory_exists("directory")
print(x)
```
OUTPUT
```
True
```

Returns:
- bool : True if directory exists, False otherwise.

---

### `file_exists`

Paramters:
- `file_path (str)` : Path to the directory.

```
x = util.file_exists("file.txt")
print(x)
```
OUTPUT
```
True
```

Returns:
- bool : True if file exists, False otherwise.

---

### `writecontent`

Parameters:
- `file_path (str)` : The path to the file to be written.
- `content (str)` : The content to write to the file.
- `append (bool)` : If True, appends to the file instead of overwriting. Defaults to False.
- `debug (bool)` : If True, prints error messages for IOError. Defaults to False.

```
x = util.writecontent("greet.txt", "Hello, World!")
print(x)
```
OUTPUT
```
True
```

Returns:
- bool : True if writing was successful, False otherwise.

---

### `readcontent`

Parameters:
- `file_path (str)` : The path to the file to be read.
- `strip_whitespace` (bool): If True, removes leading and trailing whitespace from the content. Defaults to False.
- `debug (bool)` : If True, prints error messages for FileNotFoundError or IOError. Defaults to False.
- `uppercase (bool)` : Changes every strings to uppercase.
- `lowercase (bool)` : Changes every strings to lowercase.

```
x = util.readcontent("greet.txt")
print(x)
```
OUTPUT
```
Hello, World!
```

Returns:
- str or None: The content of the file, or None if an error occurs.

---

### `respath`

Parameters:
- `relative_path (str)` : The relative path to the resource. This should be a path relative to the directory where the script is running or the bundled application's directory.

```
x = util.respath("banana.png")
print(x)
```
OUTPUT
```
K:\Application\assets\banana.png
```

Returns:
- str: The absolute path to the resource.

---

### `write_json`

Parameters:
- `file_path (str)`: Path to the JSON file.
- `data (dict)`: The data to write to the file.
- `debug (bool)`: If True, prints error messages for IOError. Defaults to False.

```
data = {"name:": "John", "age": 23, "country": "Germany"}
x = util.write_json("ID.json", data)
print(x)
```
OUTPUT
```
True
```

Returns:
- bool: True if writing was successful, False otherwise.

---

### `read_json`

Parameters:
- `file_path (str)`: Path to the JSON file.
- `debug (bool)`: If True, prints error messages for FileNotFoundError or JSONDecodeError. Defaults to False.

```
x = util.read_json("ID.json")
print(x)
```
OUTPUT
```
{'name:': 'John', 'age': 23, 'country': 'Germany'}
```

Returns:
- dict or None: The parsed JSON data as a dictionary, or None if an error occurs

---
<br><br>

## Compatibility support

The kaviyesutil version **2.1.2** is not compatible with the older versions. The version **2.0.1** is usable with:
```
import kaviyes.util.legacy as util
```

## Changelog 2.1.1

* Improved overall readability of the documentations and functions.
* Minor improvements.
* Added basic file management utilities.

## Requirements:

 Python version: **3.9** minimum

IDE:
* Visual Studio Code (Fully compatible)
* PyCharm & Visual Studio (Function description is displayed in raw but still readable)

OS:
* Linux
* Windows (8.1 and later)
* macOS (10.15 Catalina and later)

Links:
* [PyPi](https://pypi.org/project/kaviyesutil/)
* Found a problem [create an issue](https://github.com/Kaviyes/kaviyesutil/issues/new/choose) here!
* Create a [pull request](https://github.com/Kaviyes/kaviyesutil/compare) here!

<br>
<br>
<br>
<br>

<p align="center">
  <a href="https://github.com/Kaviyes/">
    <img src="https://raw.githubusercontent.com/Kaviyes/kaviyesutil/main/Kaviyes-Text.png" alt="KAVIYES" width="500"/>
  </a>
</p>

<br>
