#Aaron Parker
#240614
#Crop simulation

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import * #gives access to radio class

class CropWindow(QMainWindow):
    """This class creates a window to show the growth of the crops that are simulated"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        #initial layout of window to select crop type

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato"))
        self.instantiate_button = QPushButton("Create Crop")

        #create layout to hold widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #instantiate main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raises instance to top of the screen
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
