#!/usr/bin/python3
# -*- coding: utf-8 -*-

import importlib


def main():
    module_name = '27_module___name__callee'  # 以数字开头的脚本名字
    module = importlib.import_module(module_name)
    module.do_something()


if __name__ == '__main__':
    main()
