# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import hint
import utils


__version__ = '0.0.1'


def check(text, ignore='', format='json'):
    # check results
    errors = hint.check(text)
    # ignores
    errors = utils.ignore_errorcode(errors, ignore)
    # format output array / dict
    errors = utils.format_errors(errors, format)
    if format != 'json':
        errors = '\n'.join(errors)
    return errors
