# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''

errors = {
    # 空格
    'E101': u'英文与非标点的中文之间需要有一个空格',
    'E102': u'数字与非标点的中文之间需要有一个空格',
    'E103': u'全角标点与其他字符之间不加空格',
    'E104': u'除了％、℃、°、以及倍数单位（如 2x、3n）之外，数字与单位之间需要增加空格',
    # 标点符号
    'E201': u'不重复使用标点符号',
    'E202': u'只有中文或中英文混排中，一律使用中文全角标点',
    'E203': u'如果出现整句英文，则在这句英文中使用英文、半角标点',
    'E204': u'中文文案中使用中文引号「」和『』，其中「」为外层引号',
    'E205': u'省略号请使用……标准用法',
    'E206': u'英文中出现英文、半角标点之后，需要有空格',
    # 数字
    'E301': u'数字不使用半角字符',
    'E401': u'遇到完整的英文整句、特殊名词，其內容使用半角标点'
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

        return u'%s<%s>%s' % (self.text[start:self.error_index],
                              self.code,
                              self.text[self.error_index:end])

    def json_format(self, fn):
        rst = {}
        rst['code'] = self.code
        rst['text'] = self.short_text()
        rst['error_index'] = self.error_index
        rst['description'] = self.description()
        return {fn: rst}

    def text_format(self, fn):
        return u'%s:%s:COL<%s>:%s:"%s"' % \
            (fn, self.code, self.error_index,
             self.description(), self.short_text())

    def format(self, format='text', fn='anonymous'):
        if format == 'json':
            return self.json_format(fn)
        return self.text_format(fn)


class BaseDetector(object):
    def __ini__(self):
        pass

    def errors(self):
        return []

    def find_all_string(self, str, sub):
        index = []
        i = 0
        while i != -1:
            i = str.find(sub, i + 1)
            if i == -1:
                return index
            else:
                index.append(i)

        return index
