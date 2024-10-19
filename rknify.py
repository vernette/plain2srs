#!/usr/bin/env python3

import argparse
import asyncio

from utils.conversion import (
    compile_srs_from_ruleset,
    convert_plain_domains_to_json_ruleset,
)
from utils.domain_filtering import (
    extract_second_level_domains,
    filter_domains_by_keywords,
    get_antifilter_domains,
)
from utils.file_operations import save_json


def main(input_file: str, output_file: str):
    if output_file is None:
        output_file = 'output'
    # TODO: If output file exists, ask user if they want to overwrite
    # TODO: Add processing of input file argument
    second_level_domains: set[str] = extract_second_level_domains(
        domains=asyncio.run(get_antifilter_domains())
    )
    print(f'Got {len(second_level_domains)} second-level domains')
    keyword_filtered_domains: set[str] = filter_domains_by_keywords(
        domains=second_level_domains
    )
    print(f'Got {len(keyword_filtered_domains)} domains after filtering')

    ruleset_json = convert_plain_domains_to_json_ruleset(
        domains=keyword_filtered_domains
    )
    save_json(json_data=ruleset_json, output_file=output_file)
    compile_srs_from_ruleset(ruleset_file=output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script to convert domain list to srs sing-box format',
    )
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()
    main(args.input, args.output)
