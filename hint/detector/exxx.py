# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2017

@author: hustcc
'''
import error
import re


class Detector(error.BaseDetector):
    # 一些错误的状态情况
    error_sm = [
        ['E101', 'ZL'],
        ['E101', 'LZ'],
        ['E101', 'ZV'],
        ['E101', 'VZ'],

        ['E102', 'ZN'],
        ['E102', 'NZ'],

        ['E103', 'HS'],
        ['E103', 'SH'],

        ['E104', 'NSU'],  # 数字后面 ％℃° 不需要空格

        ['E201', 'HH'],  # 不重复使用标点符号
        ['E201', 'HI'],
        ['E201', 'IH'],

        ['E205', 'IL'],  # 英文标点后面需要有空格，不能直接跟英文
        ['E205', 'IZ'],  # 英文标点后面需要有空格，不能直接跟中文，需要有空格

        ['E301', 'F'],  # 数字不使用半角字符
    ]

    # 错误类型的自定义处理规则，因为规则比较复杂，只能自定义的去检测
    error_fsm = [
        ['E202', ''],  # 只有中文或中英文混排中，一律使用中文全角标点
        ['E203', ''],  # 如果出现整句英文，则在这句英文中使用英文、半角标点
        ['E204', ''],  # 省略号请使用……标准用法
        ['E206', ''],  # 文中出现英文、半角标点之后，需要有空格
    ]

    def __init__(self, tokens, p):
        super(Detector, self).__init__()
        self.tokens = tokens or []
        self.p = p or ''
        self.error_fsm = [
            ['E202', self._e202],  # 只有中文或中英文混排中，一律使用中文全角标点
            ['E203', self._e203],  # 如果出现整句英文，则在这句英文中使用英文、半角标点
            ['E204', self._e204],  # 省略号请使用……标准用法
            ['E206', self._e206],  # 文中出现英文、半角标点之后，需要有空格
        ]

    # 比较常用的检测器
    def _common_detector(self, sm, token_types):
        indexs = self.find_all_string(token_types, sm[1])
        return [error.Error(self.p, sm[0], i + 1) for i in indexs]

    # 只有中文或中英文混排中，一律使用中文全角标点
    def _e202(self, error_code, token_types):
        # TODO
        return []

    # 如果出现整句英文，则在这句英文中使用英文、半角标点
    def _e203(self, error_code, token_types):
        return []

    # 省略号请使用……标准用法
    def _e204(self, error_code, token_types):
        # TODO
        return []

    # 文中出现英文、半角标点之后，需要有空格
    def _e206(self, error_code, token_types):
        # 英文和标点之间不需要空格
        errors_all = re.findall(r'LS{1,}I', token_types)
        i = -1
        errors = []
        for e in errors_all:
            i = token_types.find(e, i + 1)
            if i != -1:
                errors.append(error.Error(self.p, error_code, i + 1))
        return errors

    def errors(self):
        errors = []
        token_types = [token['type'] for token in self.tokens]
        token_types = ''.join(token_types)
#         print self.p
#         print token_types
        # 1. 处理 common_detector
        for sm in self.error_sm:
            errors += self._common_detector(sm, token_types)

        # 2. 处理正则规则
        for sm in self.error_fsm:
            errors += sm[1](sm[0], token_types)

        return errors
