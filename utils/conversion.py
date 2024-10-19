import json

from core.constants import SING_BOX_TEMPLATE


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
