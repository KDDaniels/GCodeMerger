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

from PyQt6.QtWidgets import QMainWindow

class Main_Window(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(100, 100, 500, 400)
        
        
        