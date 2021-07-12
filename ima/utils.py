import requests
import pathlib


def save_page_to_file(url: str, path: str = "default.html") -> None:
    r = requests.get(url)
    with open(path, "a") as file:
        file.write(r.text)


def mkdir(path: str, parents=False):
    pathlib.Path(path).mkdir(parents=parents, exist_ok=True)


def _hash(input: str) -> str:
    pass

# save_page_to_file("https://www.biznesradar.pl/notowania-historyczne/ABS-INVESTMENT",
#                   "../brudnopis/hist-biznes-radar.html")

import hashlib

v = "1234abcd!@#$ dupa ccxcxcxcxcxcx"
r = hashlib.sha256(v.encode())
print(f'{r.hexdigest()}')
print(f'###')