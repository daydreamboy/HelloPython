#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_function(i):
    print(f"{my_function.__name__} called: i = {i}")


def main():
    my_function(1)


if __name__ == '__main__':
    main()
