# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import hint
import utils


__version__ = '1.0.0'


def check(text, ignore='', format='json', fn='anonymous'):
    '''check markdown text'''
    # check results
    errors = hint.check(text)
    # ignores
    errors = utils.ignore_errorcode(errors, ignore)
    # format output array / dict
    errors = {fn: utils.format_errors(errors, format)}
    if format != 'json':
        errors = ['File:%s\n%s' % (k, '\n'.join(es))
                  for k, es in errors.items()
                  if len(es) > 0]
        errors = '\n\n'.join(errors)
    return errors


def check_file(fn, ignore='', format='json'):
    '''check markdown file'''
    with open(fn) as f:
        text = f.read()
        return check(text, ignore, format, fn=fn)
