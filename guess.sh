#!/bin/sh


head $1 > test.csv
dataconvert test.csv _.json | \
  jq -r ".metadata.fields[] | .id + \" \" + .type" | \
  sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/,/g' | \
  sed s/Integer/int/g | \
  sed s/Float/double/g | \
  sed s/String/string/g
rm test.csv
