# myls.py

import argparse
import sys
import os

# Create the parser
my_parser = argparse.ArgumentParser(
    prog='myls',
    usage='%(prog)s [options] path',
    epilog='Enjoy the program!',
    description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')
my_parser.add_argument('-l', '--long', action='store_true', help='enable the long listing format')
my_parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)
