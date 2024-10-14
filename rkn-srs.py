#!/usr/bin/env python3

import argparse


def main(input_file, output_file): ...


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script to convert domain list to srs sing box format',
    )
    parser.add_argument(
        '-i', '--input', type=str, help='Input file path', required=True
    )
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()
    main(args.input, args.output)
