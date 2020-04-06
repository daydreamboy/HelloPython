#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""dump tool for debugging

非同级目录引用其他模块，有三种方式

1. 执行python，加上PYTHONPATH环境变量
PYTHONPATH=~/GitHub_Projects/HelloPython/python_tool python2 test_dump_tool2.py

2. 在shell配置文件中（`.bashrc`, `.bash_profile`, etc），设置PYTHONPATH环境变量
export PYTHONPATH=$HOME/GitHub_Projects/HelloPython/python_tool

3. 在import other_module语句之前，将该other_module模块所在文件夹路径，加入到sys.path中
import sys
sys.path.append('/path/to/whatever')

@see https://stackoverflow.com/a/5875962

"""

import inspect
import re
import sys


# @see https://stackoverflow.com/a/592849
def dump_object(var):
    frame_info = inspect.getframeinfo(inspect.currentframe().f_back)
    valid = False
    for line in frame_info[3]:
        m = re.search(r'\bdump_object\s*\(\s*(.+)\s*\)', line)
        if m:
            valid = True
            file_name = frame_info[0]
            line_number = frame_info[1]
            variable_name = m.group(1)
            variable_type = type(var)

            print('[Debug] {file_name}:{line_number}: {variable_name} = ({variable_type}) {var}'.format(file_name=file_name, line_number=line_number, variable_name=variable_name, variable_type=variable_type, var=var))

    if not valid:
        print(frame_info)
        #print("[Error] parse variable failed. Its value is {var}. frame_info: {frame_info}".format(var=var, frame_info=frame_info))

