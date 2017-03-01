#!/usr/bin/env python

import argparse
import csv
import sys
import re
flatten = lambda l: [item for sublist in l for item in sublist]

def main():
    parser = argparse.ArgumentParser('./copy_columns.py', description='Copy columns from one CSV into a new one.')
    parser.add_argument('-c', '--column', help='Column to use when filtering', required=True)
    parser.add_argument('-f', '--filters', help='Values to include when filtering', required=True, action='append', nargs='*')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
    args = parser.parse_args()
    filters = flatten(args.filters)

    writer = csv.writer(args.output, lineterminator="\n")
    for index, row in enumerate(csv.reader(iter(args.input.readline, ''), delimiter=',')):
        if index == 0:
            filter_column = row.index(args.column)
            writer.writerow(row)
        else:
            if row[filter_column] in filters:
                writer.writerow(row)

        # row = [c for index, c in enumerate(row) if index in filters]
        # writer.writerow(row)


if __name__ == "__main__":
    main()
