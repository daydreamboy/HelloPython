#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

def generate_exports(folder_path):
    # 创建一个列表以存储 export 语句
    export_statements = []

    # 遍历指定文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 只处理 .ts 或 .ets 文件
            if file.endswith('.ts') or file.endswith('.ets'):
                # 获取相对路径
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                # 使用 os.path.splitext() 去掉扩展名
                module_name, _ = os.path.splitext(relative_path)
                # 生成 export 语句
                export_line = f'export * from "./{module_name}"'
                export_statements.append(export_line)

    # 输出 export 语句到命令行
    for statement in export_statements:
        print(statement)

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='遍历指定文件夹，生成 TypeScript 或 ETS export 语句。')
    parser.add_argument('folder_path', type=str, help='要遍历的文件夹路径')
    args = parser.parse_args()

    generate_exports(args.folder_path)