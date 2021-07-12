# https://www.biznesradar.pl/notowania-historyczne/ABS-INVESTMENT
import datetime

from ima.config import Properties
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import date


class BiznesRadarHistorical:

    def __init__(self):
        self.br_hist_addr_base = f"{Properties.BIZNES_RADAR_BASE}/notowania-historyczne"
        self.date_addr_patters = "%Y%m%d"
        self.hist_data_table_class = "qTableFull"

    def _date(self, date: str) -> date:
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
        return date.date()

    def get_historical(self, ticker, pages=3) -> List[Dict]:
        data = []
        with requests.Session() as s:
            for i in range(pages):
                url = f"{self.br_hist_addr_base}/{ticker},{i}"
                print(f"{url}\n\n")
                page = s.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
                trs = soup.find_all('table', {"class": self.hist_data_table_class})[0].find_all('tr')
                for tr in trs:
                    tds = tr.find_all("td")
                    if tds:
                        data.append({
                            'ticker': ticker,
                            'Data': self._date(tds[0].text),
                            'Opening': tds[1].text,
                            'Max': tds[2].text,
                            'Min': tds[3].text,
                            'Closing': tds[4].text,
                            'Volume': tds[5].text,
                            'turnover': tds[6].text,
                        })
            return data