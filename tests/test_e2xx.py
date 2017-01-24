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

    def test_e201_json(self):
        # check file
        errors = hint.check_file('tests/md/E201.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E201.md', [])), 3)
        for e in errors.get('tests/md/E201.md', []):
            self.assertEqual(e.get('code'), 'E201')

        # ignore
        errors = hint.check_file('tests/md/E201.md', ignore='E201')

        self.assertEqual(len(errors.get('tests/md/E201.md', [])), 0)

    def test_e201_text(self):
        # check file
        errors = hint.check_file('tests/md/E201.md', format='text')
        errors = errors.split('\n\n')
        self.assertEqual(len(errors), 1)
        errors = errors[0].split('\n')
        self.assertEqual(len(errors), 4)
        # ignore
        errors = hint.check_file('tests/md/E201.md',
                                 format='text',
                                 ignore='E201')
        self.assertEqual(errors.strip(), '')

    def test_e202_json(self):
        # check file
        errors = hint.check_file('tests/md/E202.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E202.md', [])), 3)
        for e in errors.get('tests/md/E202.md', []):
            self.assertEqual(e.get('code'), 'E202')

        # ignore
        errors = hint.check_file('tests/md/E202.md', ignore='E202')

        self.assertEqual(len(errors.get('tests/md/E202.md', [])), 0)

    def test_e203_text(self):
        # check file
        errors = hint.check_file('tests/md/E203.md', format='text')
        errors = errors.split('\n\n')
        self.assertEqual(len(errors), 1)
        errors = errors[0].split('\n')
        self.assertEqual(len(errors), 3)
        # ignore
        errors = hint.check_file('tests/md/E203.md',
                                 format='text',
                                 ignore='E203')
        self.assertEqual(errors.strip(), '')

    def test_e204_json(self):
        # check file
        errors = hint.check_file('tests/md/E204.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E204.md', [])), 2)
        for e in errors.get('tests/md/E204.md', []):
            self.assertEqual(e.get('code'), 'E204')

        # ignore
        errors = hint.check_file('tests/md/E204.md', ignore='E204')

        self.assertEqual(len(errors.get('tests/md/E204.md', [])), 0)

    def test_e205_json(self):
        # check file
        errors = hint.check_file('tests/md/E205.md')
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(errors.get('tests/md/E205.md', [])), 2)
        for e in errors.get('tests/md/E205.md', []):
            self.assertEqual(e.get('code'), 'E205')

        # ignore
        errors = hint.check_file('tests/md/E205.md', ignore='E205')

        self.assertEqual(len(errors.get('tests/md/E205.md', [])), 0)


if __name__ == '__main__':
    unittest.main()
