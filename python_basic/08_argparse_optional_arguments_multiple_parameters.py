# Usage:
# $ python3 08_argparse_optional_arguments_multiple_parameters.py --input 4 3 2
# Namespace(input=[1, 3, 4], others=[])
#
# $ python3 08_argparse_optional_arguments_multiple_parameters.py --input 1 3 4 d ef
# Namespace(input=[1, 3, 4], others=['d', 'ef'])
#
# $ python3 08_argparse_optional_arguments_multiple_parameters.py d --input 1 3 4
# Namespace(input=None, others=['d', '--input', '1', '3', '4'])


import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments with fixed multiple parameters
my_parser.add_argument('--input', action='store', type=int, nargs=3)
my_parser.add_argument('others', action='store', nargs=argparse.REMAINDER)

# nargs can be assigned the following strings
# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
# argparse.REMAINDER: all the values that are remaining in the command line

# Execute the parse_args() method
args = my_parser.parse_args()

print(args)
