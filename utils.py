import sys

import requests
from requests.exceptions import ConnectionError, Timeout

from constants import ANTIFILTER_DOMAINS_URL


def get_antifilter_domains(timeout: int = 10) -> list:
    domains = []
    try:
        with requests.get(
            ANTIFILTER_DOMAINS_URL, timeout=timeout, stream=True
        ) as response:
            for line in response.iter_lines():
                domains.append(line.decode('utf-8').strip())
    except Timeout:
        print("Error! Didn't receive any response from antifilter!")
        sys.exit(1)
    except ConnectionError:
        print(
            "Error! Couldn't connect to antifilter! "
            'Check your internet connection.'
        )
        sys.exit(1)
    return domains
