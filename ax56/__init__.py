import requests

__version__ = '0.1.0'

__title__ = "ax56"
__github_repo__ = "ax56"
__author__ = 'Nate Harris'
__author_email__ = 'n8gr8gbln@gmail.com'
__github_username__ = "nwithan8"
__copyright__ = "Copyright © 2021 - Nate Harris"
__license__ = 'GNU General Public License v3 (GPLv3)'
__description__ = "Get lengthened URLs from A(x56)"
__keywords__ = ["A(x56)", "link", "extender", "expander", "bit.ly", "url", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]


def link(url: str):
    return _api_request(url=url)


base = "https://api.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com/a"


def _api_request(url: str):
    res = requests.get(base, params={'url': url})
    if res.text == "INVALID_URL":
        return None
    return res.text
