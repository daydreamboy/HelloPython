#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json5  # 确保你已经安装了 json5 库
from collections import defaultdict

# 定义要忽略的包名的正则表达式
IGNORE_PATTERNS = [
    r'@kit\..*',      # 匹配所有以 @kit. 开头的包名
    r'@ohos\..*',     # 匹配所有以 @ohos. 开头的包名
    r'@ohos\/hypium'  # 精确匹配 @ohos/hypium
]

def should_ignore(package_name):
    """检查包名是否匹配任何要忽略的模式"""
    for pattern in IGNORE_PATTERNS:
        if re.match(pattern, package_name):
            return True
    return False

def parse_ets_file(file_path):
    package_imports = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # 使用正则表达式匹配 import 语句（只匹配以 @ 开头的包名）
            match = re.search(r'import\s*{([\s\S]*?)}\s*from\s*["\'](@[^"\']+)["\']', line)
            if match:
                # 提取 import 内容和包名
                imported_items = match.group(1).replace(' ', '').split(',')  # 去掉空格
                package_name = match.group(2)
                for item in imported_items:
                    package_imports.append((file_path, line_number, package_name, item))
    return package_imports

def find_json5_and_related_ets_files(folder_path):
    ets_files = []
    module_info_list = []  # 用于存储所有 module.json5 的信息
    # 遍历文件夹查找所有 module.json5 文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file == 'module.json5':
                json5_path = os.path.join(root, file)
                # 读取 module.json5 的内容
                with open(json5_path, 'r', encoding='utf-8') as json5_file:
                    module_info = json5.load(json5_file)  # 使用 json5 库解析
                    module_info_list.append(module_info)  # 存储信息
            elif file.endswith('.ets'):
                ets_files.append(os.path.join(root, file))  # 保存 .ets 文件路径
    return ets_files, module_info_list

def group_imports_by_package(imports):
    package_dict = defaultdict(list)
    for file_path, line_number, package_name, item in imports:
        package_dict[package_name].append((file_path, line_number, item))
    return package_dict

def main():
    # 设置命令行参数解析
    import argparse
    parser = argparse.ArgumentParser(description='递归解析 ETS 文件中的包导入信息')
    parser.add_argument('folder_path', type=str, help='包含 module.json5 文件的文件夹路径')
    args = parser.parse_args()

    ets_files, module_info_list = find_json5_and_related_ets_files(args.folder_path)

    # 打印所有 module.json5 的内容
    for module_info in module_info_list:
        print("模块名称:", module_info.get("module", {}).get("name"))
        print("设备类型:", ", ".join(module_info.get("module", {}).get("deviceTypes", [])))
        print("请求权限:", ", ".join([perm.get("name") for perm in module_info.get("module", {}).get("requestPermissions", [])]))
        print("\n")

    all_imports = []

    for ets_file in ets_files:
        imports = parse_ets_file(ets_file)
        all_imports.extend(imports)

    grouped_imports = group_imports_by_package(all_imports)

    # 排序包名并输出，忽略在白名单中的包名
    package_names = sorted(grouped_imports.keys())
    
    ignored_packages = []  # 存储被忽略的包名

    for package_name in package_names:
        if should_ignore(package_name):
            ignored_packages.append(package_name)  # 记录被忽略的包名
            continue  # 跳过忽略的包名
        
        print(f"包名: {package_name}")

    print(f"\n")

    # 打印结果，忽略在白名单中的包名
    for package_name in package_names:
        if should_ignore(package_name):
            continue  # 跳过忽略的包名
        
        print(f"\n包名: {package_name}")
        for file_path, line_number, item in grouped_imports[package_name]:
            print(f"  文件: {file_path}, 行号: {line_number}, 引用: {item}")

    # 打印被忽略的包名
    if ignored_packages:
        print("\n被忽略的包名:")
        for ignored in ignored_packages:
            print(f"  {ignored}")

if __name__ == "__main__":
    main()