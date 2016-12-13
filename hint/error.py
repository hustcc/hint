# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

errors = {
    'E101': 'E101',
    'E102': 'E101',
    'E103': 'E101',
    'E104': 'E101',
    'E201': 'E101',
    'E301': 'E101',
    'E302': 'E101',
    'E401': 'E101'
}


class Error(object):
    def __init__(self, text, code, error_index):
        self.text = text
        self.code = code
        self.error_index = error_index

    def description(self):
        return errors.get(self.code, 'unknow')

    def short_text(self, length=20):
        text_len = len(self.text)
        half_len = length / 2

        start = self.error_index - half_len
        start = start > 0 and start or 0

        end = start + length
        end = end > text_len and text_len or end

        return '...%s...' % self.text[start:end]

    def json_format(self):
        rst = {}
        rst['code'] = self.code
        rst['text'] = self.short_text()
        rst['error_index'] = self.error_index
        rst['description'] = self.description()
        return rst

    def text_format(self):
        return '%s:%s - %s "%s"' % \
            (self.code, self.error_index,
             self.description(), self.short_text())

    def format(self, format='text'):
        if format == 'json':
            return self.json_format()
        return self.text_format()
