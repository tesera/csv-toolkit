#!/usr/bin/env python

import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser('./replace.py', description='Replace or reformat fields in csv files')
    parser.add_argument('-s', '--search', help='search criteria', required=True)
    parser.add_argument('-r', '--replace', help='replace criteria', required=True)
    parser.add_argument('-f', '--field', help='Field to search/replace in', required=False)
    return parser


def main():
    args = create_parser().parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()
