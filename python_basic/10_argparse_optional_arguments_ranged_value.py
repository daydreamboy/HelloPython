# Usage:
# $ python3 10_argparse_optional_arguments_ranged_value.py -a head -b 4
# Namespace(a='head', b=4)

import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('-a', action='store', choices=['head', 'tail'], required=True)
my_parser.add_argument('-b', action='store', type=int, choices=range(1, 5), required=True)

# Execute the parse_args() method
args = my_parser.parse_args()

print(args)