import requests
from bs4 import BeautifulSoup
import re
from ima.config import Properties


class StooqTickerService:

    def __init__(self, tickers_page_base: str = f"{Properties.STOOQ_ADDR_BASE}/t/?i=523&v=0&l=",
                 tickers_table_row_rx_pattern: str = "^r_[0-9]{1,3}$"):
        self.tickers_page_base = tickers_page_base
        self.tickers_table_row_rx_pattern = tickers_table_row_rx_pattern
        self.session = None

    def _get_table_rows(self, html_page: str):
        soup = BeautifulSoup(html_page, 'html.parser')
        return soup.find_all("tr", id=re.compile(self.tickers_table_row_rx_pattern))

    def _tickers_page_contains_table(self, html_page: str) -> bool:
        return True if self._get_table_rows(html_page) else False

    def get_tickers(self):
        page_count = 1
        page_url = self.tickers_page_base + str(page_count)
        with requests.Session() as s:
            page = s.get(page_url)
            while self._tickers_page_contains_table(page.text):
                for tr in self._get_table_rows(page.text):
                    tds_tick = tr.find_all("a")
                    tds_link = tr.find_all("a")
                    tds_name = tr.find_all(id='f10')
                    for tick, link, nazwa in zip(tds_tick, tds_link, tds_name):
                        yield {'ticker': tick.get_text(),
                               'www': f"{Properties.STOOQ_ADDR_BASE}/{link['href']}",
                               'name': nazwa.get_text()}
                page_count += 1
                page_url = self.tickers_page_base + str(page_count)
                page = s.get(page_url)