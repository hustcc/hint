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

    def test_e101_json(self):
        # check file
        errors = hint.check_file('tests/md/E101.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E101.md', [])), 2)
        for e in errors.get('tests/md/E101.md', []):
            self.assertEqual(e.get('code'), 'E101')

        # ignore
        errors = hint.check_file('tests/md/E101.md', ignore='E101')

        self.assertEqual(len(errors.get('tests/md/E101.md', [])), 0)

    def test_e101_text(self):
        # check file
        errors = hint.check_file('tests/md/E101.md', format='text')
        errors = errors.split('\n\n')
        self.assertEqual(len(errors), 1)
        errors = errors[0].split('\n')
        self.assertEqual(len(errors), 3)
        # ignore
        errors = hint.check_file('tests/md/E101.md',
                                 format='text',
                                 ignore='E101')
        self.assertEqual(errors.strip(), '')

    def test_e102(self):
        # check file
        errors = hint.check_file('tests/md/E102.md', format='text')
        errors = errors.split('\n\n')
        self.assertEqual(len(errors), 1)
        for e in errors:
            e = e.split('\n')
            self.assertEqual(len(e), 3 + 1)
        # ignore
        errors = hint.check_file('tests/md/E102.md', ignore='E102')
        self.assertEqual(len(errors.get('tests/md/E102.md', [])), 1)

    def test_e103(self):
        # check file
        errors = hint.check_file('tests/md/E103.md', format='json')
        self.assertEqual(len(errors), 1)
        errors = errors.get('tests/md/E103.md', [])
        self.assertEqual(len(errors), 5)
        for e in errors:
            self.assertEqual(e.get('code'), 'E103')
        # ignore
        errors = hint.check_file('tests/md/E103.md',
                                 ignore='E103',
                                 format='text')
        self.assertEqual(errors.strip(), '')


if __name__ == '__main__':
    unittest.main()
