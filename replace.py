#!/usr/bin/env python

import sys
import argparse

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
    pass


if __name__ == "__main__":
    main()
