#!/usr/bin/env python3

import asyncio
import argparse

from utils.domain_filtering import (
    extract_second_level_domains,
    filter_domains_by_keywords,
    get_antifilter_domains,
)


def main(input_file: str = None, output_file: str = None):
    # TODO: Add processing of input file argument
    second_level_domains: set[str] = extract_second_level_domains(
        domains=asyncio.run(get_antifilter_domains())
    )
    keyword_filtered_domains: set[str] = filter_domains_by_keywords(
        domains=second_level_domains
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script to convert domain list to srs sing-box format',
    )
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()
    main(args.input, args.output)
