# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2017

@author: hustcc
'''
import error


class Detector(error.BaseDetector):
    # 一些错误的状态情况
    error_sm = [
        ['E101', 'Z_L'],
        ['E101', 'L_Z'],
        ['E101', 'Z_V'],
        ['E101', 'V_Z'],

        ['E102', 'Z_N'],
        ['E102', 'N_Z'],

        ['E103', 'H_S'],
        ['E103', 'S_H'],

        ['E104', 'N_S_U'],  # 数字后面 ％℃°xn 不需要空格
        ['E104', 'N_S_V'],  # 数字后面 ％℃°xn 不需要空格
        ['E104', 'N_L'],  # 数字后面和其他英文单位需要空格
        ['E104', 'N_Z'],  # 数字后面和其他中文单位需要空格
    ]

    def __init__(self, tokens, p):
        super(Detector, self).__init__()
        self.tokens = tokens or []
        self.p = p or ''

    def errors(self):
        errors = []
        token_types = [token['type'] for token in self.tokens]
        token_types = '_'.join(token_types)
#         print self.p
#         print token_types
        for sm in self.error_sm:
            indexs = self.find_all_string(token_types, sm[1])
            for i in indexs:
                errors.append(error.Error(self.p, sm[0], i / 2 + 1))

        return errors
