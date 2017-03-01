# csv-toolkit
Some tools for cleaning up data in csv files

## Usage

The python tools include a usage section accessable from commandline.

    ./replace.py --help
    ./replace.py <command> --help

The awk tools usage is as follows:

    ./select_columns.awk -v cols=<filter1,filter2> input.csv > output.csv

## Testing
Run the tests using python unittest module

    python -m unittest discover --pattern=*_test.py
