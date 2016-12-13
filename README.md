# hint

> A simple **markdown** lint / hint `cli-tool`, for markdown developer integrated with travis.
 
> 一个简单的 **markdown** 静态检查的控制台 `cli` 工具，可以方便 markdown 开发者轻松集成 travis 自动检测。

[![Latest Stable Version](https://img.shields.io/pypi/v/hint.svg)](https://pypi.python.org/pypi/hint) [![Build Status](https://travis-ci.org/hustcc/hint.svg?branch=master)](https://travis-ci.org/hustcc/hint) 


## 一、安装

> **pip install hint**

然后在系统中会得到一个 `hint` 的命令 cli 工具。


## 二、使用

简单使用方法如下：

> **hint markdown_file**

或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。

```shell
$ hint --help
Usage: hint-script.py [OPTIONS]

Options:
  --ignore TEXT  The error codes which will be
                 ignored.
  --format TEXT  The output format of error
                 information.
  --help         Show this message and exit.

```


## 三、错误码

检查规则来源于 [chinese-copywriting-guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines) ，错误码命名方式参考于 flake8 。目前支持的错误码如下所示：

| 错误码 | 检查类型 | 详细描述 |
| ------ | ------ | ------ |
| E101   | 空格 | 中英文之间需要增加空格 |
| E102   | 空格 | 中文与数字之间需要增加空格 |
| E103   | 空格 | 数字与单位之间需要增加空格 |
| E104   | 空格 | 全角标点与其他字符之间不加空格 |
| E201   | 标点符号 | 不重复使用标点符号 |
| E301   | 全角半角 | 使用全角中文标点 |
| E302   | 全角半角 | 数字使用半角字符 |
| E403   | 全角半角 |遇到完整的英文整句、特殊名词，其內容使用半角标点 |

关于各种错误码的正确、错误范例，可以参考 [tests](tests)。


# LICENSE

MIT @[hustcc](https://github.com/hustcc).