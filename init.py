# --------------------------------------------------------------
#  init.py
#  Version: 1.0.0
#  Last Updated: May 6th, 2019
# --------------------------------------------------------------

# ----- DEFINE CUSTOM FOLDER STRUCTURE -------------------------

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./python/shuffleShortcuts')
nuke.pluginAddPath('./python/Incremental_AutoSave')

nuke.pluginAddPath('./icons')



##Grain_CB default presets file location and name (use this to set up different preset files for different shows or to store multiple settings/grains)
nuke.knobDefault('Grain_CB.fileLoc', '/Users/smith/.nuke/Grain_CB_presets.txt')