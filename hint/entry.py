# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import click
import sys
import hint
import utils


@click.command()
@click.argument('file', type=click.File(encoding='utf-8'))
@click.option('--ignore', default='',
              help='The error codes which will be ignored.')
@click.option('--format', default='text',
              type=click.Choice(['text', 'json']),
              help='The output format of error information.')
def hint_entry(file, ignore, format):
    md_text = file.read()

    errors = hint.check(md_text)

    errors = utils.ignore_errorcode(errors, ignore)

    utils.echo_error(errors, format)

    sys.exit(len(errors) and 1 or 0)


def run():
    hint_entry()


if __name__ == '__main__':
    run()
