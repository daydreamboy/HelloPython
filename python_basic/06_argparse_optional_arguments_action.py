# Usage:
#
# $ python3 06_argparse_optional_arguments_action.py -a 42
# {'a': '42', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
#
# $ python3 06_argparse_optional_arguments_action.py -e 1 -e 2
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': ['1', '2'], 'f': None, 'g': None}
#
# $ python3 06_argparse_optional_arguments_action.py -f -f
# $ python3 06_argparse_optional_arguments_action.py -ff
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': [42, 42], 'g': None}
#
# $ python3 06_argparse_optional_arguments_action.py -g -g
# $ python3 06_argparse_optional_arguments_action.py -gg
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 2}


import argparse

# Create the parser
my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'

# Add the arguments
my_parser.add_argument('-a', action='store')  # store what it is as string
my_parser.add_argument('-b', action='store_const', const=42)  # store 42 when -b appear
my_parser.add_argument('-c', action='store_true')  # store True when -c appear
my_parser.add_argument('-d', action='store_false')  # store False when -d appear
my_parser.add_argument('-e', action='append')  # store multiple -e <any> as list and require one parameter at least
my_parser.add_argument('-f', action='append_const', const=42)  # store multiple -f as list and each one stands for 42
my_parser.add_argument('-g', action='count')  # count the number of -g and store the count as integer
my_parser.add_argument('-i', action='help')  # show help as -h and exit
my_parser.add_argument('-j', action='version')  # show version and exit


# Execute the parse_args() method
args = my_parser.parse_args()

print(vars(args))
