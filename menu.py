# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.4
#  Last Updated: October 10th, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform
import nukescripts


# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\smith\.nuke'
MacOSX_Dir = '/Users/smith/.nuke'
Linux_Dir = '/home/smith/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None

import incremental_autosave
