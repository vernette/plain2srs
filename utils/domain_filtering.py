from asyncio.exceptions import TimeoutError

from aiohttp import (
    ClientConnectionError,
    ClientSession,
    ClientTimeout,
)

from core.constants import (
    ANTIFILTER_DOMAINS_URL,
    DOMAIN_KEYWORDS,
    MIN_REQUIRED_DOMAIN_PARTS,
    REQUEST_TIMEOUT,
    SECOND_LEVEL_DOMAIN_PARTS,
)


async def get_antifilter_domains(timeout: int = REQUEST_TIMEOUT) -> list[str]:
    """Fetch domains from the antifilter URL.

    This function retrieves a list of domains from the specified antifilter
    URL. It handles connection errors and timeouts appropriately.

    Args:
        timeout (int): The timeout for the request in seconds. Defaults to
            REQUEST_TIMEOUT.

    Returns:
        list[str]: A list of domains retrieved from the antifilter URL.

    Raises:
        TimeoutError: If the request times out.
        ClientConnectionError: If there is a connection error.
        Exception: For any other unexpected errors.
    """
    try:
        timeout_obj = ClientTimeout(total=timeout)
        async with ClientSession(timeout=timeout_obj) as session:
            async with session.get(ANTIFILTER_DOMAINS_URL) as response:
                domains = [
                    line.decode('utf-8').strip()
                    async for line in response.content
                ]
    except TimeoutError:
        print("Error! Didn't receive any response from antifilter!")
        quit(1)
    except ClientConnectionError:
        print(
            "Error! Couldn't connect to antifilter! "
            'Check your internet connection.'
        )
        quit(1)
    except Exception as e:
        print(f'Unexpected error! {e}')

    print(f'Got {len(domains)} domains from antifilter')
    return domains


def extract_second_level_domains(domains: list) -> set[str]:
    """Extract second-level domains from a list of domains.

    This function takes a list of domains and returns a set of
    second-level domains by removing subdomains.

    Args:
        domains (list): A list of domain names.

    Returns:
        set[str]: A set of second-level domains.
    """
    return {
        '.'.join(domain.split('.')[-SECOND_LEVEL_DOMAIN_PARTS:])
        for domain in domains
        if len(domain.split('.')) > MIN_REQUIRED_DOMAIN_PARTS
    }


def filter_domains_by_keywords(domains: set) -> set[str]:
    """Filter domains based on specified keywords.

    This function removes domains that contain any of the specified
    keywords.

    Args:
        domains (set): A set of domain names to filter.

    Returns:
        set[str]: A set of domains that do not contain the specified keywords.
    """
    for keyword in DOMAIN_KEYWORDS:
        domains = {domain for domain in domains if keyword not in domain}
    return domains
