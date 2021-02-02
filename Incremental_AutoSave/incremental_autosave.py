# --------------------------------------------------------------
#  incremental_autosave.py
#  Version: 1.0.0
#  Author: Alexander Smith
#  Credit: Malcolm Kesson - Pyside2 code structure
#  Website: asmithvfx.com
#  Contact: smithat93@comcast.net
#  Last Updated: January 18th, 2021
# --------------------------------------------------------------

# How it works:
#   1. Creates an incremental save
#   2. Given a user inputted time step, it will save an increment at each step
# --------------------------------------------------------------

#imports nuke lib
import nuke, nukescripts, os, time, threading, math, sys

from IntSlider import *
from IntField import *
from Thread import *

try:
	from PySide import QtGui, QtCore
except ImportError:
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	from PySide2.QtCore import *
	from PySide2.QtUiTools import *
#----------------------------------------------------------------------------------------
#   This Class builds the foundational custom GUI for the script

class IncrementalAutosave(QWidget):
	# "__init__" is a special function that is automatically called 
	# by python when an instance of our DemoDialog class is created.

	def __init__(self, parent=None):
		# Because our class is derived from QDialog its constructor is called.
		QWidget.__init__(self, parent)


		# Ensure our window stays in front and give it a title
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.setWindowTitle("Incremental Autosave")
		self.setFixedSize(400, 150)
		
		# Create and assign the main (vertical) layout.
		vlayout = QVBoxLayout()
		hlayout = QHBoxLayout()
		self.setLayout(vlayout)  
		
		# Ensure the buttonPanel is pushed down to the lower edge of the
		# Dialog window.
		vlayout.addStretch()    
		
		self.addSlidersPanel(vlayout)
		self.addIntInput(vlayout)
		self.addButtonPanel(vlayout)		
		self.show()

		self.threadpool = QThreadPool()

		

	def addSlidersPanel(self, parentLayout):
		vlayout = QVBoxLayout()
		self.num = IntSlider("Time Interval", 1, 60 ,10, vlayout)
		parentLayout.addLayout(vlayout)

	def addIntInput(self, parentLayout):
		hlayout = QHBoxLayout()
		self.versions = LabelledIntField('Versions', 5)

		hlayout.addWidget(self.versions)
		hlayout.addStretch()
		parentLayout.addLayout(hlayout)
		
	def addButtonPanel(self, parentLayout):
		# Add a Button and connect it to our custom ButtonAction() method.
		self.button = QPushButton("Save")
		self.button.clicked.connect(self.ButtonAction)
		
		# For aesthetics we add the button to a horizonal layout and use
		# stretch() to ensure it is pushed to the right hand edge.
		hlayout = QHBoxLayout()
		hlayout.addStretch()
		hlayout.addWidget(self.button)
		parentLayout.addLayout(hlayout)
		#--------------------------------------------------------------------
	def incrsave(self):
		
		if nuke.root().name() != "Root":
			versionrange = range(self.versions.getValue())
			x = self.num.getValue()
			for t in versionrange:
				root_name = nuke.root().name()
				(prefix, v) = nukescripts.version_get(root_name, "v")
				v = int(v)
				newFileName = nukescripts.version_set(root_name,prefix, v, v+1)
				newFileExists = os.path.exists(newFileName)
				if newFileExists:
					print "Next version exists...exiting"
					break
				else:
					while t <= versionrange:
						if nuke.modified() == True: 
							nukescripts.script_version_up()
							print "We have Saved."
							time.sleep(x)
							t+=1
							print t + " version(s) saved"
						else:
							print "No changes made"
							time.sleep(x)
						if t > versionrange: 
							break    
		else:
			print "Cannot Run on Root"

#Gets range of the versions to loop through	
#Loops through each increment of the chosen versions
#While the loop is less than the chosen versions, it will run through this function
#nuke.modified() checks if the nuke script has been modified, if so it runs the script version save node and sleeps
#for the desired time (x). Then the variable is incremented upon.
#If nuke.modified returns False, it means no changes has been made and the function will sleep for the given increment again
#and run through the program again
	#--------------------------------------------------------------------
	def ButtonAction(self):
		print "You will save "+ (str(self.versions.getValue()))+ " versions every " + (str(self.num.getValue())) + " seconds."

		thread = Thread(self.incrsave)

		self.threadpool.start(thread)
		#Multithread magic. You call the function from this thread, allows nuke to run the sleep functions in a separate thread 
		#and not hang during each time.sleep. Daemon makes sure the loop can be interrupted during the loop, else it will run till
		#the next increment and then close.

	#--------------------------------------------------------------------

	