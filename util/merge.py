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

import re

# TODO: change to allow any number of files to be input and merged
class Merger:
    def __init__(self):
        self.current_layer = 0
        self.output_code = ""

    def merge_gcode(self, file_one, file_two, output, settings):
        """
        Merges the G-code from the selected files and outputs to output

        Args:
            file_one : path to G-code file
            file_two : path to G-code file
            output   : path to output file
            settings : list of settings to apply
        """
        one_lines = self.read_file(file_one)
        two_lines = self.read_file(file_two)

        one_layers = self.get_line_index(one_lines, r"^;LAYER:\d+")
        two_layers = self.get_line_index(two_lines, r"^;LAYER:\d+")

        start = "".join(one_lines[:one_layers[0]-1])
        self.output_code += start

        one = "".join(one_lines[one_layers[0]+1:one_layers[1]-1])
        two = "".join(two_lines[two_layers[0]+1:two_layers[1]-1])
        self.build_gcode(one, two, ";TEST\n;PAUSE\n;INJECTION", self.current_layer)

        self.current_layer += 1
        
        one = "".join(one_lines[one_layers[1]+1:one_layers[2]-1])
        two = "".join(two_lines[two_layers[1]+1:two_layers[2]-1])
        self.build_gcode(one, two, ";TEST\n;PAUSE\n;INJECTION", self.current_layer)


        self.write_file(output, self.output_code)
    
        # for key, value in settings.items():
        #     print(f"key: {key}\nval: {value}")

        


    def read_file(self, file_name):
        with open(file_name, "r") as f:
            file_lines = f.readlines()
            f.close()

        return file_lines
    
    def write_file(self, file_name, data):
        with open(file_name, "w") as f:
            f.write(data)
            f.close()


    def get_line_index(self, lines, arg):
        """
        Returns a list of indices indicating layer changes
        """
        index_list = [
            i for i, line in enumerate(lines)
            if re.match(arg, line)
        ]
        
        return index_list

    def get_code_block(self, lines, layers, current_layer):
        """
        Returns the code between current_layer and current_layer+1
        """
        start = layers[current_layer]
        end = layers[current_layer + 1]

        block = lines[start+1:end]
        block = "".join(block)
        return block
    
    def build_gcode(self, color_one_code, color_two_code, pause, layer):
        # TODO: dynamically handle the color numbers for future expansion
        # e.g. multiple colors, whatnot
        color_one = f";LAYER:{layer} COLOR:1\n" + color_one_code
        color_two = f";LAYER:{layer} COLOR:2\n" + color_two_code
        self.output_code += color_one + f"{pause}\n" + color_two




if __name__ == "__main__":
    one = "E:\\ProgrammingStuff\\Projects\\GCodeInjector\\input\\test1.gcode"
    two = "E:\\ProgrammingStuff\\Projects\\GCodeInjector\\input\\test2.gcode"
    out = "E:\\ProgrammingStuff\\Projects\\GCodeInjector\\output\\output.gcode"
    settings = {"key":"val"}
    merger = Merger()
    merger.merge_gcode(one, two, out, settings)