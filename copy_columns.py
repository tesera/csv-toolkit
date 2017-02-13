#!/usr/bin/env python

import argparse
import csv
import sys
import re
flatten = lambda l: [item for sublist in l for item in sublist]

def main():
    parser = argparse.ArgumentParser('./copy_columns.py', description='Copy columns from one CSV into a new one.')
    parser.add_argument('-f', '--filters', help='Prefix to filter csv files before join', required=True, action='append', nargs='*')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
    args = parser.parse_args()
    filters = None

    for index, row in enumerate(csv.reader(iter(args.input.readline, ''), delimiter=',')):
        writer = csv.writer(args.output, lineterminator="\n")
        if index == 0:
            filters = list(map(lambda r: filter(re.compile(r).match, row), flatten(args.filters)))
            filters = flatten(filters)
            filters = reduce(lambda x,y: x+[y] if not y in x else x, filters,[])
            filters = map(lambda col: row.index(col), filters)
            filters = sorted(filters)

        row = [c for index, c in enumerate(row) if index in filters]
        writer.writerow(row)


if __name__ == "__main__":
    main()
