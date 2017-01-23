# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import parsing
import functools
import utils


def do_paragraph(errors, p):
    tokens = parsing.tokenizer(p)
    new_errors = parsing.detect_errors(tokens, p)
    return errors + new_errors


def check(text):
    '''check the error in mark down text
    '''
    paragraph = parsing.to_paragraph_array(text)
    # reduce to detect errors.
    return functools.reduce(do_paragraph, paragraph, [])


def check_file(fn, ignore):
    '''check the error in mark down fn
    '''
    with open(fn) as f:
        text = f.read()
        errors = check(text)
        return utils.ignore_errorcode(errors, ignore)
