# -*- coding: utf-8 -*-
import setuptools  # noqa
from distutils.core import setup
import io
import re
import os


DOC = '''
## 一、安装

> **pip install hint**

然后在系统中会得到一个 `hint` 的命令 cli 工具。


## 二、使用

简单使用方法如下：

> **hint markdown_file**

或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。

'''


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(name='hint',
      version=find_version('hint/__init__.py'),
      description=('A simple markdown lint / hint `cli-tool`, ',
                   'for markdown developer integrated with travis.'),
      long_description=DOC,
      author='hustcc',
      author_email='i@hust.cc',
      url='https://github.com/hustcc',
      license='MIT',
      install_requires=[
        'click'
      ],
      classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
      ],
      keywords='hint, lint, markdown, rules, error',
      include_package_data=True,
      zip_safe=False,
      packages=['hint', 'hint.detector'],
      entry_points={
        'console_scripts': ['hint=hint.cli:run']
      })
