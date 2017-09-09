import sys
from os.path import basename, splitext
from .parser import parse


def execute():
    in_file = sys.argv[1]

    if len(sys.argv) > 2:
        out_file = sys.argv[2]
    else:
        out_file = splitext(basename(in_file))[0] + '.md'

    parse(in_file, out_file)


if __name__ == '__main__':
    execute()
