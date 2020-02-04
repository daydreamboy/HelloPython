# Usage:
# $ python3 02_argparse_read_arguments_from_file.py @args.txt

import argparse

my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

my_parser.add_argument('a', help='the first argument')
my_parser.add_argument('b', help='the second argument')
my_parser.add_argument('c', help='the third argument')
my_parser.add_argument('d', help='the fourth argument')
my_parser.add_argument('e', help='the fifth argument')

my_parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument')

# execute parse_args()
args = my_parser.parse_args()

print(args)

print(f"-v = {args.verbose}")
print(f"a = {args.a}")
print(f"b = {args.b}")
print(f"c = {args.c}")
print(f"d = {args.d}")
print(f"e = {args.e}")

