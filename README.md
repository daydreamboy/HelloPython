# Python Notes

[TOC]

## 1、Python语法



### （1）模块（module）

#### 模块

Python的单个文件是一个模块（module），在同级目录下，当前模块可以直接引用其他模块，有两种引用方式，如下

- 导入模块

```python
# my_module.py
import my_module

my_module.function()
```

- 导入函数

```python
# my_module.py
from my_module import function

function()
```

说明

> 导入模块，调用函数需要指定模块名；导入函数，则不需要，但存在函数名冲突的情况。
>
> 示例代码，02_import_module.py和03_import_function.py



#### 包和模块的关系[^1]

模块（module）是单个文件，而包（package）是一组模块的集合。



#### 非同级目录引用模块





## 2、Python常用库



### （1）argparse

​        argparse是Python3.2+内置模块（module），用于替换optparse。argparse用于解析命令行参数，产生帮助和使用信息，以及产生错误提示。



https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script





## pip命令



| 命令                      | 作用    |
| ------------------------- | ------- |
| pip install --upgrade pip | 更新pip |



## 附录





## References

[^1]:https://stackoverflow.com/a/7948504
[^2]:https://stackoverflow.com/questions/6605851/argparse-module-not-working-in-python
[^3]:https://stackoverflow.com/questions/5875810/importerror-when-trying-to-import-a-custom-module-in-python



