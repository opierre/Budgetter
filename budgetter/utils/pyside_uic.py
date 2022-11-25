import fileinput
import os
import subprocess

if __name__ == '__main__':
    # Store strings to convert
    strings_to_convert = {
        "from view": "from budgetter.view",
        "(u\"": "(\"",
        ", u\"": ", \""
    }

    # Store relative path
    absolute_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'skeletons')

    # Build list with all UI files to convert
    ui_files = [file for file in os.listdir(absolute_path) if file.endswith('.ui')]

    for ui_file in ui_files:
        # UI file
        file_to_convert = os.path.join(absolute_path, ui_file)

        # PY file
        file_converted = os.path.join(absolute_path, ui_file[:-3] + ".py")

        # Build cmd line
        cmd_line = ["pyside6-uic.exe", file_to_convert, "-g", "python", "-o", file_converted]

        # Execute cmd line
        subprocess.run(cmd_line)

        # Open generated file and replace strings
        with fileinput.input(files=(file_converted,), inplace=True) as f:
            for line in f:
                for key, replacement in strings_to_convert.items():
                    if key in line:
                        line = line.replace(key, replacement)
                print(line, end='')
