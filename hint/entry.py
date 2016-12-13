# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import click


@click.command()
@click.argument('file')
@click.option('--ignore', default='',
              help='The error codes which will be ignored.')
@click.option('--format', default='json',
              help='The output format of error information.')
def hint_entry(file, ignore, format):
    click.echo('file: %s, ignore: %s, format: %s' % (file, ignore, format))


def run():
    hint_entry()


if __name__ == '__main__':
    run()
