# Usage:
# $ python3 04_argparse_disable_auto_help.py

import argparse

# Note: add_help=False makes -h/--help not work
my_parser = argparse.ArgumentParser(add_help=False)

# Note: required=True indicates the --input is required
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(f"input = {args.input}")
print(f"id = {args.id}")

