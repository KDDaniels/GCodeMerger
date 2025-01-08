#!/usr/bin/env python

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

import sys
from PyQt6.QtWidgets import QApplication

from ui.Main_Window import Main_Window

application_title = "GCodeMerger"
application_version = "0.1.0"

"""
Main function
Runs the program
"""
def main(title: str, version: str):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    main_window = Main_Window((title + " v" + version))
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main(application_title, application_version)