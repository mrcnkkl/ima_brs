from sqlalchemy import (create_engine)
from ima.db.model import *
from typing import List, Dict
from ima.config import Properties


class AbstractDb:
    def create_tables(self):
        pass

    def insert_tickers(self, tickers: List[Dict]):
        pass

    def insert_historical_data(self, data: List[Dict]):
        pass

    def delete_historical_data(self):
        pass


class Db(AbstractDb):
    def __init__(self, url=None):
        url = url or Properties.DB_URL
        self.engine = create_engine(url=url, echo=True)

    def create_tables(self):
        meta.create_all(self.engine)

    def insert_tickers(self, tickers: List[Dict]):
        with self.engine.connect() as conn:
            conn.execute(stooq_tickers.insert(tickers))

    def insert_historical_data(self, data: List[Dict]):
        with self.engine.connect() as conn:
            conn.execute(biznes_radar_hist.insert(data))

    def delete_historical_data(self):
        with self.engine.connect() as conn:
            conn.execute(biznes_radar_hist.delete())
