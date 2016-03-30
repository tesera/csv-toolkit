import unittest
import replace

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = replace.create_parser()
        self.expected = 'test'

    def test_find(self):
        parsed = self.parser.parse_args(['--find', self.expected, '--replace', '""'])
        self.assertEqual(parsed.find, self.expected)

    def test_replace(self):
        parsed = self.parser.parse_args(['--find', '""', '--replace', self.expected])
        self.assertEqual(parsed.replace, self.expected)
