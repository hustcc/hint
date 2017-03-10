# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''
from __future__ import absolute_import
from hint import hint, utils
import click
import sys
import json
import os


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-i', '--ignore', default='',
              help='The error codes which will be ignored.')
@click.option('-f', '--format', default='text',
              type=click.Choice(['text', 'json']),
              help='The output format of error information.')
@click.option('-m', '--max-depth', default=3,
              type=click.INT,
              help='The max depth for traverse the path.')
def hint_entry(file, ignore, format, max_depth):
    files = []
    if os.path.isdir(file):
        # 遍历 n 层，获得所有的 .md 文件
        files = utils.traversing_path_norecursive([],
                                                  file,
                                                  max_depth=max_depth)
    elif os.path.isfile(file):
        files.append(file)

    errors_dict = {}  # check results
    cnt = 0
    for fn in files:
        # check files & ignore
        errors = hint.check_file(fn, ignore)
        cnt += len(errors)
        errors_dict[fn] = errors

    # format output array / dict
    edi = errors_dict.items()
    errors_dict = {
        fn: utils.format_errors(errors, format) for fn, errors in edi
    }
    # success or fail
    fail = cnt and True or False
    errors = ''  # errors text to be console.log
    if format == 'json':
        errors = json.dumps(errors_dict, indent=2)
    else:
        errors = ['File:%s\n%s' % (k, '\n'.join(es))
                  for k, es in errors_dict.items()
                  if len(es) > 0]
        errors = '\n\n'.join(errors)
    # echo
    click.echo(fail and errors or '^_^ No Hint, well done.')

    sys.exit(fail and 1 or 0)


def run():
    hint_entry()


if __name__ == '__main__':
    run()
