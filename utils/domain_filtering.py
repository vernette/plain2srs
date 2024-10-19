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
    return {
        '.'.join(domain.split('.')[-SECOND_LEVEL_DOMAIN_PARTS:])
        for domain in domains
        if len(domain.split('.')) > MIN_REQUIRED_DOMAIN_PARTS
    }


def filter_domains_by_keywords(domains: set) -> set[str]:
    for keyword in DOMAIN_KEYWORDS:
        domains = {domain for domain in domains if keyword not in domain}
    return domains
