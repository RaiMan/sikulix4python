# https://www.python.org should be opened in Safari

# build the bridge to SikuliX
from sikulix4python import *
reset()

#print(sxClassHelp("Region")); exit()

reg = Region()
print(reg)
reg.setX(100).setW(300)
print(reg)
hover()
hover(reg)

exit()

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
