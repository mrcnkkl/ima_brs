from typing import List, Dict
from ima.db.db import AbstractDb


class ServiceManager:

    def __init__(self, db: AbstractDb, *args, **kwargs):
        self.historical_service = kwargs.get("historical_service", None)
        self.db = db

    #TODO
    def save_historical(self, tickers: List[str]):
        for ticker in tickers:
            pass
            # self.db.insert_historical_data()
