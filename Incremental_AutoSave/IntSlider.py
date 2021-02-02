# --------------------------------------------------------------
#  IntSlider.py
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
#   This class makes sure an integer is an integer and designs the slider panel
class IntSlider(QWidget):
    def __init__(self, title, min, max, def_value, parent_layout, label_width=100):
        super(IntSlider, self).__init__(None)
        label = QLabel()
        label.setText(title)
        label.setFixedWidth(label_width)
    
        self.spinbox = QSpinBox()
        self.spinbox.setRange(min, max)
        self.spinbox.setValue(def_value)
        
        self.slider  = QSlider(Qt.Horizontal)
        self.slider.setRange(min, max)
        self.slider.setValue(def_value)
            
        self.slider.valueChanged.connect(self.update_spinbox)
        self.spinbox.valueChanged.connect(self.update_slider)
        hlayout = QHBoxLayout() 
        hlayout.addWidget(label)
        hlayout.addWidget(self.spinbox)
        hlayout.addWidget(self.slider)
        parent_layout.addLayout(hlayout)
        
    def update_spinbox(self):
        value = self.slider.value()
        self.spinbox.setValue( value )
    def update_slider(self):
        value = self.spinbox.value()
        self.slider.setValue( value )
    def getValue(self):
        return self.spinbox.value()