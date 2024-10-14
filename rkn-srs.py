#!/usr/bin/env python3

import argparse


def main(input_file, output_file): ...


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script to convert domains list to srs sing box format',
    )
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path')
    args = parser.parse_args()
    main(args.input, args.output)
