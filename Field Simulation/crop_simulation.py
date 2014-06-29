#Aaron Parker
#240614
#Crop simulation

import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import * #gives access to radio class
from manual_grow_dialog_class import * #gives access to manual grow dialog class
from crop_view_class import * #provides graphical crop status display
from Wheat_Class import *
from Potato_Class import *


class CropWindow(QMainWindow):
    """This class creates a window to show the growth of the crops that are simulated"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

        #stacked layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_crop_widget)

        #set central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

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

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def create_view_crop_layout(self,crop_type):
        #second layout of window, allows us to view crop growth

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        if crop_type == 1:
            self.crop_view = WheatView()
        elif crop_type == 2:
            self.crop_view = PotatoView()

        #ensure the crop view appears a certain size
        self.crop_view.setHorizontalScrollBarPolicy(1)
        self.crop_view.setVerticalScrollBarPolicy(1)
        self.crop_view.setFixedHeight(182)
        self.crop_view.setFixedWidth(242)

        self.manual_grow_button = QPushButton("Manual Grow")
        self.automatic_grow_button = QPushButton("Automatic Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widgets to status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #line edit widgets for status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #grow grid widgets
        self.grow_grid.addWidget(self.crop_view,0,0)
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #widget to hold layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        #connections
        self.automatic_grow_button.clicked.connect(self.automatically_grow_crop)
        self.manual_grow_button.clicked.connect(self.manually_grow_crop)
        

    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() # gets the radio button that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()

        self.create_view_crop_layout(crop_type)
        self.stacked_layout.addWidget(self.view_crop_widget)
        self.stacked_layout.setCurrentIndex(1) #change visible layout

    def automatically_grow_crop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def manually_grow_crop(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_() #run manual dialog window
        light, water = manual_values_dialog.values()
        self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def update_crop_view_status(self):
        crop_status_report = self.simulated_crop.report() #gets report from crop class

        #update line edit text fields
        self.growth_line_edit.setText(str(crop_status_report["growth"]))
        self.days_line_edit.setText(str(crop_status_report["days growing"]))
        self.status_line_edit.setText(str(crop_status_report["status"]))

        if crop_status_report["status"] == "Seed":
            self.crop_view.switch_scene(0)
        elif crop_status_report["status"] == "Seedling":
            self.crop_view.switch_scene(1)
        elif crop_status_report["status"] == "Young":
            self.crop_view.switch_scene(2)
        elif crop_status_report["status"] == "Mature":
            self.crop_view.switch_scene(3)
        elif crop_status_report["status"] == "Old":
            self.crop_view.switch_scene(4)


        
                                        
        
def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #instantiate main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raises instance to top of the screen
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
