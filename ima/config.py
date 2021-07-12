import sqlalchemy.engine.url as sql_url
import os


class Properties:
    STOOQ_ADDR_BASE = "https://stooq.pl"
    BIZNES_RADAR_BASE = "https://www.biznesradar.pl"
    TEMP = os.getenv("IMA_TEMP") or "C:\\projects\\InvestorMateApp\\ima_brs\\ima\\temp"
    DB_URL = os.getenv("IMA_DB_URL") or sql_url.make_url("sqlite:///C:\\projects\\InvestorMateApp\\ima_brs\\ima\\db\\ima.db")
