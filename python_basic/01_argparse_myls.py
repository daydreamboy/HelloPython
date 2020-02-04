# myls.py

import argparse
import sys
import os

# Create the parser
my_parser = argparse.ArgumentParser(
    prog='myls',
    usage='%(prog)s [options] path',
    epilog='Enjoy the program!',
    prefix_chars='/',
    description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
