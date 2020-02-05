
import argparse
import json
import sys
import os
import logging


data = {'people': []}
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})


def main():
    my_parser = argparse.ArgumentParser(description='Write JSON to string')
    my_parser.add_argument('-p', '--path', help='The path of input JSON file', required=True)
    my_parser.add_argument('-k', '--keyOrdered', action='store_true',
                           help='Sort key by order. Default is not unordered')

    my_group = my_parser.add_mutually_exclusive_group()
    my_group.add_argument('-i', '--indent', type=int, default=None,
                          help='The indent width of JSON. Default is literal print, not indent')
    my_group.add_argument('-c', '--compact', action='store_true', help='Output compact string of JSON')

    args = my_parser.parse_args()
    file_path = args.path
    indent = args.indent
    # compact JSON: @see https://stackoverflow.com/a/33233406
    # ternary operator: @see https://stackoverflow.com/a/394814
    separators = (',', ':') if args.compact else (', ', ': ')
    sort_keys = args.keyOrdered

    if not os.path.exists(file_path):
        logging.error(f"The file not exists: {file_path}")
        return 1

    json_string = json.dumps(data, indent=indent, separators=separators, sort_keys=sort_keys)
    print(json_string)

    return 1


if __name__ == '__main__':
    sys.exit(main())
