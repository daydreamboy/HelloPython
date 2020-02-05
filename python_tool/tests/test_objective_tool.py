# Usage:
# $ python3 test_objective_tool.py -p json.txt


import argparse
import sys
import os
import logging
import json
import objective_c_tool


def main():
    my_parser = argparse.ArgumentParser(
        description='Generate Objective-C literal string from JSON',
        epilog='If any problem about this program, feel free to contact me. Enjoy the program!')
    my_parser.version = '1.0'

    my_parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose info')
    my_parser.add_argument('--version', action='version')
    my_parser.add_argument('-d', '--debug', action='store_true', help='Print debugging info')

    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument('-p', '--path', help='The path of JSON file')
    my_group.add_argument('-s', '--string', help='The content string of JSON')

    args = my_parser.parse_args()
    file_path = args.path
    json_string = args.string
    is_debug = args.debug

    # check None: @see https://stackoverflow.com/a/3965129
    if not (json_string is None):
        if len(json_string) > 0:
            json_object = json.loads(json_string)
        else:
            logging.error(f"The JSON string is empty: `{json_string}`")
            return 1
    else:
        if not (file_path is None) and len(file_path) > 0 and not os.path.exists(file_path):
            logging.error(f"The path not exists: {file_path}")
            return 1

        with open(file_path, 'r') as file:
            json_object = json.load(file)

    target_json_object = json_object

    if is_debug:
        print(target_json_object)
        print(json.dumps(target_json_object))
        print('----------------')

    literal_string = objective_c_tool.generate_literal_oc_string(target_json_object, 0, 0, 2, False, True)
    print(literal_string)

    return 1


if __name__ == '__main__':
    sys.exit(main())

