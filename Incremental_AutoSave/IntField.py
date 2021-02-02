# --------------------------------------------------------------
#  IntField.py
#  Version: 1.0.0
#  Author: Alexander Smith
#  Credit: Malcolm Kesson - Pyside2 code structure
#  Website: asmithvfx.com
#  Contact: smithat93@comcast.net
#  Last Updated: January 18th, 2021
# --------------------------------------------------------------
import math

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import *

#---------------------------------------------------------------------------------------
#   This class makes sure an integer is an integer and designs the integer input field
class LabelledIntField(QWidget):
    def __init__(self, title, initial_value=None):
        QWidget.__init__(self)
        self.intwidget = QLineEdit()
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.label = QLabel()
        self.label.setText(title)
        self.label.setFixedWidth(100)
        self.label.setFont(QFont("Arial",weight=QFont.Bold))
        layout.addWidget(self.label)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedWidth(100)
        self.lineEdit.setValidator(QIntValidator())
        if initial_value != None:
            self.lineEdit.setText(str(initial_value))
        layout.addWidget(self.lineEdit)
        layout.addStretch()
        
    def setLabelWidth(self, width):
        self.label.setFixedWidth(width)
        
    def setInputWidth(self, width):
        self.lineEdit.setFixedWidth(width)
        
    def getValue(self):
        return int(self.lineEdit.text())