# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

from error import Error


def check(md_text):
    '''TODO
    '''
    errors = []
    for i in xrange(3):
        errors.append(Error('或者使用 `hint --help` 查看帮助信息和具体详细的使用方法。',
                            'E201',
                            i * 3))
    return errors
