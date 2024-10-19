import subprocess

from core.constants import OUTPUT_DIR, SING_BOX_TEMPLATE


def convert_plain_domains_to_json_ruleset(domains: list[str]) -> dict:
    """Convert plain domains to sing-box format.

    This function takes a list of plain domains and returns a JSON string
    representing the sing-box ruleset.

    Args:
        domains (list[str]): A list of plain domains.

    Returns:
        str: A JSON string representing the sing-box ruleset.
    """
    template = SING_BOX_TEMPLATE.copy()
    template['rules'][0]['domain_suffix'] = list(domains)
    return template


def compile_srs_from_ruleset(ruleset_file: str) -> None:
    """Compile SRS from a ruleset file.

    Args:
        ruleset_file (str): The name of the ruleset file.
    """
    print(f'Compiling {ruleset_file}.srs...')
    subprocess.run(
        [
            'sing-box',
            'rule-set',
            'compile',
            f'{OUTPUT_DIR}/{ruleset_file}.json',
            '-o',
            f'{OUTPUT_DIR}/{ruleset_file}.srs',
        ]
    )
