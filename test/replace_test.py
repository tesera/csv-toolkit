import unittest
import replace

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = replace.create_parser()
        self.expected = 'test'

    def test_find(self):
        parsed = self.parser.parse_args(['--search', self.expected, '--replace', '""', '--input', '""', '--output', '""'])
        self.assertEqual(parsed.search, self.expected)

    def test_replace(self):
        parsed = self.parser.parse_args(['--search', '""', '--replace', self.expected, '--input', '""', '--output', '""'])
        self.assertEqual(parsed.replace, self.expected)

    def test_field(self):
        parsed = self.parser.parse_args(['--search', '""', '--replace', '""', '--field', self.expected, '--input', '""', '--output', '""'])
        self.assertEqual(parsed.field, self.expected)

    def test_input_output(self):
        parsed = self.parser.parse_args(['--search', '""', '--replace', '""', '--field', '""', '--input', self.expected, '--output', self.expected])
        self.assertEqual(parsed.input, self.expected)
        self.assertEqual(parsed.output, self.expected)
