# Python Notes

[TOC]

## 1、Python语法



### （1）module[^10]（模块）

#### module分类

Python定义module，有三种方式

* Python的单个文件
* 用C写的module，然后运行时加载。例如re（regular expression）module
* builtin module模块，包含在Python编译器（interpreter）中。例如itertools module

上面三种模块都用import语句导入。



#### module的搜索路径

当使用`import mod`语句时，Python编译器搜索mod.py的顺序，如下

* 当前输入脚本的所在文件夹，或者运行python交互环境的当前文件夹
* PYTHONPATH环境变量中列出文件夹路径，可以有多个，类似PATH环境变量
* Python安装时所配置的文件夹路径，一般是Python安装目录

搜索路径可以用`sys.path`来确认，例如

```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages']
```

因此，为了能引用到对应的python文件，可以将文件放在上面三种搜索对应的地方。

除此之外，可以运行时来修改`sys.path`，来引用到对应的python文件。例如

```python
>>> sys.path.append(r'C:\Users\john')
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages', 'C:\\Users\\john']
>>> import mod
```



#### 确认module的所在位置

每个module有`__file__`变量，用于表示该文件所在的路径。例如

```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'

>>> import re
>>> re.__file__
'C:\\Python36\\lib\\re.py'
```





#### Python单个文件模块

​       Python的单个文件是一个模块（module），在同级目录下，当前模块可以直接引用其他模块，有两种引用方式，如下

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

非同级目录引用其他模块，有三种方式[^4]，如下

* 执行python，加上PYTHONPATH环境变量

```shell
$ PYTHONPATH=~/GitHub_Projects/HelloPython/python_tool python3 test_dump_tool.py
```

* 在shell配置文件中（`.bashrc`, `.bash_profile`, etc），设置PYTHONPATH环境变量

```shell
export PYTHONPATH=$HOME/GitHub_Projects/HelloPython/python_tool
```

* 在import other_module语句之前，将该other_module模块所在文件夹路径，加入到sys.path中

```python
import sys
sys.path.append('/path/to/whatever')

# Ok, other_module can be found
import other_module
```



### （2）字符串（string）



#### f-strings格式

Python 3.6引入f-strings语法[^5]，支持字符串中替换变量，举个例子如下

```python
a = 'Hello'
b = 'world'

if __name__ == '__main__':
    print(f"{a}, {b}!")
    print(f"{a}, {{b}}!")
```

说明

> 1. 如果要对`{`和`}`进行转义，可以使用`{{`和`}}`表示[^9]







### （3）内置函数（builtin function）

#### type函数

type函数可以检查变量类型[^6]



#### isinstance函数

判断实例对象是否属于某些类型



#### print函数

print可以传入任意多个参数，默认用空格分隔。

举个例子

```python
print('[Debug]', message)
```



函数签名，如下

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```



### （4）内置常量

#### \__file__常量

\__file__表示当前脚本的路径。举个例子，如下

```python
def test__file__():
    print(__file__)  # ./27_module__file__.py if python ./27_module__file__.py
    print(os.path.basename(__file__))  # 27_module__file__.py
    print(os.path.splitext(os.path.basename(__file__))[0])  # 27_module__file__
```

> 示例代码，见27_module\__file__.py 







## 2、Python常用库



### （1）argparse[^7]

​        argparse是Python3.2+内置模块（module），用于替换optparse。argparse用于解析命令行参数，产生帮助和使用信息，以及产生错误提示。



#### 介绍CLI参数

CLI（Command Line Interface）定义命令行工具的参数协议，对于命令行参数分为下面两种

* optional argument，可选参数（也可以配置为必选），多个可选参数和顺序无关，示例格式为`-h`或`--help`。
* positionnal argument，固定参数（可以必选或可选），多个固定参数和顺序有关

说明

> 可选参数的参数，称为parameter，示例如`--level 2`。



#### argparse使用步骤

1. import argparse模块
2. 创建parser
3. parser添加optional和positional参数
4. parser执行parse_args()方法



#### ArgumentParser参数详解

ArgumentParser是argparse module中的类，用于创建parser。这个类的构造参数（可选），如下

* prog：程序的名称。默认是sys.argv[0]
* usage：用法提示。默认自动生成
* description：程序描述
* epilog：结束语，位于参数描述的下面
* prefix_chars：可选参数的前缀符号。默认是`-`
* fromfile_prefix_chars：用于调试时，指定参数文件（命令行参数存到文件中）的前缀符号，例如`@`
* add_help：是否自动添加`-h/--help`可选参数。默认是True
* allow_abbrev：是否允许可选参数简写，即在没有歧义下，`--help`可以写为`--he`、`--hel`等。默认是True



#### add_argument参数详解

add_argument是ArgumentParser实例的方法，用于添加parser的需要解析的参数。



##### 添加optional argument

```python
my_parser.add_argument('-l', '--long')
```

需要两个参数，同时有前缀



##### 添加positional argument

```python
my_parser.add_argument('Path')
```

需要一个参数，区分大小写



add_argument方法的其他参数，如下

* metavar：参数的名称，参数释义中显示的标识
* type：参数按照指定类型解析。默认是字符串类型
* required：是否必选。默认是False
* action：解析的特定操作。默认是store
  * store，按照指定类型存储
  * store_const（需要额外指定const），按照常量（const）的值存储
  * store_true，存储True
  * store_false，存储False
  * append，允许多个相同的可选参数，存储到同一个list中
  * append_const（需要额外指定const），允许多个相同的可选参数，存储常量（const）的值到同一个list中
  * count，允许多个相同的可选参数，计算个数，将个数存储
  * help，打印帮助信息并退出程序
  * version，打印版本信息并退出程序

* nargs：指定可选参数的个数，支持数字和通配符
  * ?，一个或者无
  * *，任意多个
  * +，至少一个
  * argparse.REMAINDER，剩余所有的参数

* default：设置默认值

* choices：指定参数的值在某个范围中，例如`choices=['head', 'tail']`、`choices=range(1, 5)`
* dest：my_parser.parse_args()返回对象中对应参数的属性名



#### argparse示例程序

```python
import argparse
import sys
import os

# Create the parser
my_parser = argparse.ArgumentParser(
    prog='myls',
    usage='%(prog)s [options] path',
    epilog='Enjoy the program!',
    prefix_chars='/',
    description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')
my_parser.add_argument('/v', '//verbose', action='store_true', help='an optional argument')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
```



#### 执行argparse.py报错的问题

举个例子，如下

```shell
$ python3 argparse.py 
Traceback (most recent call last):
  File "argparse.py", line 1, in <module>
    import argparse
  File "/.../argparse.py", line 7, in <module>
    parser = argparse.ArgumentParser(description='Process some integers.')
AttributeError: module 'argparse' has no attribute 'ArgumentParser'
```

原因：python文件名和系统module名冲突。优先认为当前文件argparse.py是argparse模块，它里面没有ArgumentParser属性，因此报错。

解决方法：重命名python文件[^2]



### （2）json[^8]

Python内置库提供json模块，用于处理JSON。



#### 文件和JSON之间序列化和反序列化

* 读JSON文件（json.load）

```python
with open(file_path, 'r') as file:
    json_object = json.load(file)
```



* 写JSON文件（json.dump）

```python
with open(file_path, 'w') as file:
    json.dump(data, file, indent=indent, separators=separators, sort_keys=sort_keys)
```



#### 字符串和JSON之间序列化和反序列化

* 读JSON字符串

```python
json_object = json.loads(json_string)
```



* 写JSON字符串

```python
json_string = json.dumps(data, indent=indent, separators=separators, sort_keys=sort_keys)
```



##### 压缩JSON

```python
json.dumps(jsonObj, separators=(',', ':'), ensure_ascii=False, sort_keys=True).encode('utf8')
```

separators默认是`(', ', ': ')`，这里去掉后面的空格。





### （3）collections





### （4）datetime



### （5）os.path

| 函数       | 作用              |
| ---------- | ----------------- |
| join       | 拼接path          |
| expanduser | 展开path中的~符号 |



> 示例代码，见27_module_os_path.py



## pip命令



| 命令                      | 作用    |
| ------------------------- | ------- |
| pip install --upgrade pip | 更新pip |



## 附录

### （1）PyCharm使用常见问题

#### 自定义module，不被PyCharm识别，产生报错提示[^3]

在右键选中对应module所在文件夹，Mark Directory > Sources Root

> In the project explorer, right-click on the directory that you want import. Then select `Mark Directory As` and select `Sources Root`.





## References

[^1]:https://stackoverflow.com/a/7948504
[^2]:https://stackoverflow.com/questions/6605851/argparse-module-not-working-in-python
[^3]:https://stackoverflow.com/questions/5875810/importerror-when-trying-to-import-a-custom-module-in-python

[^4]:https://stackoverflow.com/a/5875962
[^5]:https://stackoverflow.com/a/4450610
[^6]:https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type

[^7]:https://realpython.com/command-line-interfaces-python-argparse/

[^8]:https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

[^9]:https://stackoverflow.com/a/42521252

[^10]:https://realpython.com/python-modules-packages/











