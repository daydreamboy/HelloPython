# Python Notes

[TOC]

## 1、Python语法

### (1) 模块[^10]（module）

#### a. module分类

Python定义module，有三种方式

* 单个Python文件作为模块
* 用C写的module，然后运行时加载。例如re（regular expression）module
* builtin module模块，包含在Python编译器（interpreter）中。例如itertools module

上面三种模块都用import语句导入。



#### b. module的搜索路径

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



#### c. 确认module的所在位置

每个module有`__file__`变量，用于表示该文件所在的路径。例如

```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'

>>> import re
>>> re.__file__
'C:\\Python36\\lib\\re.py'
```



#### d. 单个Python文件作为模块

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



#### e. 包和模块的关系[^1]

模块（module）是单个文件，而包（package）是一组模块的集合。



#### f. 非同级目录引用其他模块

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



### (2) 字符串（string）



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
> 1. f-strings语法也支持单引号的字符串，例如print(f'{a}, {b}!')



#### format函数

Python2的str类提供实例方法format，用于格式化字符串。format函数签名，如下

```python
str.format(*args, **kwargs)
```

format函数可以接受任意多个参数。

format函数的调用字符串，是必现符合特定格式化语法的字符串，类似C的printf函数。

格式化字符串语法[^13]（Format String Syntax），如下

```
format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```



TODO

https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-a-string-and-also-use-format



#### split函数

split函数的签名，如下

```python
// Python 2
str.split([sep[, maxsplit]])
// Python 3
str.split(sep=None, maxsplit=- 1)
```

* sep，表示分隔符。默认可以没有
* maxsplit，表示分隔的次数

关于maxsplit参数，举个例子，如下

```python
if __name__ == '__main__':
    string = 'a b c'
    print(string.split())  # ['a', 'b', 'c']
    print(string.split(None))  # ['a', 'b', 'c']
    print(string.split(None, 1))  # ['a', 'b c']
```

> 示例代码，见25_builtin_type_str_split.py





### (3) 内置函数（builtin function）

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





### (4) 内置属性（attribute）

#### a. `__file__`属性

`__file__`表示当前脚本的路径。举个例子，如下

```python
def test__file__():
    print(__file__)  # ./27_module__file__.py if python ./27_module__file__.py
    print(os.path.basename(__file__))  # 27_module__file__.py
    print(os.path.splitext(os.path.basename(__file__))[0])  # 27_module__file__
```

> 示例代码，见27_module\__file__.py 



#### b. `__name__`属性

##### 1. 模块的`__name__`属性

`__name__`表示当前模块的名字，它是可以被修改的，不是固定的值。

目前有两种情况：

* 直接执行脚本，那么`__name__`是`__main__`。例如python脚本经常遇到的范式，如下

  ```python
  def main():
      # 一些代码逻辑
  
  if __name__ == '__main__':
      main()
  ```

* 使用import导入脚本，那么`__name__`是脚本的名字，去掉py扩展名

举个例子，如下

`27_module___name__callee.py`脚本的内容

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def do_something():
    print(f"__name__ = {__name__}")


if __name__ == '__main__':
    do_something()
```

* 如果直接执行这个脚本，则输出

```shell
$ ./27_module___name__callee.py
__name__ = __main__
```

* 如果导入这个脚本，调用脚本中的do_something函数，则输出

```shell
$ ./27_module___name__caller.py 
__name__ = 27_module___name__callee
```

说明

> import不支持以数字开头的脚本名字，则使用importlib模块完成这种特殊的情况。`27_module___name__caller.py `的内容，如下
>
> ```python
> #!/usr/bin/python3
> # -*- coding: utf-8 -*-
> 
> import importlib
> 
> 
> def main():
>     module_name = '27_module___name__callee'  # 以数字开头的脚本名字
>     module = importlib.import_module(module_name)
>     module.do_something()
> 
> 
> if __name__ == '__main__':
>     main()
> 
> ```
>
> 一般情况直接使用import语句



##### 2. 函数的`__name__`属性

函数也有内置`__name__`属性，它的值是函数名，没有参数列表

举个例子，如下

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def my_function(i):
    print(f"{my_function.__name__} called: i = {i}")


def main():
    my_function(1)


if __name__ == '__main__':
    main()
```







## 2、Python常用模块

### (1) argparse[^7]

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



### (2) json[^8]

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



#### 压缩JSON[^11]

```python
json.dumps(jsonObj, separators=(',', ':'), ensure_ascii=False, sort_keys=True).encode('utf8')
```

separators默认是`(', ', ': ')`，这里去掉后面的空格。





### (3) collections





### (4) datetime



### (5) os.path

| 函数       | 作用              |
| ---------- | ----------------- |
| join       | 拼接path          |
| expanduser | 展开path中的~符号 |



> 示例代码，见27_module_os_path.py



### (6) venv

venv是Python3内置的虚拟环境管理工具，可以帮助用户创建虚拟环境，隔离不同Python项目所使用的依赖包。

```
python -m venv venv_name
```



```
source venv_name/bin/activate
```



```
pip install requests
```



```
python script.py
```



```
deactivate
```



### (7) subprocess

#### a. 执行其他脚本

subprocess提供check_output函数，用于执行脚本并获取结果。

举个例子，如下

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

# 执行另一个Python脚本并获取输出结果
output = subprocess.check_output(["python3", "callee.py"])
output = output.decode('utf-8')

# 输出结果
print(f"result: `{output}`")
```

callee.py的内容，如下

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('{"Hello":"World"}', end="")
```



### (8) logging

#### a. 修改日志级别

举个例子，如下

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


def test_default_log_level():
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_change_log_level():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('This is DEBUG')
    logging.info('This is INFO')
    logging.warning('This is WARNING')
    logging.error('This is ERROR')
    logging.critical('This is CRITICAL')


def test_custom_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('This is DEBUG')
    logger.info('This is INFO')
    logger.warning('This is WARNING')
    logger.error('This is ERROR')
    logger.critical('This is CRITICAL')


test_default_log_level()
print('-----------')
test_change_log_level()
print('-----------')
test_custom_logger()
```







## 3、Python常用三方库

### (1) python-gitlab

安装方法：

```shell
$ pip3 install python-gitlab
```



#### gitlab v3 API



https://www.cnblogs.com/40kuai/p/9378038.html



### (2)  python-dotenv

安装方法：

```shell
$ pip3 install python-dotenv
```

使用方法：

* 和python脚本同级下，配置`.env`文件

举个例子，如下

```properties
array=["element1","element2"]
string = 'This is a string' # some comment
```

* 代码导入dotenv模块，以及相关函数

举个例子，如下

```python
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
array = json.loads(os.getenv('array'))
string = os.getenv('string')
```

代码上其他使用方式，参考[官方文档](https://pypi.org/project/python-dotenv/)



## 4、常见任务

### (1) 设置python为python3

在macOS 12.3上，已经没有Python 2，但是有些历史脚本还是使用python。因此，需要设置python别名，指向python3命令。

```shell
$ which python3
/usr/local/bin/python3
$ ll | grep python      
lrwxr-xr-x  1 wesley_chen  wheel    40B Apr 18 19:21 python3 -> ../Cellar/python@3.11/3.11.3/bin/python3
...
$ ln -s python3 /usr/local/bin/python 
```

说明

> 1. ln命令的格式：ln  -s source_file target_file
> 2. 使用alias方法，需要修改很多shell的资源文件，不能一劳永逸



### (2) Python 2和Python 3共存使用

在macOS 12.3上，已经没有Python 2，可以使用`pyenv`来维护多个版本的python

按照下面几个步骤使用Python 2[^14]

* 安装pyenv，`brew install pyenv`
* 列出Python所有版本，`pyenv install --list`
* 安装最新Python2的版本，`pyenv install 2.7.18`

* 列出pyenv已安装的Python所有版本，`pyenv versions`

  ```shell
  $ pyenv versions
  * system (set by /Users/wesley_chen/.pyenv/version)
    2.7.18
  ```

* 将python命令设置2.7.18版本

  ```shell
  $ pyenv global 2.7.18
  ```

* 到这里，pyenv不会修改python，依然找不到python命令。根据使用的shell配置对应资源文件，添加一行`eval "$(pyenv init --path)"`

  * zsh，`~/.zshrc`或`~/.zprofile`

    ```shell
    $ python --version
    Python 2.7.18
    $ python3 --version
    Python 3.11.3
    $ pyenv versions
      system
    * 2.7.18 (set by /Users/wesley_chen/.pyenv/version)
    ```

  * bash，`~/.bash_profile`

    ```shell
    $ bash
    bash-3.2$ python --version
    Python 2.7.18
    bash-3.2$ python3 --version
    Python 3.11.3
    bash-3.2$ pyenv versions  
      system
    * 2.7.18 (set by /Users/wesley_chen/.pyenv/version)
    ```

说明

> 配置shell资源文件，需要重新打开terminal



### (3) 添加自定义源

这里使用pip3的user级别的配置，添加自定义源。在`~/.pip/pip.conf`文件，添加下面内容

```properties
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

这里使用清华大学提供pypi源。

如果有多个源，可以按照下面方式配置[^16]，如下

```properties
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
               pypi.tuna.tsinghua.edu.cn
extra-index-url= https://pypi.tuna.tsinghua.edu.cn/simple
```

参考这篇文章[^17]提供的国内的源，如下

```properties
阿里云: https://mirrors.aliyun.com/pypi/simple/
清华: https://pypi.tuna.tsinghua.edu.cn/simple/
中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学: https://pypi.hustunique.com/
山东理工大学: https://pypi.sdutlinux.org/ 
豆瓣: https://pypi.douban.com/simple/
```



## 5、常见问题

### (1) pip3 search报错

执行`pip3 search`命令会报错，如下

```shell
$ pip3 search gitlab
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead. See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
```

参考这里文章的解释[^15]，官方停用pip search命令，推荐使用浏览器打开https://pypi.org/search来查询。

解决方法：安装pip-search包，使用pip_search搜索，如下

```shell
$ pip3 install pip-search
$ pip_search gitlab
                      🐍 https://pypi.org/search/?q=gitlab 🐍                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Package                 ┃ Version        ┃ Released   ┃ Description                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┃ 📂 gitlab3              │ 0.5.8          │ 18-03-2017 │ GitLab API v3 Python Wrapper.┃
...
```

根据提示信息，可以知道pip_search也是通过查询https://pypi.org/search/得到数据



## 附录

### (1) 安装python3

安装前，python3使用系统默认的python3，如下

```shell
$ which python3
/usr/bin/python3
$ python3 --version        
Python 3.9.6
```

使用Homebrew安装python3

```shell
$ brew install python3
```

安装后，如下

```shell
$ which python3
/usr/local/bin/python3
$ python3 --version   
Python 3.11.3
```

说明

> 使用Homebrew安装python3，也自动安装pip3命令，如下
>
> ```shell
> $ which pip3
> /usr/local/bin/pip3
> $ pip3 --version
> pip 23.0.1 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
> ```
>
> 



### (2) pip命令

| 命令                      | 作用    |
| ------------------------- | ------- |
| pip install --upgrade pip | 更新pip |



### (3) `pip.conf`文件

pip3（后面简称pip）提供三种方式，配置pip3命令的参数

* 命令行参数
* 环境变量
* `pip.conf`配置文件

这里主要介绍`pip.conf`配置文件。完整文档可以参考这篇[官方文档](https://pip.pypa.io/en/stable/topics/configuration/)

`pip.conf`配置文件有三种配置级别：

* global（全局）
* user（用户）
* site

在MacOS系统上面这三种级别配置，对应的`pip.conf`文件路径，如下

* global

```shell
/Library/Application Support/pip/pip.conf
```

* user

```shell
# 优先使用这个路径
$HOME/Library/Application Support/pip/pip.conf
# 其次使用这个路径
$HOME/.config/pip/pip.conf
```

* site

```shell
$VIRTUAL_ENV/pip.conf
```

环境变量`PIP_CONFIG_FILE`，可以指定`pip.conf`配置文件的路径。



#### a. `pip.conf`文件加载顺序

`pip.conf`文件加载，按照下面的顺序

- `PIP_CONFIG_FILE`环境变量
- Global
- User
- Site

后者总是覆盖前者，应该是根据相同的key，进行值覆盖。



#### b. `pip.conf`文件的格式

`pip.conf`文件的格式。举个例子，如下

```properties
[global]
timeout = 60
index-url = https://download.zope.org/ppix

[install]
ignore-installed = true
no-dependencies = yes

[freeze]
timeout = 10
```



#### c. `pip3 config`命令

`pip3 config`命令，用于管理本地和全局配置。它可以查看和编辑`pip.conf`文件。`pip3 config`命令对应的官方文档在[这里](https://pip.pypa.io/en/stable/cli/pip_config/)

使用下面命令，可以查看完整的`pip3 config`命令的帮助信息

```shell
$ pip3 help config
```

查看`~/.config/pip/pip.conf`，如下

```shell
$ pip3 config list
global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
install.trusted-host='pypi.tuna.tsinghua.edu.cn'
```

如果`pip3 config`命令不提供`--user`、`--global` 或 `--site`，该命令默认是user级别。

`~/.config/pip/pip.conf`的实际内容，如下

```properties
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```





### (4) 常用pip包

#### a. cocoapods-graph[^12]

安装

```shell
$ sudo pip install cocoapods-graph
```



使用

```shell
$ cocoapods-graph -f Podfile.lock --html
Saving html file...
done
```





### (4) PyCharm使用常见问题

#### a. 自定义module，不被PyCharm识别，产生报错提示[^3]

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

[^11]:https://stackoverflow.com/a/16311587

[^12]:https://pypi.org/project/cocoapods-graph/

[^13]:https://docs.python.org/2.7/library/string.html#formatstrings

[^14]:https://stackoverflow.com/questions/71591971/how-can-i-fix-the-zsh-command-not-found-python-error-macos-monterey-12-3

[^15]:https://www.jianshu.com/p/0d55f82d8d08
[^16]:https://stackoverflow.com/questions/30889494/can-pip-conf-specify-two-index-url-at-the-same-time
[^17]:https://zhuanlan.zhihu.com/p/404529640







