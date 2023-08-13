#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# History:
#   2016-11-12 wesley_chen new version of parsing Podfile.lock
#   01b,9Nov.2016,caonian   Parser Podfile.lock instead of OneTravelPods.rb
#   01a,30Oct.2016,caonian  Initial version
#
# Usage:
#   1. Place theone_summary_pod_info.py along with Podfile.lock inside the same folder
#   2. Type command as followings:
#       python theone_summary_pod_info.py <folder containing json file>
#   3. Xcode -> Run Script
#       python "$PROJECT_DIR/theone_summary_pod_info.py"
#
# 1、<project root>/Pods/ONEDebugKit_<xcworkspace name>/Pod/Assets/tag_summary.json
# 2、<project root>/Pods/ONEDebugKit/Pod/Assets/tag_summary.json
# 3、根目录

import os
import sys
import logging
import json
from collections import OrderedDict
import argparse

## The format of the Podfile.lock
# PODS:
# ...
# DEPENDENCIES:
# ...
# SPEC REPOS:
# ...
# EXTERNAL SOURCES:
# ...
# SPEC CHECKSUMS:
# ...
# PODFILE CHECKSUM: ...
# COCOAPODS: ...
# 

# Note: different version of cocoapods, the format of the Podfile.lock is slightly different

PODS='PODS'
DEPENDENCIES='DEPENDENCIES'
COCOAPODS='COCOAPODS'
SPEC_CHECKSUMS='SPEC CHECKSUMS'
PODFILE_CHECKSUM='PODFILE CHECKSUM'
EXTERNAL_SOURCES='EXTERNAL SOURCES'
SPEC_REPOS='SPEC REPOS'
SEPARATOR=':'

def main():
    args = run_command_parser()
    run_podfile_lock_file_parser(args.path, args)


def get_section_string(file_content, start_string, end_string):
    start_index = file_content.index(start_string) + len(start_string)
    content = file_content[start_index:]
    end_index = content.find(end_string) + len(end_string)
    section_string = content[:end_index]

    return section_string

def get_PODS_components(cocoapods_version, file_content):
    FISRT_LEVEL_PREFIX = '  - '
    SECOND_LEVEL_PREFIX = '    - '

    PODS_components_list = []

    PODS_string = get_section_string(file_content, f"{PODS}{SEPARATOR}", '\n\n')
    line_list = PODS_string.splitlines()
    index = 0
    while index < len(line_list):
        line = line_list[index]
        if line.strip() == '':
            index += 1
            continue

        if not line.startswith(FISRT_LEVEL_PREFIX):
            index += 1
            continue

        pod_name = line.strip(" -:").split(" ")[0]
        pod_version = line.strip(" -:").split(" ")[1].strip("()")

        pod_info_dict = {
            'pod_name': pod_name,
            'pod_version': pod_version,
        }

        if line.endswith(":"):
            next_index = index + 1
            dependency_pod_list = []
            while next_index < len(line_list):
                next_line = line_list[next_index]
                if next_line.startswith(SECOND_LEVEL_PREFIX):
                    components = next_line.split("(")
                    assert len(components) == 1 or len(components) == 2, f"{components} must have one or tow elements"

                    dependency_pod_name = components[0].strip(" -")
                    if len(components) == 2:
                        dependency_pod_version = components[1].strip(")")
                        dependency_pod_info = {
                            'pod_name': dependency_pod_name,
                            'pod_version': dependency_pod_version,
                        }
                    else:
                        dependency_pod_info = {
                            'pod_name': dependency_pod_name,
                        }
                    dependency_pod_list.append(dependency_pod_info)
                    next_index += 1
                else:
                    break

            index = next_index
            if len(dependency_pod_list):
                pod_info_dict["pod_dependencies"] = dependency_pod_list
        else:
            index += 1
        PODS_components_list.append(pod_info_dict)

    return PODS_components_list


def get_DEPENDENCIES_components(cocoapods_version, file_content):
    LEVEL_PREFIX = '  - '

    DEPENDENCIES_string = get_section_string(file_content, f"{DEPENDENCIES}{SEPARATOR}", '\n\n')
    line_list = DEPENDENCIES_string.splitlines()

    dependency_list = []
    for line in line_list:
        if line.strip() == '':
            continue

        if not line.startswith(LEVEL_PREFIX):
            continue
        
        components = line.strip(" -").split('(')
        assert len(components) == 1 or len(components) == 2, f"{components} must only have one or two elements"
        pod_name = components[0].strip(' -')
        # Note: pod_version maybe from local source code, 
        # and maybe have words ["from", "tag", "branch", "commit"]

        if len(components) == 2:
            pod_version = components[1].strip(')')
            pod_info = {
                'pod_name': pod_name,
                'pod_version': pod_version,
            }
        else:
            pod_info = {
                'pod_name': pod_name,
            }
        dependency_list.append(pod_info)

    return dependency_list


def get_SPEC_CHECKSUMS_components(cocoapods_version, file_content):
    SPEC_CHECKSUMS_string = get_section_string(file_content, f"{SPEC_CHECKSUMS}{SEPARATOR}", '\n\n')
    line_list = SPEC_CHECKSUMS_string.splitlines()
    line_list = [x for x in line_list if x.strip()]

    podspec_checksum_list = []
    for x in line_list:
        components = x.split(':')
        assert len(components) == 2, f"{components} must only have two elements"
        checksum_info = {
            "pod_name": components[0].strip(),
            "checksum": components[1].strip(),
        }
        podspec_checksum_list.append(checksum_info)

    return podspec_checksum_list


def get_cocoapods_version(file_content):
    COCOAPODS_string = file_content[file_content.index(f"{COCOAPODS}") :]
    line_list = COCOAPODS_string.splitlines()
    line_list = [x for x in line_list if x.strip()]
    line_list = line_list[0].split(":")
    assert len(line_list) == 2, f"{line_list} must only have two elements"
    version = line_list[1].strip()

    return version


def run_podfile_lock_file_parser(podfile_lock_file_path, args):
    logging.info("Podfile.lock path: %s" % podfile_lock_file_path)

    if not os.path.isfile(podfile_lock_file_path):
        logging.error("%s is not exist!" % podfile_lock_file_path)
        sys.exit(0)
        return
    
    with open(podfile_lock_file_path) as f:
        file_content = f.read()
        f.close()
    
    cocoapods_version = get_cocoapods_version(file_content)
    print(f"cocoapods_version = {cocoapods_version}")
    PODS_components = get_PODS_components(cocoapods_version, file_content)
    print(f"1 = {cocoapods_version}")

    DEPENDENCIES_components = get_DEPENDENCIES_components(cocoapods_version, file_content)
    print(f"2 = {cocoapods_version}")

    SPEC_CHECKSUMS_components = get_SPEC_CHECKSUMS_components(cocoapods_version, file_content)
    print(f"3 = {cocoapods_version}")

    if args.json_output_file.strip():
        out_file = open(args.json_output_file, "w")
        json_list = [
            { PODS: PODS_components },
            { DEPENDENCIES: DEPENDENCIES_components },
            { SPEC_CHECKSUMS: SPEC_CHECKSUMS_components },
        ]
        out_file.writelines(json.dumps(json_list))
        out_file.close()

    return

def run_command_parser():
    my_parser = argparse.ArgumentParser(description='Parse the Podfile.lock file')
    my_parser.add_argument('-p', '--path', help='The path of Podfile.lock file', required=True)
    my_parser.add_argument('-d', '--debug', action='store_true', help='The debug mode')
    my_parser.add_argument('-j', '--json-output-file', help='The path of output JSON file', required=False)
    args = my_parser.parse_args()
    return args

if __name__ == '__main__':
    sys.exit(main())
