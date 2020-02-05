
import argparse
import json
import sys
import os
import logging


def main():
    my_parser = argparse.ArgumentParser(description='Read JSON from file')
    my_parser.add_argument('-p', '--path', help='The path of JSON file', required=True)

    args = my_parser.parse_args()
    file_path = args.path

    if not os.path.exists(file_path):
        logging.error(f"The path not exists: {file_path}")
        return 1

    # @see https://stackoverflow.com/a/38644565
    with open(file_path, 'r') as file:
        json_object = json.load(file)
        for item in json_object:
            print(item)
        print(json_object)

    return 1


if __name__ == '__main__':
    sys.exit(main())
