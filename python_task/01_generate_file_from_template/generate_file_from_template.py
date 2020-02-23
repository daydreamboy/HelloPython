import argparse
import os
import logging
import json
import collections
import datetime
import objective_c_tool
import placeholder


def generate(file_name, class_name, key_path, task_type):
    my_parser = argparse.ArgumentParser(
        description='Generate Objective-C class files(.h/m) from JSON',
        epilog='If any problem about this program, feel free to contact me. Enjoy the program!')
    my_parser.version = '1.0'

    my_parser.add_argument('-c', '--classname', default=class_name, help='the class name')
    my_parser.add_argument('-f', '--filename', default=file_name, help='the file name')
    my_parser.add_argument('-m', '--methodName', default='presetData', help='the class method name')
    my_parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose info')
    my_parser.add_argument('--version', action='version')
    my_parser.add_argument('-d', '--debug', action='store_true', help='Print debugging info')

    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument('-p', '--path', help='The path of JSON file')
    my_group.add_argument('-s', '--string', help='The content string of JSON')

    args = my_parser.parse_args()
    file_path = args.path
    json_string = args.string
    class_name = args.classname
    file_name = args.filename
    method_name = args.methodName
    is_debug = args.debug

    # check None: @see https://stackoverflow.com/a/3965129
    if not (json_string is None):
        if len(json_string) > 0:
            json_object = json.loads(json_string, parse_int=str)
        else:
            logging.error(f"The JSON string is empty: `{json_string}`")
            return 1
    else:
        if not (file_path is None) and len(file_path) > 0 and not os.path.exists(file_path):
            logging.error(f"The path not exists: {file_path}")
            return 1

        with open(file_path, 'r') as file:
            json_object = json.load(file, parse_int=str)

    try:
        target_json_object = json_object[key_path]
    except KeyError:
        logging.error(f"Get value by data.model.templates failed. Please check json object:\n{json_object}")
        return 1

    if not isinstance(target_json_object, list):
        logging.error(f"data.model.templates is not a list. Please check json object:\n{target_json_object}")
        return 1

    if is_debug:
        print(target_json_object)
        print(json.dumps(target_json_object))
        print('----------------')

    result_json_object = {}
    for item in target_json_object:
        if task_type == 'template':
            if isinstance(item, dict) and 'id' in item:
                result_json_object[item['id']] = item
        else:
            if isinstance(item, dict) and 'list' in item:
                layout_group = item['list']
                if isinstance(layout_group, list):
                    for layout_item in layout_group:
                        if isinstance(layout_item, dict) and 'id' in layout_item:
                            key = f"prefix_{layout_item['id']}"
                            ordered_layout_item = collections.OrderedDict(sorted(layout_item.items()))
                            value = {'rawDict': ordered_layout_item}
                            value.update(layout_item)
                            value['type'] = int(layout_item['type'])
                            value['version'] = int(layout_item['version'])
                            result_json_object[key] = collections.OrderedDict(sorted(value.items()))

    ordered_json_object = collections.OrderedDict(sorted(result_json_object.items()))
    literal_string = objective_c_tool.generate_literal_oc_string(ordered_json_object, 0, 0, 2, False, True)

    timestamp = datetime.datetime.now()
    comment_string = placeholder.comment_string(__file__, timestamp)

    h_file_string = placeholder.h_file_string(comment_string, class_name, method_name)
    m_file_string = placeholder.m_file_string(comment_string, class_name, method_name, literal_string)

    if is_debug:
        print(h_file_string)
        print('---------------------------------------------')
        print(m_file_string)

    # @see https://stackoverflow.com/a/5214587
    with open(f"{file_name}.h", 'w') as file:
        file.write(h_file_string)

    with open(f"{file_name}.m", 'w') as file:
        file.write(m_file_string)

    print(f"Generated {file_name}.h/m files successfully!")

    return 0

