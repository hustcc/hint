# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''
import functools
import error


def pre_process(md_text):
    '''TODO: pre process the mark down text string.
    '''
    # remove code block
    md_text = md_text or ''
    return md_text


def to_paragraph_array(md_text):
    '''TODO: parse mark down file, and return all the paragraph array'''
    md_text = pre_process(md_text)
    md_lines = md_text.split('\n')

    paragraph = [line for line in md_lines if line.strip() != '']
    return paragraph


def reduce_handler(tokens, current):
    '''TODO: how to reduce to get token strings.'''
    tokens.append(current)
    return tokens


def tokenizer(p):
    '''parse each mark down text line, get the tokenizer of the line'''
    tokens = functools.reduce(reduce_handler, p, [])
    return tokens


def detect_errors(tokens):
    '''TODO: detect error code from tokens.'''
    errors = []
    for i in xrange(3):
        errors.append(error.Error('或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。',
                                  'E201', i * 3))
    return errors
