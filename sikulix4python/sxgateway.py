import sys
import time
import os

def convertArgs(args):
    sxargs = JavaGW.jvm.java.util.ArrayList()
    for arg in args:
        try:
            sxargs.append(arg)
        except:
            sxargs.append(arg.instance())
    return sxargs

def sxstart():
    from py4j.java_gateway import JavaGateway
    try:
        JavaGW = JavaGateway()
        SXPKG = JavaGW.jvm.org.sikuli
        return (JavaGW, SXPKG)
    except:
        print("sxstart: SikuliX not running")
        exit(1)

(JavaGW, SXPKG) = sxstart()

def sxClass(className, pkgName = "script"):
    classRef = "SXPKG.%s.%s" % (pkgName, className)
    theClass = eval(classRef, {"SXPKG" : SXPKG})
    try:
        theClass.getDefaultInstance4py()
    except:
        print("sxClass: Class missing: %s" % (classRef))
        return None
    return theClass

def sxClassHelp(className, pkgName = "script"):
    theClass = sxClass(className, pkgName)
    if theClass:
        print(theClass.__doc__)
    return theClass
