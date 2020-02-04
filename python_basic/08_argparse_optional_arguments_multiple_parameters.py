# Usage:
# $ python3 08_argparse_optional_arguments_multiple_parameters.py --input 4 3 2


import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments with fixed multiple parameters
my_parser.add_argument('--input', action='store', type=int, nargs=3)

# nargs can be assigned the following strings
# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
# argparse.REMAINDER: all the values that are remaining in the command line

# Execute the parse_args() method
args = my_parser.parse_args()

print(args.input)
