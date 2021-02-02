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





# --------------------------------------------------------------
#  KNOB DEFAULTS  ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')




# --------------------------------------------------------------
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)



# --------------------------------------------------------------
#  Python SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import shuffleShortcuts
import ListNavigator
import filepathLister
import paste_selected
##import shortcut_NodeComment
import shortcut_NodeCustom
import incremental_autosave

# --------------------------------------------------------------
#  Merge MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------
#mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

#mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")',  "alt+o", icon = "Out.png", shorcutContext =2)




# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Utilities menu & assign items ---

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
autosaveMenu = nuke.menu('Nuke').addMenu('Autosave')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
utilitiesMenu.addCommand('File Lister', 'filepathLister.file_lister()')

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"/icons/myGizmos_icon.png")

myGizmosMenu.addCommand('Autocrop', 'nukescripts.autocrop()') #have to addCommand in order for this to show
myGizmosMenu.addCommand('File Lister', 'filepathLister.file_lister()')
##Grain_CB
nuke.menu("Nodes").addCommand("Draw/Grain_CB", "nuke.createNode('Grain_CB')", icon="GrainCB.png")
# --------------------------------------------------------------
#  EDIT MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------
nuke.menu('Nuke').addCommand('Edit/Paste to Selected', 'paste_selected.paste_selected()', 'ctrl+shift+v')