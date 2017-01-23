# -*- coding: utf-8 -*-
'''
Created on 2016年12月13日

@author: hustcc
'''
import os


def is_latin(c):
    '''decide c is latin or not
    '''
    return c.isalpha()


def is_space(c):
    '''decide c is space，中文
    '''
    return c.isspace()


def is_number(c):
    # 是否是数字
    return c.isdigit()


def is_unit(c):
    # 判断是否为单位
    return 'TODO'


def is_zh_symbol(c):
    # 是否为中文符号
    return c in u'，。；「」：《》『』、[]（）？'


def is_fw_number(c):
    # 是否是圆角数字
    return c in u'０１２３４５６７８９'


def is_zh(c):
    '''判断是否为中文'''
    return u'\u4e00' <= c <= u'\u9fff' and True or False


def is_zh_unit(c):
    '''判断是否为单位'''
    return c in u'％℃°'


def is_en_unit(c):
    return c in 'xn'


def ignore_errorcode(errors, ignores):
    '''ignore the errors in ignores
    '''
    if not isinstance(ignores, list):
        ignores = ignores.split(',')
    # trim the error code
    ignores = [code.strip() for code in ignores]
    # ignore error codes.
    errors = [error for error in errors if error.code not in ignores]
    return errors


def format_errors(errors, format):
    return [e.format(format) for e in errors]


def typeof(c):
    if is_number(c):
        return 'N'  # number
    if is_zh_unit(c):
        return 'U'  # zh unit
    if is_en_unit(c):
        return 'V'  # en unit
    if is_space(c):
        return 'S'  # space
    if is_zh_symbol(c):
        return 'H'  # zh sym
    if is_fw_number(c):
        return 'F'  # fw number
    if is_zh(c):
        return 'Z'  # zh
    if is_latin(c):
        return 'L'  # latin
    return 'O'  # other， no limit


detectors_on = None


def load_detectors():
    '''加载所有的检测器'''
    global detectors_on
    if detectors_on:
        return detectors_on

    from detector import e1xx
    detectors_on = [e1xx.Detector]
#     detector_files = os.listdir(os.path.join(os.getcwd(), 'hint/detector/'))
#     for detector_file in detector_files:
#         if detector_file.endswith('.py') and \
#                 detector_file not in ['__init__.py', 'error.py']:
#             detector_file = detector_file[0:-3]
#             try:
#                 module_path = 'hint.detector.%s' % detector_file
#                 plugin = __import__(module_path)
#                 plugin_class = getattr(getattr(getattr(plugin, 'detector'),
#                                        detector_file), 'Detector')
#                 if plugin_class:
#                     detectors.append(plugin_class)
#             except:
#                 continue

    return detectors_on


def traversing_path(all_files, path, depth=0, max_depth=3, suffixs=['.md']):
    # 目录，新增一级
    depth += 1
    if depth > max_depth:
        return all_files

    ls = os.listdir(path)
    files = [f for f in ls if os.path.isfile(os.path.join(path, f))]
    dirs = [d for d in ls if os.path.isdir(os.path.join(path, d))]

    for d in dirs:
        all_files += traversing_path(all_files, os.path.join(path, d),
                                     depth=depth,
                                     max_depth=max_depth,
                                     suffixs=suffixs)
    # 添加到最后的 files 中
    fs = [os.path.join(path, f) for f in files if f[-3:] in suffixs]
    fs = depth == 1 and all_files + fs or fs
    return fs


if __name__ == '__main__':
    print(traversing_path([], 'E:/Work/git_code/hint', max_depth=4))
