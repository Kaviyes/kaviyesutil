![Open Issues](https://img.shields.io/github/issues/Kaviyes/kaviyesutil.svg) ![License](https://img.shields.io/github/license/Kaviyes/kaviyesutil.svg)
<p align="center">
  <img src="https://raw.githubusercontent.com/Kaviyes/kaviyesutil/main/image-kaviyesutilites.png" alt="Kaviyes Utilities" width="450" />
</p>

## [Experimental] 
### Version 0.1.4 Standard Utility

A toolkit often used with **Kaviyes related projects**, Its also ideal for small projects.

---

## Installation
You can install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)
```
pip install kaviyesutil
```
## Examples
```
import kaviyesutil

kaviyesutil.Countdown(2, 'Countdown: ', 'Countdown Complete!')

#Clear the temrinal
kaviyesutil.cter()

time = kaviyesutil.CurrentTime('%H:%M:%S')
print(time)

rand1 = kaviyesutil.GenerateCustomID('STD08')
print(rand1) #Output: ETFQD7WW

rand2 = kaviyesutil.GenerateCustomID(Length=8, Type='standard') #'all' and 'digit' is also available
print(rand2) #Output: FE6B2PUV

rand3 = kaviyesutil.GenerateCustomID('$0A$ - 0A00 - 00A0 - A$0A')
print(rand3) #Output: !8W+ - 2L70 - 90B5 - C#9N

kaviyesutil.Terminal('echo Hello Kaviyes!') #quick terminal access

kaviyesutil.sleep(1) #Its from time.sleep()
```
## Note
Some features are untested on the following platforms
- MacOS
- Linux

If you see an issue, report it here!

[![Open Issue](https://img.shields.io/badge/Open-Issue-brightgreen?style=for-the-badge)](https://github.com/Kaviyes/kaviyesutil/issues/new)

#### Links
- [PyPi](https://pypi.org/project/kaviyesutil/)
