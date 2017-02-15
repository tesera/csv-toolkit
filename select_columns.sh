#!/bin/sh

cut \
  -f $(head -1 $1 | sed 's/,/\'$'\n/g' | grep -n 'column name' | cut -f1 -d,) \
  -d, \
  file.csv
