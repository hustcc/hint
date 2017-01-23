# -*- coding: utf-8 -*-
'''
Created on Jan 23, 2017

@author: hustcc
'''
import unittest
import hint


class TestE1xx(unittest.TestCase):
    def setUp(self):
        pass

    def test_e301_json(self):
        # check file
        errors = hint.check_file('tests/md/E301.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E301.md', [])), 3)
        for e in errors.get('tests/md/E301.md', []):
            self.assertEqual(e.get('code'), 'E301')

        # ignore
        errors = hint.check_file('tests/md/E301.md', ignore='E301')

        self.assertEqual(len(errors.get('tests/md/E301.md', [])), 0)

    def test_e301_text(self):
        # check file
        errors = hint.check_file('tests/md/E301.md', format='text')
        errors = errors.split('\n\n')
        self.assertEqual(len(errors), 1)
        errors = errors[0].split('\n')
        self.assertEqual(len(errors), 4)
        # ignore
        errors = hint.check_file('tests/md/E301.md',
                                 format='text',
                                 ignore='E301')
        self.assertEqual(errors.strip(), '')


if __name__ == '__main__':
    unittest.main()
