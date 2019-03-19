from . sxclasses import *

SCREEN = Screen()

def reset():
    SX().reset()

def setBundlePath():
    addImagePath()

def addImagePath(*path):
    if len(path) == 0:
        import inspect
        stack = inspect.stack()
        aPath = os.path.dirname(stack[1].filename)
        SXImagePath.setBundlePath(aPath)
        print("setBundlePath:", aPath)
    else:
        aPath = path[0]
        SXImagePath.add(aPath)

def openApp(app):
    return SXApp(app).open()

def switchApp(app):
    return SXApp(app).focus()

def closeApp(app):
    return SXApp(app).close()

def click(*args):
    return SCREEN.click(*args)

def hover(*args):
    """
    **hover** Move the mouse pointer to the given target (args[0])

    if the target is
     - not given, it will be lastMatch or center (if no lastMatch) of this Region
     - an image-filename, a Pattern or an Image, it will first be searched and the valid Match's center/targetOffset will be the target
     - a Match: target will be center/targetOffset of the Match
     - a Region: target will be center of the Region
     - a Location: will be the target
     - (int, int): explicit target coordinates

    :param args: see above
    :return: int: 1 if done without errors, 0 otherwise
    """
    return SCREEN.hover(*args)
