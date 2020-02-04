# Usage:
# $ python3 10_argparse_optional_arguments_ranged_value.py -a head -b 4
# Namespace(a='head', b=4)

import argparse

# Create the parser
my_parser = argparse.ArgumentParser()
my_group = my_parser.add_mutually_exclusive_group(required=True)

# Add the exclusive arguments
# Note: -v/-s only one can appear
my_group.add_argument('-v', '--verbose', action='store_true')
my_group.add_argument('-s', '--silent', action='store_true')

# Execute the parse_args() method
args = my_parser.parse_args()

print(vars(args))
