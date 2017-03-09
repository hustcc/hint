# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2017

@author: hustcc
'''
from __future__ import absolute_import
from hint.detector import error
import re


class Detector(error.BaseDetector):
    # 一些错误的状态情况
    error_sm = [
        ['E101', 'ZL'],  # 中英文之间需要增加空格
        ['E101', 'LZ'],  # 中英文之间需要增加空格

        ['E102', 'ZN'],  # 中文与数字之间需要增加空格
        ['E102', 'NZ'],  # 中文与数字之间需要增加空格

        ['E103', 'HS'],  # 全角标点与其他字符之间不加空格
        ['E103', 'SH'],  # 全角标点与其他字符之间不加空格

        ['E104', 'NSU'],  # 数字后面 ％℃° 不需要空格

        ['E201', 'HH'],  # 不重复使用标点符号 中文中文
        ['E201', 'HI'],  # 不重复使用标点符号 中文英文
        ['E201', 'IH'],  # 不重复使用标点符号 英文中文
        ['E201', 'II'],  # 不重复使用标点符号 英文英文

        ['E202', 'ZI'],  # 只有中文或中英文混排中，一律使用中文全角标点，中文英文标点
        ['E202', 'IZ'],  # 英文标点，中文

        ['E301', 'F'],  # 数字不使用半角字符
    ]

    # 错误类型的自定义处理规则，因为规则比较复杂，只能自定义的去检测
    error_fsm = [
        ['E203', ''],  # 如果出现整句英文，则在这句英文中使用英文、半角标点
        ['E204', ''],  # 省略号请使用……标准用法
        ['E205', ''],  # 英文和后面的半角标点之间不需要空格
    ]

    def __init__(self, tokens, p):
        super(Detector, self).__init__()
        self.tokens = tokens or []
        self.p = p or ''
        self.error_fsm = [
            ['E203', self._e203],  # 如果done出现整句英文，则在这句英文中使用英文、半角标点
            ['E204', self._e204],  # 省略号请使用……标准用法
            ['E205', self._e205],  # 文中出现英文、半角标点之后，需要有空格
        ]

    # 比较常用的检测器
    def _common_detector(self, sm, token_types):
        indexs = self.find_all_string(token_types, sm[1])
        return [error.Error(self.p, sm[0], i + 1) for i in indexs]

    # 如果出现整句英文，则在这句英文中使用英文、半角标点
    def _e203(self, error_code, token_types):
        # 如果整行中只有 数字、空格、英文标点、英文、中文标点
        errors_all = re.match(r'^[NSILOH]*$', token_types)

        errors = []
        if not errors_all:
            return errors

        i = -1
        while True:
            i = token_types.find('H', i + 1)
            if i == -1:
                break
            errors.append(error.Error(self.p, error_code, i + 1))
        return errors

    # 省略号请使用……标准用法
    def _e204(self, error_code, token_types):
        errors_all = re.findall(r'[^E]E{1,}[^E]{0,1}', token_types)
        i = -1
        errors = []
        for e in errors_all:
            if e.count('E') != 2:
                i = token_types.find(e, i + 1)
                if i != -1:
                    errors.append(error.Error(self.p, error_code,
                                              i + 1 + e.rindex('E')))
        return errors

    # 文中出现英文、半角标点之后，需要有空格
    def _e205(self, error_code, token_types):
        # 英文和标点之间不需要空格
        errors_all = re.findall(r'LS{1,}I', token_types)
        i = -1
        errors = []
        for e in errors_all:
            i = token_types.find(e, i + 1)
            if i != -1:
                errors.append(error.Error(self.p, error_code, i + 2))
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
