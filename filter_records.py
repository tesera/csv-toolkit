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
    parser.add_argument('-g', '--generate-index', help='Should the script generate a new index column to prepend')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin, help='Input file', required=False)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file', required=False)
    args = parser.parse_args()
    filters = flatten(args.filters)
    writer = csv.writer(args.output, lineterminator="\n")
    selected_columns = 0

    def writerow(row, header=False):
        if args.generate_index and header:
            writer.writerow([args.generate_index] + row)
        else:
            if args.generate_index:
                writer.writerow([selected_columns] + row)
            else:
                writer.writerow(row)

    for index, row in enumerate(csv.reader(iter(args.input.readline, ''), delimiter=',')):
        if index == 0:
            filter_column = row.index(args.column)
            writerow(row, True)
        else:
            if row[filter_column] in filters:
                writerow(row)
                selected_columns += 1

if __name__ == "__main__":
    main()
