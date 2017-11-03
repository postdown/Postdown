import sys
from os.path import basename, splitext
from .parser import parse


def execute():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--zh", action="store_true", help="生成中文文档")
    parser.add_argument("json", type=str, help="Postman JSON文件")
    parser.add_argument("markdown", type=str, help="生成的文档", nargs='?')

    args = parser.parse_args()

    in_file = args.json

    if args.markdown:
        out_file = args.markdown
    else:
        out_file = splitext(basename(in_file))[0] + '.md'

    if args.zh:
        parse_zh(in_file, out_file)
    else:
        parse(in_file, out_file)



if __name__ == '__main__':
    execute()
