# pywhiteboard
Whiteboard software for linux.
Installation
------------
```
$ sudo apt-get python-twisted python-xlib
$ python -m pip install PyUserInput==0.1.9
```

Finding Device
------------
```
$ xinput list | grep Hite
```
Note the id number of the device.

For example:
```
abhishek@vaio:~/dev_work/whiteboard/device_info$ xinput list | grep Hite
⎜   ↳ Hite Board-XXXXXXXX                       id=14   [slave  pointer  (2)]
```
id number is 14 in the above case.
