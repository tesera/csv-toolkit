import unittest
from replace import TextReplacer

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.expected = 'test'
        self.expected_file = 'test/fixtures/sample-dirty.csv'

    def test_find(self):
        replacer = TextReplacer(['--search', self.expected, '--replace', '""'])
        self.assertEqual(replacer.args.search, self.expected)

    def test_replace(self):
        replacer = TextReplacer(['--search', '""', '--replace', self.expected])
        self.assertEqual(replacer.args.replace, self.expected)

    def test_field(self):
        replacer = TextReplacer(['--search', '""', '--replace', '""', '--field', self.expected])
        self.assertEqual(replacer.args.field, self.expected)

    def test_input(self):
        replacer = TextReplacer(['--search', '""', '--replace', '""', '--field', '""', '--input', self.expected_file])
        self.assertEqual(replacer.args.input.name, self.expected_file)
