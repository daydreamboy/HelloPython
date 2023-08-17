#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def test_expanduser(path):
    print(os.path.expanduser(path))


def test_join(path1, path2):
    print(os.path.join(path1, path2))


if __name__ == '__main__':
    test_expanduser('~')
    test_expanduser('/aaa')
    test_join(os.path.expanduser('~'), 'some_folder')

