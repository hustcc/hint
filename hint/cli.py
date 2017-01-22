# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import click
import sys
import hint
import utils
import json


@click.command()
@click.argument('file', type=click.File(encoding='utf-8'))
@click.option('--ignore', default='',
              help='The error codes which will be ignored.')
@click.option('--format', default='text',
              type=click.Choice(['text', 'json']),
              help='The output format of error information.')
def hint_entry(file, ignore, format):
    md_text = file.read()
    # check results
    errors = hint.check(md_text)
    # ignores
    errors = utils.ignore_errorcode(errors, ignore)
    # format output array / dict
    errors = utils.format_errors(errors, format)

    if format == 'json':
        errors = json.dumps(errors, indent=2)
    else:
        errors = '\n'.join(errors)
    # echo
    click.echo(errors or '^_^ No Hint, well done.')

    sys.exit(len(errors) and 1 or 0)


def run():
    hint_entry()


if __name__ == '__main__':
    run()
