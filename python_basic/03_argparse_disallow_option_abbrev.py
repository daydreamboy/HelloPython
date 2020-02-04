# Usage:
# $ python3 03_argparse_disallow_option_abbrev.py

import argparse

# Note: allow_abbrev=True by default
my_parser = argparse.ArgumentParser(allow_abbrev=False)

# Note: required=True indicates the --input is required
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(f"input = {args.input}")
print(f"id = {args.id}")

