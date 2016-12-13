# -*- coding: utf-8 -*-
'''
Created on 2016年12月13日

@author: hustcc
'''
# Add space between CJK and Latin characters according to
# https://open.leancloud.cn/copywriting-style-guide.html. Mainly used for
# cleanning up Markdown documents.
#
# SYNOPSIS
#   add-space-between-latin-and-cjk input_file [out_file]
#
# CAUTION
#   If output_file is not provided, input_file is changed in-place.

import sys
import functools

def is_latin(c):
    return ord(c) < 256

# Some characters should not have space on either side.
def allow_space(c):
    return not c.isspace() and not (c in '，。；「」：《》『』、[]（）*_')

def add_space_at_boundry(prefix, next_char):
    if len(prefix) == 0:
        return next_char
    if is_latin(prefix[-1]) != is_latin(next_char) and \
            allow_space(next_char) and allow_space(prefix[-1]):
        return prefix + ' ' + next_char
    else:
        return prefix + next_char

if len(sys.argv) < 2:
    print('A minimum of one argument is required!\n')
    exit()

infile = open(sys.argv[1], 'r')
instr = infile.read()
infile.close()

outstr = functools.reduce(add_space_at_boundry, instr, '')
with open(sys.argv[2 if len(sys.argv) > 2 else 1], 'w') as outfile:
    outfile.write(outstr)