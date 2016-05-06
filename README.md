# pywhiteboard
Whiteboard software for linux.
Installation
------------
```
$ sudo apt-get python-twisted python-xlib
$ python -m pip install PyUserInput==0.1.9
```

Finding and Specify the Device
------------
1.  Note the id number of the device.
  ````
  $ xinput list
  ```
  
  For example:
  ```
  abhishek@vaio:~/dev_work/whiteboard/device_info$ xinput list | grep Hite
  ⎜   ↳ Hite Board-XXXXXXXX                       id=14   [slave  pointer  (2)]
  ```
  id number is 14 in the above case.

2. Modify the correct id in code (https://github.com/abhigenie92/pywhiteboard/blob/master/pywhiteboard.py#L58)
