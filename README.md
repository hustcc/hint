# hint

> A simple **markdown** lint / hint `cli-tool`, for markdown developer integrated with travis.
 
> 一个简单的 **markdown** 静态检查的控制台 `cli` 工具，可以方便 markdown 开发者轻松集成 travis 自动检测。

[![Latest Stable Version](https://img.shields.io/pypi/v/hint.svg)](https://pypi.python.org/pypi/hint) [![Build Status](https://travis-ci.org/hustcc/hint.svg?branch=master)](https://travis-ci.org/hustcc/hint) 


## 一、安装

> **pip install hint**

然后在系统中会得到一个 `hint` 的命令 cli 工具。


## 二、使用

使用方法有两种：

**2.1 一种是`命令行 cli 方式`**，简单使用方法如下：

> **hint markdown_file**

或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。

```shell
$ hint --help
Usage: hint-script.py [OPTIONS] FILE

Options:
  -i, --ignore TEXT         The error codes which will be ignored.
  -f, --format [text|json]  The output format of error information.
  -m, --max-depth INTEGER   The max depth for traverse the path.
  --help                    Show this message and exit.

```

可以用于直接集成到各种 ci 系统中，例如 travis-ci。

**2.2 另外一种是`代码 API 调用的方式`**，简单使用方法如下：

```py
import hint

text='''
hint 是一个简单的 **markdown** 静态检查的控制台 `cli` 工具。
可以方便 markdown 开发者轻松集成 travis 自动检测。
'''
errors = hint.check(text, ignore='E201')

fn = 'README.md'
errors = hint.check_file(fn, format='text')
```

可以方便的进行第三方扩展开发。


## 三、错误码

检查规则来源于 [chinese-copywriting-guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines)，错误码命名方式参考于 flake8。目前支持的错误码如下所示：

| 错误码 | 检查类型 | 详细描述 | 完成 |
| ------ | ------ | ------ | ------ |
| E101   | 空格 | 中英文之间需要增加空格 | done |
| E102   | 空格 | 中文与数字之间需要增加空格 | done |
| E103   | 空格 | 全角标点与其他字符之间不加空格 | done |
| E104   | 空格 | 除了％、℃、°、以及倍数单位（如 2x、3n）之外，数字与单位之间需要增加空格 | done |
| E201   | 标点 | 不重复使用标点符号 | done |
| E202   | 标点 | 只有中文或中英文混排中，一律使用中文全角标点 | done |
| E203   | 标点 | 如果出现整句英文，则在这句英文中使用英文、半角标点 | done |
| E204   | 标点 | 省略号请使用……标准用法 | done |
| E205   | 标点 | 英文和后面的半角标点之间不需要空格 | done |
| E301   | 数字 | 数字使用半角字符 | done |

关于各种错误码的正确、错误范例，可以参考 [tests](tests)。**目前有了大概的代码结构，欢迎 PR 更多的检查错误类型和检查方式**。


# LICENSE

MIT @[hustcc](https://github.com/hustcc).