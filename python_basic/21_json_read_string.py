# Usage:
# $ python3 20_json_read_string.py -s "[1, 2, 3]"

import argparse
import json
import sys
import os
import logging


def main():
    my_parser = argparse.ArgumentParser(description='Read JSON from string')
    my_parser.add_argument('-s', '--string', help='The JSON string', required=True)

    args = my_parser.parse_args()
    json_string = args.string

    if len(json_string) <= 0:
        logging.error(f"The JSON string is empty: {json_string}")
        return 1

    # @see https://stackoverflow.com/a/4528110
    json_object = json.loads(json_string)
    print(json_object)

    return 1


if __name__ == '__main__':
    sys.exit(main())
