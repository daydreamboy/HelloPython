#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

# 执行另一个Python脚本并获取输出结果
output = subprocess.check_output(["python3", "callee.py"])
output = output.decode('utf-8')

# 输出结果
print(f"result: `{output}`")
