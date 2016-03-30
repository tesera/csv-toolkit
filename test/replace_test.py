import unittest
from StringIO import StringIO
import replace

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.sample_csv = 'test/fixtures/sample-dirty.csv'

    def file_contents(self, csv):
        with open(csv) as f:
            return f.read()

    def test_global_replace(self):
        expected_csv = 'test/fixtures/sample-clean.csv'
        parsed = replace.create_parser().parse_args(['--search', 'NA', '--replace', '', '--input', self.sample_csv])
        parsed.output = StringIO()
        replace.replace(parsed)
        self.assertEqual(parsed.input.name, self.sample_csv)
        self.assertEqual(parsed.output.getvalue(), self.file_contents(expected_csv))

    def test_field_replace(self):
        expected_csv = 'test/fixtures/sample-clean-name.csv'
        parsed = replace.create_parser().parse_args(['--search', 'NA', '--replace', '', '--field', 'NAME', '--input', self.sample_csv])
        parsed.output = StringIO()
        replace.replace(parsed)
        self.assertEqual(parsed.input.name, self.sample_csv)
        self.assertEqual(parsed.output.getvalue(), self.file_contents(expected_csv))
