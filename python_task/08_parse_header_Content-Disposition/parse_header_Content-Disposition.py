#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.parse

# 定义正则表达式
filename_pattern = r'filename=(?P<filename>[^;]*)(;|$)|filename\*=UTF-8\'\'(?P<filename_utf8>[^;]*)'

# 测试字符串
test_strings = [
    'Content-Disposition: attachment; filename="example.txt"',
    'Content-Disposition: attachment; filename*=UTF-8\'\'example%20file.txt',
    'Content-Disposition: attachment; filename="example.txt"; filename*=UTF-8\'\'example%20file.txt'
]

# 解析并输出结果
for test_string in test_strings:
    print(f"---test_string: {test_string}")
    matches = re.findall(filename_pattern, test_string)
    for match in matches:
        if match[0]:  # 说明匹配的是 filename
            filename = match[0].strip('"')  # 去掉引号
            filename = urllib.parse.unquote(filename)
            print(f"Found filename: {filename}")
        if match[2]:  # 说明匹配的是 filename*
            filename_utf8 = match[2]
            filename_utf8 = urllib.parse.unquote(filename_utf8)
            print(f"Found UTF-8 filename: {filename_utf8}")