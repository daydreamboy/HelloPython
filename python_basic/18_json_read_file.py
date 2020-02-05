
import argparse
import json
import sys
import os
import logging


def main():
    my_parser = argparse.ArgumentParser(description='Parse JSON from file')
    my_parser.add_argument('-p', '--path', help='The path of JSON file', required=True)

    args = my_parser.parse_args()
    file_path = args.path

    if os.path.exists(file_path):
        # @see https://stackoverflow.com/a/38644565
        with open(file_path, 'r') as f:
            json_object = json.load(f)
            print(json_object)
    else:
        logging.error(f"The path not exists: {file_path}")

    return 1


if __name__ == '__main__':
    sys.exit(main())
