from . sxgateway import *

SX = SXPKG.script.SX
SXRegion = SXPKG.script.Region
SXScreen = SXPKG.script.Screen
SXLocation = SXPKG.script.Location
SXImage = SXPKG.script.Image
SXImagePath = SXPKG.script.ImagePath
SXApp = SXPKG.script.App

class SXBase():

    SXClass = SX

    def __init__(self, *args):
        self.instance = self.SXClass.getDefaultInstance4py()
        if len(args) > 0:
            self.instance = self.SXClass.make4py(convertArgs(args))

    def __str__(self):
        return self.instance.toString()

    def __getattr__(self, item):
        currentObject = self.instance;

        def temp_method(*args, **kwargs):
            mCall = item + "("
            mCallError = "" + mCall
            countArgs = len(args)
            if countArgs > 0:
                mCall += "args[0]"
                mCallError += "%s" % (args[0])
            for nArg in range(1, countArgs):
                mCall += ", args[%d]" % nArg
                mCallError += ", %s" % (args[nArg])
            mCall += ")"
            mCallError  += ")"
            try:
                toEval = "currentObject." + mCall
                result = eval(toEval, {"currentObject": self.instance, "args": args})
                return result
            except:
                print("Method missing: %s::%s" % (currentObject, mCallError))
                return currentObject

        return temp_method

class Region(SXBase):
    """
    Wrapper for org.sikuli.script.Region

    - Region() the region of the primary screen
    - Region(x,y,w,h) a region at (x,y) with size (w,h) cropped to the containing screen
    - Region(otherRegion) make an object-copy of object otherRegion
    """

    SXClass = SXRegion

    def hover(self, *args):
        """
        Move the mouse pointer to the given target (args[0])

        if the target is
         - not given, it will be lastMatch or center (if no lastMatch) of this Region
         - an image-filename, a Pattern or an Image, it will first be searched and the valid Match's center/targetOffset will be the target
         - a Match: target will be center/targetOffset of the Match
         - a Region: target will be center of the Region
         - a Location: will be the target

        :param args: see above
        :return: int: 1 if done without errors, 0 otherwise
        """
        if len(args) == 0:
            return self.instance.hover()
        return self.instance.hover(convertArgs(args))

    def click(self, *args):
        if len(args) == 0:
            return self.instance.click()
        return self.instance.click(convertArgs(args))

    def highlight(self, *args):
        """
        show a colored frame around the region for a given time or switch on/off
        
        - **() or (color)** switch on/off with color (default red)

        - **(number) or (number, color)** show in color (default red) for number seconds (cut to int)
        
        allowed colors given as string               
         - a color name out of: black, blue, cyan, gray, green, magenta, orange, pink, red, white, yellow (lowercase and
           uppercase can be mixed, internally transformed to all uppercase)
         - these colornames exactly written: lightGray, LIGHT_GRAY, darkGray and DARK_GRAY
         - a hex value like in HTML: #XXXXXX (max 6 hex digits)    
         - an RGB specification as: #rrrgggbbb where rrr, ggg, bbb are integer values in range 0 - 255
           padded with leading zeros if needed (hence exactly 9 digits)

        :param args: a valid combination (see above) or omitted
        :return: self
        """
        if len(args) == 0:
            return self.instance.highlight()
        return self.instance.highlight4py(convertArgs(args))

class Screen(Region):

    SXClass = SXScreen

class Location(SXBase):

    SXClass = SXLocation

class Image(SXBase):

    SXClass = SXImage
