"""dump tool for debugging

1.
PYTHONPATH=~/GitHub_Projects/HelloPython/python_tool python3 test_dump_tool.py

2.
export PYTHONPATH=$HOME/GitHub_Projects/HelloPython/python_tool

3.
import sys
sys.path.append('/path/to/whatever')

@see https://stackoverflow.com/a/5875962

"""

import inspect
import re


def dump_object(var):
    frame_info = inspect.getframeinfo(inspect.currentframe().f_back)
    valid = False
    for line in frame_info[3]:
        m = re.search(r'\bdump_object\s*\(\s*([A-Za-z_][A-Za-z0-9_.]*)\s*\)', line)
        if m:
            valid = True
            filename = frame_info[0]
            line_number = frame_info[1]
            variable_name = m.group(1)
            variable_type = type(var)

            print(f"[Debug] {filename}:{line_number}: {variable_name} = ({variable_type}) {var}")

    if not valid:
        print(f"[Error] parse variable failed. Its value is {var}. frame_info: {frame_info}")

