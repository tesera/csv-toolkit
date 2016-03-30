import unittest
from StringIO import StringIO
import replace

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.sample_csv = 'test/fixtures/sample.csv'

    def sample_file_contents(self):
        with open(self.sample_csv) as f:
            return f.read()

    def test_stdout(self):
        parsed = replace.create_parser().parse_args(['--search', 'NA', '--replace', '', '--input', self.sample_csv])
        parsed.output = StringIO()
        self.assertEqual(parsed.input.name, self.sample_csv)
        self.assertEqual(parsed.output.getvalue(), self.sample_file_contents())
