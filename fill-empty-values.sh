#!/bin/bash
sed -e "s/^,/0,/g" -e "s/,,/,0,/g" -e "s/,$/,0/g"
