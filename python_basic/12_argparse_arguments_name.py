# Usage:
# $ python3 12_argparse_arguments_name.py -h

import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
# Note: metavar to name the argument
my_parser.add_argument('-v', '--verbosity', action='store', type=int, metavar='LEVEL')
my_parser.add_argument('-s', '--silent', action='store_true')

# Execute the parse_args() method
args = my_parser.parse_args()

print(vars(args))
