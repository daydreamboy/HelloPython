# Usage:
# $ python3 13_argparse_arguments_set_variable_name.py -v 1 -s 3

import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
# Note: dest to rename variable name for the  argument
my_parser.add_argument('-v', '--verbosity', action='store', type=int, dest='my_verbosity_level')
my_parser.add_argument('-s', '--silent', action='store', type=int)

# Execute the parse_args() method
args = my_parser.parse_args()

print(vars(args))
print(args.my_verbosity_level)
print(args.silent)
