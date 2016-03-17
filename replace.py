#!/usr/bin/env python

import argparse

def main():
  parser = argparse.ArgumentParser('cat coordinates.csv | ./step3.py', description='Append TMS to csv with lat/long.')
  parser.add_argument('-z', '--zoom', type=int, help='zoom level', required=True)
  args = parser.parse_args()
  writer = csv.writer(sys.stdout)

if __name__ == "__main__":
  main()