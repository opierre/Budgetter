import os
import subprocess

if __name__ == '__main__':

    # Store relative path
    absolute_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'skeletons')

    # Build list with all UI files to convert
    ui_files = ["MainWindow", "Options", "Dialog"]

    for ui_file in ui_files:
        # Build cmd line
        cmd_line = ["uic.exe", os.path.join(absolute_path, ui_file + ".ui"), "-g", "python",
                    "-o", os.path.join(absolute_path, ui_file + ".py")]

        # Execute cmd line
        subprocess.run(cmd_line)
