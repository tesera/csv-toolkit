#!/usr/bin/env python

import argparse
import sys
import csv

def create_parser():
    parser = argparse.ArgumentParser('./replace.py', description='Replace or reformat fields in csv files')
    parser.add_argument('-s', '--search', help='search criteria', required=True)
    parser.add_argument('-r', '--replace', help='replace criteria', required=True)
    parser.add_argument('-f', '--field', help='Field to search/replace in', required=False)
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
    return parser

def main():
    args = create_parser().parse_args(sys.argv[1:])
    replace(args)

def replace(args):
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

if __name__ == "__main__":
    main()
