# Usage:
# $ python3 09_argparse_positional_optional_arguments_default_value.py
# $ python3 09_argparse_positional_optional_arguments_default_value.py me you us

import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('input', action='store', nargs='*', default='my default value')

# Execute the parse_args() method
args = my_parser.parse_args()

print(args.input)