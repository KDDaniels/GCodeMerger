"""
GCodeMerger is mean to merge G-code files with some addition to make multi-color printing easier with a single filament printer.
Copyright (C) 2025 Kendall Daniels

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QLabel, QPushButton, QLineEdit, QTabWidget

class Main_Window(QMainWindow):
    """
    Main component of the GUI
    Holds all of the widgets
    """
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(100, 100, 500, 400)

        self.generate_widgets()

    def generate_widgets(self):

        ### Main container ###
        self.container_main = QWidget(self)
        self.setCentralWidget(self.container_main)
        self.layout_vert_main = QVBoxLayout(self.container_main)



        ### File Select ###
        self.container_file_select = QWidget(self.container_main)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.container_file_select.sizePolicy().hasHeightForWidth())

        self.container_file_select.setSizePolicy(sizePolicy)
        self.layout_vert_select = QVBoxLayout(self.container_file_select)

        ## File One ##
        self.container_file_one = QHBoxLayout()

        self.label_file_one = QLabel("File One: ", self.container_file_select)
        self.open_file_one = QPushButton("Load...", self.container_file_select)
        self.input_file_one = QLineEdit(self.container_file_select)

        self.container_file_one.addWidget(self.label_file_one)
        self.container_file_one.addWidget(self.open_file_one)
        self.container_file_one.addWidget(self.input_file_one)

        self.layout_vert_select.addLayout(self.container_file_one)

        ## File Two ##
        self.container_file_two = QHBoxLayout()

        self.label_file_two = QLabel("File Two: ", self.container_file_select)
        self.open_file_two = QPushButton("Load...", self.container_file_select)
        self.input_file_two = QLineEdit(self.container_file_select)

        self.container_file_two.addWidget(self.label_file_two)
        self.container_file_two.addWidget(self.open_file_two)
        self.container_file_two.addWidget(self.input_file_two)

        self.layout_vert_select.addLayout(self.container_file_two)


        self.layout_vert_main.addWidget(self.container_file_select)



        ### Settings ###
        # TODO: get tabs from ./tabs

        self.container_settings = QWidget(self.container_main)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.container_settings.sizePolicy().hasHeightForWidth())

        self.container_settings.setSizePolicy(sizePolicy)

        self.layout_grid_settings = QGridLayout(self.container_settings)
        
        self.container_tabs = QTabWidget(self.container_settings)

        # Insert tabs here #

        self.layout_grid_settings.addWidget(self.container_tabs, 0, 0, 1, 1)

        self.layout_vert_main.addWidget(self.container_settings)

        
        ### Output ###
        self.container_output = QWidget(self.container_main)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.container_output.sizePolicy().hasHeightForWidth())

        self.container_output.setSizePolicy(sizePolicy)

        self.layout_hor_output = QHBoxLayout(self.container_output)

        self.label_output = QLabel("Output: ", self.container_output)
        self.button_select_output = QPushButton("Select...", self.container_output)
        self.input_output_dir = QLineEdit(self.container_output)
        self.button_merge = QPushButton("Merge", self.container_output)

        self.layout_hor_output.addWidget(self.label_output)
        self.layout_hor_output.addWidget(self.button_select_output)
        self.layout_hor_output.addWidget(self.input_output_dir)
        self.layout_hor_output.addWidget(self.button_merge)

        self.layout_vert_main.addWidget(self.container_output)
        
