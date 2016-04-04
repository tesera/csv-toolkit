import unittest
from StringIO import StringIO
from replace import TextReplacer

class TextParserTest(unittest.TestCase):
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

class TextReplacerTest(unittest.TestCase):
    def setUp(self):
        self.sample_csv = 'test/fixtures/sample-dirty.csv'

    def file_contents(self, csv):
        with open(csv) as f:
            return f.read().strip()

    def test_global_replace(self):
        expected_csv = 'test/fixtures/sample-clean.csv'
        replacer = TextReplacer(['--search', 'NA', '--replace', '', '--input', self.sample_csv])
        replacer.args.output = StringIO()
        replacer.replace()
        self.assertEqual(replacer.args.input.name, self.sample_csv)
        self.assertEqual(replacer.args.output.getvalue().strip(), self.file_contents(expected_csv))

    def test_field_replace(self):
        expected_csv = 'test/fixtures/sample-clean-name.csv'
        replacer = TextReplacer(['--search', 'NA', '--replace', '', '--field', 'NAME', '--input', self.sample_csv])
        replacer.args.output = StringIO()
        replacer.replace()
        self.assertEqual(replacer.args.input.name, self.sample_csv)
        self.assertEqual(replacer.args.output.getvalue().strip(), self.file_contents(expected_csv))
