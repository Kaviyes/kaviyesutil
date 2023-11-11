<img src="https://raw.githubusercontent.com/Kaviyes/kaviyesutil/main/Kaviyesutil.png" width="410"/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)

![Open Issues](https://img.shields.io/github/issues/Kaviyes/kaviyesutil.svg) ![Closed Issues](https://img.shields.io/github/issues-closed/Kaviyes/kaviyesutil.svg) ![License](https://img.shields.io/github/license/Kaviyes/kaviyesutil.svg) ![VsCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg) 

A standard kaviyes utility for python thats ideal for small projects and prototypes.

## Installation
You can install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)
```
pip install kaviyesutil -U
```

## Documentation

### FUNCTIONS

<br>

FUNCTION | DESCRIPTION
--------- | ------------
`printc` | Quick and easy way to customize your text
`countdown` | A verbose countdown timer
`cloakedLink` | create a visually appealing links for terminals
`resourcePath` | Get absolute path to resource, works for dev and for PyInstaller
`generateCustomID` | Generate own custom ID or use premade formats
`prompt` | Prompts user with desired message
`currentTime` | A simplified version of datetime function
`delay` | a delay function / This function is from time.sleep()
`decodeHex` | Decodes Hex into String
`encodeHex` | Encodes String into Hex
`terminal` | a quick access to terminal
`cter` | Clears the terminal

### EXAMPLES
### printc
```
printc('Hello Kaviyes!', 'red', 'magenta')
print(printc('Hello Kaviyes!', 'red', 'magenta', True))
    
printc('Hello Kaviyes!', 'red', 'magenta', 'bold', 'italic')
print(printc('Hello Kaviyes!', 'red', 'magenta', 'bold', 'italic', ReturnText='True'))
```

### countdown
```
countdown(10,'Timer: ' ,'Timer complete!')
```

### cloakedLink
```
cloakedLink('visit kaviyes on github!', 'https://github.com/Kaviyes', True)
print(cloakedLink('visit kaviyes on github!', 'https://github.com/Kaviyes'))
cloakedLink(printc('Visit Kaviyes on Github!', 'cyan', 'default', 'underlined', ReturnText=True), 'https://github.com/Kaviyes', Print=True)
```

### resourcePath
```
resourcePath("image.png") # For PyInstaller
```

### generateCustomID
```
generateCustomID('STD08') # 08 | 16 | 32

generateCustomID(Length="8", Type="standard") # does not include special characters
generateCustomID(Length="8", Type="all") # includes special characters
generateCustomID(Length="8", Type "digits")

generateCustomID('AA00aa$$') # custom one
# A = Uppercase letter A-Z
# a = Lowercase letter a-z
# $ = Custom Characters
# 0 = Digits 0-9

# NOTE: Using "Length" will override "Format"
```

### prompt
```
#default value / Waits until the user press enter
prompt()

#Pause until user press any key
prompt(Anykey=True)

#Add Desired message / Waits until the user press enter
prompt('Hello Kaviyes!')
```

### currentTime
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

### delay
```
delay(1) # delays for 1 second

sleep(.25) # delays for 250 miliseconds
```

### decodeHex
```
x = 68656c6c6f20746865726521
decodeHex(x, reversed = True)

decodeHex(x, reversed = False)
```

### encodeHex
```
x = "hello there!"
encodeHex(x, reversed = True)

encodeHex(x, reversed = False)
```

### terminal
```
terminal('echo Hello Kaviyes!') #Outputs Hello Kaviyes! to terminal
```

### cter
```
cter() # will clear the terminal
```

<br>

## Notes

Kaviyesutil version **2.0.0** is no longer compatible with older versions.
* This is a completely revamped version, and it is not compatible with older versions due to function changes. It is better to download the old version and use it locally if you want to update to the latest version.

Changes in the new version:

* Renamed FancyText to `printc`.
* Removed `ConvertUnits` and `Today` functions.
* Improved function names.
* General bug fixes and improvements.

Compatibilities:

 Python version: **3.10** minimum

IDE:
* Visual Studio Code (fully compatible)
* PyCharm (function description is displayed in raw but still readable)
* Not tested on other IDEs yet

OS:
* Android (Termux)
* Windows (8.1 and later)
* Linux (Debian and others)
* macOS (10.15 Catalina or later)

Links:
* [PyPi](https://pypi.org/project/kaviyesutil/)
* [Wheelsodex](https://www.wheelodex.org/projects/kaviyesutil/)
* Found a problem [create an issue](https://github.com/Kaviyes/kaviyesutil/issues/new/choose) here!
* Create a [pull request](https://github.com/Kaviyes/kaviyesutil/compare) here!

<br>
<br>
<br>
<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/Kaviyes/kaviyesutil/main/Kaviyes-Text.png" alt="KAVIYES" width="500"/>
</p>

<br>
