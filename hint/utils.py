# -*- coding: utf-8 -*-
'''
Created on 2016年12月13日

@author: hustcc
'''


def is_latin(c):
    '''decide c is latin or not
    '''
    return ord(c) < 256


def is_space(c):
    '''decide c is space
    '''
    return c == ' '


def ignore_errorcode(errors, ignores):
    '''ignore the errors in ignores
    '''
    if not isinstance(ignores, list):
        ignores = ignores.split(',')
    # trim the error code
    ignores = [code.strip() for code in ignores]
    # ignore error codes.
    errors = [error for error in errors if error.code not in ignores]
    return errors


def format_errors(errors, format):
    return [e.format(format) for e in errors]
