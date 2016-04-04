#!/usr/bin/env python

import argparse
import sys
import csv

class TextReplacer():
    def __init__(self,argv):
        self.parser = argparse.ArgumentParser('./replace.py text', description='Replace or reformat fields in csv files')
        self.parser.add_argument('-s', '--search', help='search criteria', required=True)
        self.parser.add_argument('-r', '--replace', help='replace criteria', required=True)
        self.parser.add_argument('-f', '--field', help='Field to search/replace in', required=False)
        self.parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
        self.parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
        self.args = self.parser.parse_args(argv)

    def replace(self):
        args = self.args
        column_names = {}
        writer = csv.writer(args.output, lineterminator="\n")
        for index, row in enumerate(csv.reader(iter(args.input.readline, ''), delimiter=',')):
            if index == 0:
                for col in row: column_names[col] = row.index(col)
            else:
                if args.field:
                    row[column_names[args.field]] = row[column_names[args.field]].replace(args.search, args.replace)
                else:
                    row = [cell.replace(args.search, args.replace) for cell in row]
            writer.writerow(row)
            args.output.flush()


class CaseReplacer():
    cases = ('camel', 'title', 'upper', 'lower')

    def __init__(self, argv):
        self.parser = argparse.ArgumentParser('./replace.py case')
        self.parser.add_argument('-f', '--field', help='Field to search/replace in', required=False)
        self.parser.add_argument('-c', '--case', help='Case to use. Valid options are: camel, title, upper, lower', required=True)
        self.parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
        self.parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
        self.args = self.parser.parse_args(argv)
        if self.args.case not in self.cases:
            self.parser.error('case must be one of: {}'.format(', '.join(self.cases)))

    def replace(self):
        args = self.args
        column_names = {}
        writer = csv.writer(args.output, lineterminator="\n")
        for index, row in enumerate(csv.reader(iter(args.input.readline, ''), delimiter=',')):
            if index == 0:
                for col in row: column_names[col] = row.index(col)
            else:
                if args.field:
                    row[column_names[args.field]] = row[column_names[args.field]].upper()
                else:
                    row = [cell.upper() for cell in row]
            writer.writerow(row)
            args.output.flush()

def main():
    command_parser = argparse.ArgumentParser(
        description='Replaces text in CSV files',
        usage='''./replace.py <command> [<args>]

The commands are:
    text
    case
    ''')
    command_parser.add_argument('command', help='Subcommand to run')
    command = command_parser.parse_args(sys.argv[1:2]).command
    replacer = globals()[command.capitalize()+"Replacer"](sys.argv[2:])
    replacer.replace()

if __name__ == "__main__":
    main()
