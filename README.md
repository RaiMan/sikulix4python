# sikulix4python

*(currently paused --- will be continued starting in late Summer 2019)*

Use SikuliX from real [Python via py4j](https://www.py4j.org) (but no need to know, how it works ;-)

**under development -- no guarentee for anything :-)**

... but you might post issues (questions, bugs, ideas, requests, ...)

**What you need**
 - the latest 1.1.4 sikulixapi.jar (https://raiman.github.io/SikuliX1/downloads.html)
 - a Python installation 2.7 up to 3.7 (3.7 recommended)
 - run ``pip install py4j`` to get the support on the Python side
 - a mature Python IDE (I use IntelliJ's PyCharm) or just a Python REPL.
 
**How to test**

Currently it is recommended, to fork this project and work in the project context.

But this should also be possible:
 - copy the folder ``sikulix4python`` from inside the project to a place, where your Python will find it, when imported
 
In both cases:
 - put ``from sikulix4phyton import *`` at the beginning of your test script
 - use stuff from ``sxundotted`` just as is
 - use stuff from ``sxclasses`` to access features of the SikuliX API classes like Region, Screen, Location ...
 
Currently you have to look into the Python files, to find out, what is possible.

**How is the SikuliX Java API accessed from Python**

Before running Python scripts this way, you have to start a SikuliX server instance manually:

``java -jar path-to/sikulixapi.jar -p``

When you see this in the terminal window, it is running:

```
März 15, 2019 10:26:20 VORM. py4Java.GatewayServer fireServerStarted
INFO: Gateway Server Started
```

To stop the server you can use the known stop hotkey (Windows: ALT-SHIFT-C, Mac: CMD-SHIFT-C).

Adding ``-v`` to the commandline will give you startup debug information.

**What is the plan**
 - have the complete official SikuliX API with docs available at time of script development (autocomplete, docs, help, ...)
 - be able to additionally access every public method from the SikuliX Java API (you must know the method signature)
 - have a handy solution for handling image path's of imported scripts/modules
 - run existing SikuliX scripts without changes (... but there will surely be exceptions)
 
**Things you should be aware off**
- you might get any problem at any time, since the current state is ``proof of concept``
- anything might be changed at any time without notice
- errors and warnings you get in the terminal window can be ignored, as long as it works as intended on the Python side
- output coming from the SikuliX Java API is currently only going to the terminal window
- my current development work is on macOS 10.14/Windows 10, Java 11/12, Python 3.7 with PyCharm
- no tests on Linux yet

**An example**

``` python
# https://www.python.org should be opened in Safari

# build the bridge to SikuliX
from sikulix4python import *

# make images available in the folder of the script
addImagePath()

switchApp("Safari")

hover() # undotted uses SCREEN object (sxundotted)

scr = Screen()

# getCenter() is found auto-magically,
# though not defined in the Python class Screen
# see sxclasses::__getattr__
# one gets method missing, if signatures do not fit
scr.getCenter().grow(100).highlight(2)

img = "img.png" # located via ImagePath

# a Match object is completely handled at the Java level
# not defined at the Python level
match = scr.exists(img, 3) # method missing, wrong signature
match = scr.exists(img, 3.0) # number must be float/double
if match:
    match.highlight(2)
    match.click()
```
