# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

import parsing
import functools


def do_paragraph(errors, p):
    tokens = parsing.tokenizer(p)
    new_errors = parsing.detect_errors(tokens)
    return errors + new_errors


def check(text):
    '''check the error in mark down text
    '''
    paragraph = parsing.to_paragraph_array(text)
    # reduce to detect errors.
    return functools.reduce(do_paragraph, paragraph, [])
