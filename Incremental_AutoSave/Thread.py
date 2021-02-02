# --------------------------------------------------------------
#  Thread.py
#  Version: 1.0.0
#  Author: Alexander Smith
#  Website: asmithvfx.com
#  Contact: smithat93@comcast.net
#  Last Updated: January 18th, 2021
# --------------------------------------------------------------
import os, time, threading, math, sys

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import *

#---------------------------------------------------------------------------------------
#	Creates a seperate thread for the pyside2 code to run on and function. This ensures nuke won't hang while executing.
class Thread(QRunnable):

    def __init__(self, threadrun, *args, **kwargs):
        super(Thread, self).__init__()
        self.threadrun = threadrun
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.threadrun(*self.args,**self.kwargs)