import sys
import unittest
from StringIO import StringIO
from replace import CaseReplacer

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.expected = 'test'
        self.expected_file = 'test/fixtures/sample-dirty.csv'

    def test_case(self):
        replacer = CaseReplacer(['--case', 'upper'])

    def test_negate_case(self):
        with self.assertRaises(SystemExit) as exit:
            replacer = CaseReplacer(['--case', 'nocase'])
        self.assertEqual(exit.exception.code, 2)

    def test_field(self):
        replacer = CaseReplacer(['--case', 'upper', '--field', self.expected])
        self.assertEqual(replacer.args.field, self.expected)

    def test_input(self):
        replacer = CaseReplacer(['--case', 'upper', '--field', self.expected, '--input', self.expected_file])
        self.assertEqual(replacer.args.input.name, self.expected_file)

class ReplacerTest(unittest.TestCase):
    def setUp(self):
        self.sample_csv = 'test/fixtures/sample-dirty.csv'

    def file_contents(self, csv):
        with open(csv) as f:
            return f.read()

    def test_case_upper_global(self):
        expected_csv = 'test/fixtures/sample-uppercased.csv'
        replacer = CaseReplacer(['--case', 'upper', '--input', self.sample_csv])
        replacer.args.output = StringIO()
        replacer.replace()
        self.assertEqual(replacer.args.input.name, self.sample_csv)
        self.assertEqual(replacer.args.output.getvalue(), self.file_contents(expected_csv))

    # def test_case_upper_with_field(self):
    #     expected_csv = 'test/fixtures/sample-clean-name.csv'
    #     replacer = CaseReplacer(['--search', 'NA', '--replace', '', '--field', 'NAME', '--input', self.sample_csv])
    #     replacer.args.output = StringIO()
    #     replacer.replace()
    #     self.assertEqual(replacer.args.input.name, self.sample_csv)
    #     self.assertEqual(replacer.args.output.getvalue(), self.file_contents(expected_csv))
