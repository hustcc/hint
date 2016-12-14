# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''
import functools
import error
import utils


def pre_process(md_text):
    '''pre process the mark down text string.
    '''
    return md_text or u''


def to_paragraph_array(md_text):
    '''parse mark down file, and return all the paragraph array'''
    md_text = pre_process(md_text)
    # change to unicode
    if type(md_text) is not unicode:
        md_text = md_text.decode('utf-8')

    md_lines = md_text.split('\n')
    # filter not empty element
    return [line for line in md_lines if line.strip()]


def reduce_handler(token, c):
    '''TODO: how to reduce to get token strings.'''
    tokens = token[0]
    pre_token = token[1]

    type = utils.typeof(c)
    print type
    # if is the first char of token, return for next
    if pre_token is False:
        token[1] = {'type': type, 'text': c}
        return token

    # if not the first char of token
    # 需要判断各种不同情况下，不同 type 组合的类型，状态机
    tokens
    return token


def tokenizer(p):
    '''parse each mark down text line, get the tokenizer of the line'''
    tokens = functools.reduce(reduce_handler, p, [[], False])
    return tokens


def detect_errors(tokens):
    '''TODO: detect error code from tokens.'''
    errors = []
    for i in xrange(3):
        errors.append(error.Error(u'或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。',
                                  'E201', i * 3))
    return errors
